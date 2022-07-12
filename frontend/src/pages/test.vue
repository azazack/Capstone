<template lang="pug">
button(@click="test") test
</template>

<script lang="ts" setup>
import useAxios from "@/composables/useAxios";
import {useAuth} from "../store/auth";
import {onMounted} from "vue";
import isEmpty from "lodash/isEmpty"

const auth = useAuth()
const {axios} = useAxios();

onMounted(() => {
  console.log(isEmpty(auth.user))
  if (isEmpty(auth.user)) {
    loadUser()
  }
});

const loadUser = () => {
  axios.get("/api/v1/me").then(({data}) => {
     auth.setUser(data);
  });
};


const test = () => {
  axios.delete("/api/v1/logout");
  auth.logout();
  window.location.reload()
}
</script>
