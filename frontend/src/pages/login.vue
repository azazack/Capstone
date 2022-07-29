<template lang="pug">
.row.h-100.m-0
  .col-lg-6.col-md-9.d-flex.align-items-center
    .container
      h1.text-center.text-warning
      form(@submit.prevent='onSubmit')
        .row
          .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
            label.form-field
              input.form-control(v-model='email', name='email' placeholder="Email" type='email', required autocomplete="email")
              span.floated Email
              small.text-danger {{ errors.email }}
          .offset-sm-2.col-sm-8.col-md-8
            label.form-field
              input.form-control(v-model='password', name='password' placeholder="Password" type='password', required='' minlength='6', maxlength='64' autocomplete="current-password")
              span.floated Password
              small.text-danger {{ errors.password }}
          .offset-sm-2.col-sm-8.col-md-8.mt-3
            Button.primary.mb-3.w-100(type='submit' :suffix-loading="loading") Sign In
  .col-lg-6.col-md-3.col-0.d-none.d-md-flex.login-page
    img(:src="login")
</template>

<script lang="ts" setup>
// import logo from "../assets/logo.svg";
import {useField, useForm} from "vee-validate";
import useAxios from "@/composables/useAxios";
import * as yup from "yup";
import {useAuth} from "@/store/auth";
import {ref} from "vue";
import {useRouter} from "vue-router";
import login from "@/assets/images/login.svg";

const {handleSubmit, errors} = useForm({
  validationSchema: yup.object({
    email: yup.string().required().email(),
    password: yup.string().required(),
  }),
  validateOnMount: false,
});

const {value: email} = useField("email");
const {value: password} = useField("password");

const loading = ref(false);

const {axios} = useAxios();

const auth = useAuth();

const router = useRouter();

const onSubmit = handleSubmit(() => {
  loading.value = true;
  axios
      .post("/api/v1/login", {
        user: {
          email: email.value,
          password: password.value,
        },
      })
      .then(({data}) => {
        auth.setToken(data.jwt);
        router.push("/dashboard");
      })
      .finally(() => {
        loading.value = false;
      });
});


</script>

<style lang="scss">
.login-page {
  //background: radial-gradient(
  //  ellipse at center,
  //  #5a93af 0%,
  //  $primary-color 100%
  //);
  //background-image: url("../assets/placeholder_cover.png");
  background-position: center;
  border-bottom-left-radius: 40px;
  color: $primary-color;
}
</style>
