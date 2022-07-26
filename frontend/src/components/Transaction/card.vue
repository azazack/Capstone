<template lang="pug">
.transaction
  .left-side
    .receiver  Sent To : {{transaction.receiver.name}}
    .amount {{transaction.amount}} $
  .right-side
    .test {{DateForm(transaction.created_at)}}
</template>
<script lang="ts" setup>
import {format} from "date-fns";

const DateForm = (date: number): string => {
  return format(new Date(date), 'MM/dd/yyyy')
}

const props = defineProps({
  transaction: Object
})
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
