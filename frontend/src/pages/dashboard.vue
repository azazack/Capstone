<template lang="pug">
.container.dashboard
  AddTransaction(:is-open="isOpen" @close="close" @added="loadTransaction" :transaction="selectedTransaction")
  h1 Transactions
  .d-flex.justify-content-between
    Button.primary(@click="AddNewTransaction") New Transaction
    .d-flex
      p  Sent
        span.type.sender-type.me-3.ms-2
      p Received
        span.type.receiver-type.ms-2
  TransactionCard(v-for="transaction in transactions" :transaction="transaction" @edit="openEdit(transaction)" @paid="markAsPaid(transaction.id)" editable)
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
import {notify} from "@kyvg/vue3-notification";
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

const selectedTransaction = ref({})

const AddNewTransaction = () => {
  selectedTransaction.value = {}
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

const openEdit = (transaction:Record<string, string>) => {
  selectedTransaction.value = transaction
  isOpen.value = true
}

const loadTransaction = () => {
  close()
  axios.get("/api/v1/own_transaction").then(({data}) => {
    transactions.value = data
  })
}

const markAsPaid = (id:string) => {
  axios.put(`/api/v1/transactions/${id}/mark_as_paid`).then(() => {
    notify({
      title: "Success",
      text: "Transaction paid Successfully",
      type: "success"
    });
    loadTransaction()
  }).catch(() => {
    notify({
      title: "Error",
      type: "error"
    });
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
