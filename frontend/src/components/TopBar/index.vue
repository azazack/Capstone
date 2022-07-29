<template lang="pug">
nav.top-bar
  .user {{auth.user.name}}
  a.logout(@click="logout") Logout
</template>

<script lang="ts" setup>
import {useAuth} from "../../store/auth";
import {useRouter} from "vue-router";
import useAxios from "../../composables/useAxios";

const auth = useAuth()
const router = useRouter();
const {axios} = useAxios();

const logout = () => {
  axios.delete('logout').then(() => {
  localStorage.clear()
  }).finally(() => {
    location.reload();
  })
}
</script>

<style lang="scss">
nav.top-bar {
  height: 50px;
  position: fixed;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background-color: white;
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
  border-bottom: 1px solid #64646F33;
}
</style>
