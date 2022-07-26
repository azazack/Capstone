<template lang="pug">
input.form-control(v-model='value' :placeholder="title")
span.floated {{title}}
.options(v-if="showOptions &&  options.length" v-click-away="hideOptions")
  .option(@click="selectOption(option)" v-for="option in options") {{getValue(option)}}
</template>

<script lang="ts" setup>
import {ref, watch} from "vue"

const props = defineProps({
  options: Array,
  title: String,
  key: {type: String, default: 'id'},
  value: {type: String, default: 'name'},
  keyOnly: {type: Boolean, default: false}
})
const value = ref("")

const showOptions = ref(false)

const emit = defineEmits(["updateOption", "selectOption", "update:modelValue"]);

const getKey = (option: Record<string, string>) => {
  return option[props.key]
}
const getValue = (option: Record<string, string>) => {
  return option[props.value]
}

const hideOptions = () => {
  showOptions.value = false;
}

const selectOption = (option: Record<string, string>) => {
  value.value = option[props.value];
  emit("update:modelValue", props.keyOnly ? getKey(option) : option);
  if (props.keyOnly) {
    emit('selectOption', getKey(option))
  } else {
    emit('selectOption', option)
  }
  hideOptions()
}

watch(
    () => value.value,
    (val: string): void => {
      showOptions.value = true
      emit("updateOption", val);
    },
);
</script>

<style lang="scss">
.options {
  background: white;
  position: absolute;
  z-index: 999;
  width: 100%;
  height: fit-content;

  .option {
    padding: 5px 10px;
    border-bottom: gray;
    font-size: 15px;
  }
}
</style>
