<template lang="pug">
.container
  h1 Sent
  TransactionCard(v-for="transaction in transactions" :transaction="transaction")
  .text-center
    Pagination(:paginate="pagination" @page-changed="changePage")
</template>

<script lang="ts" setup>
// Imports
import useAxios from "../composables/useAxios";
import {onMounted} from "vue";
import {ref} from "vue"
import TransactionCard from "../components/Transaction/card.vue"
import Pagination from "../components/Pagination/index.vue"

// Data
const {axios} = useAxios();
const transactions = ref([])

onMounted(() => {
  loadTransaction()
});

const page = ref(1)

const pagination = ref({})

const changePage = (selectedPage:number) => {
  page.value = selectedPage
  loadTransaction()
}


const loadTransaction = () => {
  close()
  axios.get("/api/v1/own_transaction", {
    params: {
      type: "sent",
      page:page.value,
    }
  }).then(({data}) => {
    transactions.value = data.data
    pagination.value = data.meta
  })
}
</script>
