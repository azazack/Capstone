<template lang="pug">
modal(v-if="isOpen" @close="isOpen=false")
  form(@submit.prevent='onSubmit')
    .row
      .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
        label.form-field
          input.form-control(v-model='amount', name='amount' placeholder="Amount" type='number', required)
          span.floated Amount
      .offset-sm-2.col-sm-8.col-md-8.mb-3
        label.form-field
          SingleSelect(@updateOption="loadUser" :options="options" title="Receiver" key-only v-model="receiver")
      .offset-sm-2.col-sm-8.col-md-8
        label.form-field
          input.form-control(v-model='date', name='date' placeholder="Date" type="date")
          span.floated Date
      .offset-sm-2.col-sm-8.col-md-8.mt-3
        Button.primary.mb-3.w-100(type='submit' :loading="loading") Add transaction
</template>
<script lang="ts" setup>
import modal from "../components/modal.vue"
import useAxios from "@/composables/useAxios";
import {defineEmits, ref} from "vue";
import SingleSelect from "./Dropdown/SingleSelect.vue";
import type {AxiosResponse} from "axios";
import {notify} from "@kyvg/vue3-notification";
import Button from "../components/Button/index.vue"

const {axios} = useAxios();

const amount = ref(0)

const receiver = ref(0)

const options = ref([])

const date = ref(new Date())

const loading = ref(false)


const props = defineProps({
  isOpen: {type: Boolean},
})

const emit = defineEmits(["added"])

const loadUser = (name: string) => {
  axios.get(`/api/v1/users`, {params: {name: name}}).then((res: AxiosResponse) => {
    options.value = res.data
  })
}

const onSubmit = () => {
  loading.value = true;
  axios
      .post("/api/v1/transaction", {
        transaction: {
          amount: amount.value,
          receiver: receiver.value,
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
};

</script>
