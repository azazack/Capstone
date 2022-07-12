<template lang="pug">
.row.h-100.m-0
  .col-lg-12.d-flex.align-items-center
    .container
      h1.text-center.text-warning
      form(@submit.prevent='onSubmit')
        .row
          .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
            label.form-field
              input.form-control(v-model='email', name='email' placeholder="Email" type='email', required autocomplete="email")
              span.floated Email
              small.text-danger {{ errors.email }}
          .offset-sm-2.col-sm-8.col-md-8.mb-3
            label.form-field
              input.form-control(v-model='name', name='name' placeholder="Name"  required autocomplete="name")
              span.floated Name
              small.text-danger {{ errors.name }}
          .offset-sm-2.col-sm-8.col-md-8
            label.form-field
              input.form-control(v-model='password', name='password' placeholder="Password" type='password', required='' minlength='6', maxlength='64' autocomplete="current-password")
              span.floated Password
              small.text-danger {{ errors.password }}
          .offset-sm-2.col-sm-8.col-md-8.mt-3
            Button.primary.mb-3.w-100(type='submit' :suffix-loading="loading") Register


</template>

<script lang="ts" setup>
// import logo from "../assets/logo.svg";
import {useField, useForm} from "vee-validate";
import useAxios from "@/composables/useAxios";
import * as yup from "yup";
import {useAuth} from "@/store/auth";
import {ref} from "vue";
import {useRouter} from "vue-router";

const {handleSubmit, errors} = useForm({
  validationSchema: yup.object({
    email: yup.string().required().email(),
    password: yup.string().required(),
  }),
  validateOnMount: false,
});

const {value: email} = useField("email");
const {value: password} = useField("password");
const {value: name} = useField("name");

const loading = ref(false);

const {axios} = useAxios();

const auth = useAuth();

const router = useRouter();

const onSubmit = handleSubmit(() => {
  loading.value = true;
  axios
      .post("/api/v1/register", {
        user: {
          email: email.value,
          password: password.value,
          name: name.value
        },
      })
      // .then(({data}) => {
      //   auth.setToken(data.token);
      //   loadUser();
      // })
      .finally(() => {
        loading.value = false;
      });
});
</script>

