<template lang="pug">
.base-button
  button.button.custom.align-items-center.justify-content-center(@click="onClick" :disabled="disabled || loading ")
    slot
    font-awesome-icon.icon-spin.me-1(:icon="faRotate" v-if="loading" :class="{ 'me-3': $slots.default }")
    font-awesome-icon(:icon="prefixIcon" v-else-if="prefixIcon" :class="{ 'me-3': $slots.default }")
</template>

<script lang="ts" setup>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faRotate} from "@fortawesome/free-solid-svg-icons/faRotate";
const props = defineProps({
  type: {
    type: String,
    default: () => "button",
  },
  disabled: { type: Boolean, default: () => false },
  loading: Boolean,
  prefixIcon: { type: Object, default: undefined },
});

const emit = defineEmits(["click"]);


function onClick(): void {
  emit("click");
}
</script>

<style lang="scss">
.base-button {
  position: relative;
  display: inline-block;
  border-radius: 5px;

  &:focus {
    outline: 1px solid #fff;
    outline-offset: -2px;
  }

  &:active {
    transform: scale(0.99);
  }

  button.button {
    width: 100%;
    display: inline-flex;
    padding: 8px 16px;
    min-height: 28px;
    font-size: 12px;
    font-weight: bold;
    line-height: 15px;
    border: none;
    border-radius: 5px;
    color: inherit;
    margin: 0;
    text-decoration: none;
    font-family: sans-serif;
    background-color: transparent;
    cursor: pointer;
    transition: background 250ms ease-in-out, transform 150ms ease;
    -webkit-appearance: none;
    -moz-appearance: none;

    .icon-spin {
      animation: spin;
      animation-duration: 500ms;
      animation-iteration-count: infinite;
      animation-timing-function: linear;
    }
  }

  &.big {
    button.button {
      padding: 0.7rem 1rem;
      font-size: 14px;
    }
  }

  &.small {
    button.button {
      padding: 7px 10px;
      font-size: 10px;
    }
  }

  &.x-small {
    button.button {
      padding: 0 10px;
      font-size: 10px;
    }
  }

  &.form-button {
    button.button {
      min-width: 150px;
    }
  }

  &.link-white {
    color: #fff;

    &:hover {
      color: #e3e3e3;
    }
  }

  &.dark-link {
    .button {
      font-weight: 100;
      font-size: 14px;
    }
  }

  &.dark {
    .button {
      background: darkgray;
      border: 1px solid darkgray;
      color: #fff;

      &:hover,
      &:focus {
        background: lighten(darkgray, 5);
      }
    }
  }

  &.outline-primary {
    .button {
      background-color: transparent;
      border: 1px solid $primary-color;
      color: $primary-color;

      &:hover,
      &:focus {
        background-color: $primary-color;
        color: white;
      }
    }
  }

  &.primary {
    .button {
      background: $primary-color;
      border: 1px solid $primary-color;
      color: #fff;

      &:hover,
      &:focus {
        background: #0053ba;
      }
    }
  }

  &.outline-dark {
    .button {
      background-color: transparent;
      border: 1px solid darkgray;
      color: darkgray;

      &:hover,
      &:focus {
        background-color: darkgray;
        color: white;
      }
    }
  }

  &.outline-white {
    .button {
      background-color: transparent;
      border: 1px solid $white;
      color: $white;

      &:hover,
      &:focus {
        border: 1px solid darkgray;
        background-color: $white;
        color: darkgray
      }
    }
  }
  &.danger {
    .button {
      background-color: #dc3545;
      border: 1px solid #dc3545;
      color: #fff;

      &:hover,
      &:focus {
        background: #fc1b2a;
      }
    }
  }

  .confirm-action {
    padding: 8px 16px;
    position: absolute;
    right: 0;
    top: 100%;
    border-radius: 4px;
    min-width: 250px;
    width: 120%;
    height: 100px;
    background-color: white;
    border: 1px solid #efefef;
    font-size: 14px;
    z-index: 99;

    .message-confirm {
      color: #0a1f43;
    }

    .cancel,
    .confirm {
      cursor: pointer;
    }

    .cancel {
      color: $primary-color;

      &:hover {
        color: darken($primary-color, 20);
      }
    }

    .confirm {
      color: $danger;

      &:hover {
        color: darken($danger, 20);
      }
    }
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
</style>
