<template lang="pug">
Modal(v-if="isOpen" @close="isOpen=false")
  form(@submit.prevent='onSubmit')
    .row
      .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
        label.form-field
          input.form-control(v-model='amount', name='amount' placeholder="Amount" type='number', required)
          span.floated Amount
      .offset-sm-2.col-sm-8.col-md-8.mb-3(v-if="!isEdit")
        label.form-field
          SingleSelect(@updateOption="loadUser" :options="options" title="Receiver" v-model="receiver" key-only )
      .offset-sm-2.col-sm-8.col-md-8
        label.form-field
          input.form-control(v-model='date', name='date' placeholder="Date" type="date" :min="todayDate()")
          span.floated Date
      .offset-sm-2.col-sm-8.col-md-8.mt-3
        Button.primary.mb-3.w-100(type='submit' :loading="loading") {{isEdit ? 'Edit':'Add'}} transaction
</template>
<script lang="ts" setup>
import Modal from "../components/modal.vue"
import useAxios from "@/composables/useAxios";
import {ref, computed,watch} from "vue";
import SingleSelect from "./Dropdown/SingleSelect.vue";
import type {AxiosResponse} from "axios";
import {notify} from "@kyvg/vue3-notification";
import Button from "../components/Button/index.vue"
import isEmpty from "lodash/isEmpty"
import {format} from "date-fns";

const {axios} = useAxios();

const amount = ref(0)

const receiver = ref(0)

const options = ref([])

const date = ref(new Date())

const loading = ref(false)


const props = defineProps({
  isOpen: {type: Boolean},
  transaction: {
    type: Object,
    default: () => ({ amount: 0, receiver: 0,date:new Date() }),
  },})

const emit = defineEmits(["added"])

const loadUser = (name: string) => {
  axios.get(`/api/v1/users`, {params: {name: name}}).then((res: AxiosResponse) => {
    options.value = res.data
  })
}

const isEdit = computed(() => {
  return !isEmpty(props.transaction.id);
});

const todayDate = () => {
  return format(new Date(), 'yyyy-mm-dd')
}


const onSubmit = () => {
  loading.value = true;
  if(!isEdit.value){
  axios
      .post("/api/v1/transactions", {
        transaction: {
          amount: amount.value,
          due_to: date.value
        },
      })
      .then(() => {
        notify({
          title: "Success",
          text: "Transaction Added Successfully",
          type: "success"
        });
        emit('added')
      }).catch(() => {
    notify({
      title: "Error",
      text: "Error While Adding Transaction",
      type: "error"
    });
  })
  .finally(() => {
    loading.value = false;
  });
  } else {
    axios.put(`/api/v1/transactions/${props.transaction.id}`, {
      transaction: {
        amount: amount.value,
        due_to: date.value,
        receiver:props.transaction?.receiver.id
      },
    })      .then(() => {
      notify({
        title: "Success",
        text: "Transaction Edited Successfully",
        type: "success"
      });
      emit('added')
    }).catch(() => {
      notify({
        title: "Error",
        text: "Error While Editing Transaction",
        type: "error"
      });
    })
        .finally(() => {
          loading.value = false;
        });
  }

};

watch(
    () => props.transaction,
    () => {
      amount.value = props.transaction.amount;
      date.value = props.transaction?.due_to;
    },
    { immediate: true, deep: true }
);
</script>
