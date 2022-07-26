<template lang="pug">
.container
  //router-link(:to="{name:'new_depth'}")
  button.primary(@click="test") New Product Tag
  AddTransaction(:is-open="isOpen" @close="isOpen = false")
  .transaction(v-for="transaction in transactions")
    .left-side
      .receiver  Sent To : {{transaction.receiver.name}}
      .amount {{transaction.amount}} $
    .right-side
      .test {{DateForm(transaction.created_at)}}
</template>

<script lang="ts" setup>
import useAxios from "../composables/useAxios";
import {useAuth} from "../store/auth";
import {onMounted} from "vue";
import isEmpty from "lodash/isEmpty"
import {ref} from "vue"
import {format} from 'date-fns'
import AddTransaction from "../components/AddTransaction.vue";

const auth = useAuth()
const {axios} = useAxios();
const isOpen = ref(false)
const transactions = ref([])

onMounted(() => {
  loadTransaction()
  if (isEmpty(auth.user)) {
    loadUser()
  }
});

const DateForm = (date: number): string => {
  return format(new Date(date), 'MM/dd/yyyy')
}

const test = () => {
  console.log("test")
  isOpen.value = true
}

const loadUser = () => {
  axios.get("/api/v1/me").then(({data}) => {
    auth.setUser(data);
  });
};


// const test = () => {
//   axios.delete("/api/v1/logout");
//   auth.logout();
//   window.location.reload()
// }

const loadTransaction = () => {
  axios.get("/api/v1/own_transaction").then(({data}) => {
    transactions.value = data
  })
}
</script>


<style lang="scss">
.transaction {
  display: flex;
  justify-content: space-between;
  border: 1px solid gray;
  margin: 10px 0;
  padding: 5px;
  border-radius: 10px;
}
</style>
