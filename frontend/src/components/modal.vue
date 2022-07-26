<template lang="pug">
transition(name='modal')
  .modal-mask
    .modal-wrapper
      .modal-container
        .modal-body.pt-5(v-click-away="close")
          slot
</template>

<script lang="ts" setup>
const emit = defineEmits(["close"]);
const close = (): void => {
  emit("close");
};
</script>

<style lang="scss">
.modal-container {
  --color-background: white;
  max-width: 800px;
  width: 100%;
  margin: 0 auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  height: fit-content;
  //overflow-y: scroll;
}

.modal-enter-active .modal-container,
.modal-leave-active .modal-container {
  transform: scale(1.1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;

  .modal-body {
    background: white;
    max-height: 100vh;
    overflow: inherit;
    overflow-y: auto;
    padding: 1rem;
    position: relative;

    .title {
      color: $primary-color;
      font-size: 20px;
      font-weight: bold;
      line-height: 28px;
      text-align: center;
      margin-bottom: 32px;
      text-transform: capitalize;
    }

    label {
      font-size: 12px;
      font-weight: bold;
      letter-spacing: 0;
    }

    abbr {
      color: #f03d3d;
      text-decoration: none;
    }

    @at-root #{&}__close-icon {
      z-index: 1;
      position: absolute;
      height: 30px;
      width: 30px;
      top: 21px;
      right: 18px;
      &:hover {
        cursor: pointer;
      }

      @at-root #{&}--default-hidden {
        display: none;
      }
    }
    .close-icon {
      position: absolute;
      right: 22px;
      top: 20px;
      font-size: 26px;
      cursor: pointer;
    }
  }

  &.show-close-icon {
    .modal-body__close-icon--default-hidden {
      display: block !important;
    }
  }

  &.big {
    .modal-container {
      max-width: 1140px;
    }
  }

  &.small {
    .modal-container {
      max-width: 550px;
    }
  }

  &.out-box {
    .modal-body {
      overflow-y: inherit !important;
    }
  }

  &.padding-less {
    .modal-body {
      padding: 0 !important;
    }
  }

  &.fit-content {
    .modal-body,
    .modal-container {
      width: fit-content;
    }

    .modal-body {
      padding: 0 !important;
    }
  }
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>
