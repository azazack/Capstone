<template lang="pug">
  nav#sidebar(v-if="opened")
    ul.list-unstyled.sidebar-body
      li(v-for="(item, i) in menu" :key="i")
        component( :is="item.route ? 'router-link': 'a'" :to="item.route" data-toggle="collapse" :aria-expanded="show === item.name" class="dropdown-toggle collapsed" @click="showing(item.name)")
          font-awesome-icon.path-icon.me-2(:icon="item.icon" v-if="item.icon" :title="item.name")
          span.path-text {{ item.name }}
        transition(name="fadeHeight" mode="out-in" v-if="item.children")
          ul.list-unstyled( id="homeSubmenu" :class="{ show: show === item.name }" v-show="show === item.name")
            li( v-for="(subItem, i) in item.children" :key="i")
              router-link( :to="subItem.route" :class="{ 'router-link-active': $route.name.startsWith(subItem.route.name) }")
                font-awesome-icon.path-icon.me-2(:icon="subItem.icon" v-if="subItem.icon" :title="subItem.name")
                span.path-text {{ subItem.name }}
</template>

<script lang="ts" setup>
import type {PropType} from "vue";
import {onBeforeMount, ref} from "vue";
import {useRoute} from "vue-router";

const props = defineProps({
  menu: {
    type: Array as PropType<Menu[]>,
    required: true,
  },
  opened: {
    type: Boolean,
    required: true,
  },
});

const show = ref("");

const route = useRoute();

onBeforeMount(() => {
  props.menu.forEach((element: Menu) => {
    if (element.route?.name) {
      if (element.route?.name === route.name) show.value = element.name;
    } else {
      element.children?.forEach((child: Menu) => {
        if (child.route?.name) {
          if (route.name?.toString().includes(child.route.name))
            show.value = element.name;
        }
      });
    }
  });
  console.log("mounted")
});

function showing(item: string): void {
  if (show.value === item) show.value = "";
  else show.value = item;
}
</script>

<style lang="scss">
.fadeHeight-enter-active,
.fadeHeight-leave-active {
  transition: all 0.3s;
  max-height: 1030px;
}

.fadeHeight-enter,
.fadeHeight-leave-to {
  opacity: 0;
  max-height: 0;
}

#sidebar {
  min-width: 250px;
  max-width: 250px;
  min-height: 100vh;
  background: white;
  color: darken($primary-color, 40);
  transition: all 0.3s;
  -moz-box-shadow: -3px 4px 4px 0px #555;
  -webkit-box-shadow: -3px 4px 4px 0px #555;
  box-shadow: -3px 4px 4px 0px #555;
  border-bottom-right-radius: 20px;

  .logo-nav {
    padding-top: 35px;
    padding-bottom: 35px;
    text-align: center;
    border-bottom: 1px solid #f4f7fe;

    img {
      height: 35px;
      object-fit: scale-down;
    }
  }

  .list-unstyled {
    padding-left: 0;
    list-style: none;
  }

  ul {
    &.sidebar-body {
      height: calc(100% - 140px);
      overflow-y: auto;
      margin-top: 2rem;
    }

    ul {
      a {
        font-size: 0.75em !important;
        padding-left: 50px !important;
      }
    }

    li {
      a {
        padding: 12px 30px;
        font-size: 0.75em;
        display: block;
      }

      .router-link-active,
      a:hover,
      a[aria-expanded="true"] {
        color: $primary-color;
        background: #fff;
        border-right: 3px solid $primary-color;
        font-weight: bold;
      }
    }
  }

  &.opened {
    min-width: 70px;
    max-width: 70px;
    transition: all 0.5s ease-in-out;

    .sidebar-header {
      justify-content: center !important;

      .open-icon {
        transform: rotate(-180deg);
        transition: all 0.5s ease-in-out;
      }
    }

    .sidebar-body {
      .dropdown-toggle {
        display: flex;
        align-items: center;
        flex-direction: column;
      }

      .path-icon {
        font-size: 26px;
      }

      .path-text {
        display: none;
      }

      ul {
        li {
          a {
            display: flex;
            justify-content: center;
            font-size: 2em !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
          }
        }
      }
    }
  }

  &.active {
    margin-left: -250px;
  }

  a[data-toggle="collapse"] {
    position: relative;
  }

  .dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
  }

  @include media-breakpoint-down(lg) {
    #sidebar {
      margin-left: -250px;
    }
    #sidebar.active {
      margin-left: 0;
    }
  }
}
</style>
