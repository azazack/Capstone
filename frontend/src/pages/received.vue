<template lang="pug">
.container
  h1 Received
  TransactionCard(v-for="transaction in transactions" :transaction="transaction")
</template>

<script lang="ts" setup>
// Imports
import useAxios from "../composables/useAxios";
import {onMounted} from "vue";
import {ref} from "vue"
import TransactionCard from "../components/Transaction/card.vue"
// Data
const {axios} = useAxios();
const transactions = ref([])

onMounted(() => {
  loadTransaction()
});


const loadTransaction = () => {
  close()
  axios.get("/api/v1/own_transaction", {
    params: {
      type: "received"
    }
  }).then(({data}) => {
    transactions.value = data
  })
}
</script>
