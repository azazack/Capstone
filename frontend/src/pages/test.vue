<template lang="pug">
button(@click="test") test
</template>

<script lang="ts" setup>
import useAxios from "@/composables/useAxios";

const {axios} = useAxios();

const test = () => {
  axios.get("/api/v1/me");
}
</script>
