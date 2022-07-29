<template lang="pug">
.transaction(:class="isSender(transaction.sender.id)? 'sender' : 'receiver'")
  .left-side
    .receiver  Sent To : {{transaction.receiver.name}}
    .amount {{transaction.amount}} $
  .right-side
    .test Created: {{DateForm(transaction.created_at)}}
    .test Due To: {{DateForm(transaction.due_to)}}
    Options
      .menu-item(@click="emit('edit')") Edit
</template>
<script lang="ts" setup>
import {format} from "date-fns";
import {useAuth} from "../../store/auth";
import Options from "../options.vue"

const DateForm = (date: number): string => {
  return format(new Date(date), 'MM/dd/yyyy')
}
const auth = useAuth()

const isSender = (user_id:number):boolean => {
  return user_id == auth.user.id
}

const emit = defineEmits(["edit"]);

const props = defineProps({
  transaction: Object
})
</script>


<style lang="scss">
.transaction {
  background-color: white;
  display: flex;
  justify-content: space-between;
  border: 1px solid gray;
  margin: 10px 0;
  padding: 5px;
  border-radius: 10px;

  &.sender {
    border: 2px solid green;
  }
  &.receiver {
    border: 2px solid red;
  }
}
</style>
