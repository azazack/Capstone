<template lang="pug">
.container.dashboard
  AddTransaction(:is-open="isOpen" @close="close" @added="loadTransaction")
  h1 Transactions
  .d-flex.justify-content-between
    Button.primary(@click="AddNewTransaction") New Transaction
    .d-flex
      p  Sent
        span.type.sender-type.me-3.ms-2
      p Received
        span.type.receiver-type.ms-2
  TransactionCard(v-for="transaction in transactions" :transaction="transaction" @edit="isOpen = true")
</template>

<script lang="ts" setup>
// Imports
import useAxios from "../composables/useAxios";
import {useAuth} from "../store/auth";
import {onMounted} from "vue";
import isEmpty from "lodash/isEmpty"
import {ref} from "vue"
import AddTransaction from "../components/AddTransaction.vue";
import Button from "../components/Button/index.vue"
import TransactionCard from "../components/Transaction/card.vue"
// Data
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

const AddNewTransaction = () => {
  isOpen.value = true
}

const loadUser = () => {
  axios.get("/api/v1/me").then(({data}) => {
    auth.setUser(data);
  });
};

const close = () => {
  isOpen.value = false
}

const loadTransaction = () => {
  close()
  axios.get("/api/v1/own_transaction").then(({data}) => {
    transactions.value = data
  })
}
</script>

<style lang="scss">
.dashboard{
  .type {
    padding: 4px 10px;
    color: white;
    border-radius: 5px;
    &.sender-type {
      background-color: green;
    }
    &.receiver-type {
      background-color: red;
    }
  }
}
</style>
