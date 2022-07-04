<template>
  <button @click="test">test</button>
  <button @click="testw">testw</button>
  <button @click="logout">logout</button>
</template>


<script setup lang="ts">
import useAxios from "./composables/useAxios";
import {useAuth} from "./store/auth";

const {axios} = useAxios()

const auth = useAuth()

const test =  () => {
  axios.post('http://127.0.0.1:8000/api/v1/login',{
    email:'d@d.com',
    password:'d'
  }).then(({data}) => {
    auth.setToken(data.jwt)
  })
}

const testw =  () => {
  axios.get('http://127.0.0.1:8000/api/v1/user')
}

const logout =  () => {
  axios.post('http://127.0.0.1:8000/api/v1/logout')
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
