<template lang="pug">
modal(v-if="isOpen" @close="isOpen=false")
  form(@submit.prevent='onSubmit')
    .row
      .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
        label.form-field
          input.form-control(v-model='amount', name='amount' placeholder="Amount" type='number', required)
          span.floated Amount
          //small.text-danger {{ errors.amount }}
      .offset-sm-2.col-sm-8.col-md-8
        label.form-field
          //input.form-control(v-model='name', name='receiver' placeholder="Receiver"  v-on:change="loadUser")
          //span.floated Receiver
          SingleSelect(@updateOption="loadUser" :options="options" title="Receiver" @selectOption="selectOption" key-only)
          //small.text-danger {{ errors.receiver }}
      .offset-sm-2.col-sm-8.col-md-8
        label.form-field
          input.form-control(v-model='date', name='date' placeholder="Date" type="date")
          span.floated Date
          //small.text-danger {{ errors.receiver }}
      .offset-sm-2.col-sm-8.col-md-8.mt-3
        Button.primary.mb-3.w-100(type='submit' :suffix-loading="loading") Add transaction
</template>
<script lang="ts" setup>
import modal from "../components/modal.vue"
import useAxios from "@/composables/useAxios";
import {ref} from "vue";
import SingleSelect from "./Dropdown/SingleSelect.vue";
import type {AxiosResponse} from "axios";

const {axios} = useAxios();

const amount = ref(0)

const receiver = ref(0)

const options = ref([])

const date = ref(new Date())

const selectOption = (user) => {
  console.log(user)
}

const props = defineProps({
  isOpen: {type: Boolean},
})

const test = (test: string) => {
  console.log(test)
}

const loadUser = (name: string) => {
  axios.get(`/api/v1/users`, {params: {name: name}}).then((res: AxiosResponse) => {
    options.value = res.data
  })
}

const onSubmit = () => {
  // loading.value = true;
  axios
      .post("/api/v1/transaction", {
        transaction: {
          amount: amount.value,
          receiver: receiver.value,
          due_to: date.value
        },
      })
  // .then(({data}) => {
  //   auth.setToken(data.jwt);
  //   router.push("/");
  // })
  // .finally(() => {
  //   loading.value = false;
  // });
};

</script>
