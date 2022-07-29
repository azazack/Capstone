<template lang="pug">
.more-options
  FontAwesomeIcon.more-options-button.mx-auto(:icon="icon" @click="toggleShowMoreOptions" v-if="!hideIcon")
  slot(name="action" :click="toggleShowMoreOptions")
  .more-options-menu(v-if="showMoreOptions" v-on-clickaway="toggleShowMoreOptions")
    slot
</template>

<script lang="ts" setup>
import {faEllipsis} from "@fortawesome/free-solid-svg-icons/faEllipsis";
import { directive as vOnClickaway } from "vue3-click-away";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import { ref } from "vue";
defineProps({
  icon: {
    type: Object,
    default: () => faEllipsis,
  },
  hideIcon: Boolean,
});

const showMoreOptions = ref(false);

const toggleShowMoreOptions = (): void => {
  showMoreOptions.value = !showMoreOptions.value;
};
</script>

<style lang="scss">
.more-options {
  position: relative;
  display: flex;
  .more-options-button {
    width: 24px;
    cursor: pointer;
  }
  &.small {
    .more-options-button {
      width: 10px;
      height: 10px;
    }
  }
  .more-options-menu {
    position: absolute;
    z-index: 1;
    top: 30px;
    right: 5px;
    min-width: 150px;
    max-height: 200px;
    overflow-y: auto;
    width: fit-content;
    padding: 8px 0 4px 0;
    background-color: #fff;
    box-shadow: 0 0 1px 0 rgba(10, 31, 68, 0.08),
    0 8px 10px 0 rgba(10, 31, 68, 0.1);
    .menu-item {
      cursor: pointer;
      white-space: nowrap;
      color: #0a1f44;
      padding: 0 16px 0 20px;
      margin-bottom: 5px;
      font-size: 14px;
      line-height: 32px;
      text-align: left;
      a {
        text-decoration: none;
        color: inherit;
      }
      &:hover {
        background-color: #e2e2e2;
      }
    }
  }
  @media only screen and (max-height: 800px) {
    .more-options-menu {
      max-height: 120px;
    }
  }
}
</style>
