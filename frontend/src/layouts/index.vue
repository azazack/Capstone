<template lang="pug">
TopBar(:is-mobile="isMobile" @showSidebar="opened = !opened")
Sidebar.side-fixed(:menu="menu" :opened="isOpen")
.wrapper(:class="{ 'wrapper-mobile': isMobile }")
  .w-100.py-3
    .mb-3
      .d-flex.justify-content-between.align-items-center
        #action-container
    router-view
</template>

<script lang="ts" setup>
import useMenu from "@/composables/useMenu";
import { computed, onBeforeUnmount, onMounted, ref } from "vue";
import Sidebar from "@/components/navbar.vue";
import { breakpointsBootstrapV5, useBreakpoints } from "@vueuse/core";
import TopBar from "../components/TopBar/index.vue";

const opened = ref(false);

const windowWidth = ref(0);

const breakpoints = useBreakpoints(breakpointsBootstrapV5);

const isMobile = breakpoints.smaller("md");

const isOpen = computed((): boolean => {
  return !isMobile.value || opened.value;
});

onMounted(() => {
  setWindowWidth();
  window.addEventListener("resize", setWindowWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", setWindowWidth);
});

const setWindowWidth = () => {
  windowWidth.value = window.innerWidth;
};

const menu = useMenu();
</script>

<style lang="scss">
.nav-fixed,
.side-fixed {
  position: fixed;
  left: 0;
  z-index: 25;
}
.nav-fixed {
  top: 0;
}

.side-fixed {
  top: 0;

  @include media-breakpoint-down(md) {
    top: 60px;
  }
}

.wrapper-mobile {
  width: 100% !important;
  margin-left: auto !important;
}
.wrapper {
  width: calc(100% - 250px);
  height: calc(100% - 50px);
  align-items: stretch;
  margin-left: 250px;
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 50px;
  #page-indicator {
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: $primary-color;
  }

  #page-title {
    font-weight: 700;
    line-height: 42px;
    letter-spacing: -0.02em;
    color: $primary-color;
  }

  @include media-breakpoint-down(md) {
    padding-top: 60px;
  }

  &.small {
    width: calc(100% - 70px);
    margin-left: 70px;
    transition: all 0.5s ease-in-out;
  }
  .content {
    height: calc(100% - 60px);
    overflow-y: auto;
  }
}
</style>
