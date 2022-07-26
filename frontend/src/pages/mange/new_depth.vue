<template lang="pug">
form(@submit.prevent='onSubmit')
  .row
    .offset-sm-2.col-sm-8.col-md-8.mt-3.mb-3
      label.form-field
        input.form-control(v-model='amount', name='amount' placeholder="Amount" type='number', required)
        span.floated Amount
        //small.text-danger {{ errors.amount }}
    .offset-sm-2.col-sm-8.col-md-8
      label.form-field
        input.form-control(v-model='receiver', name='receiver' placeholder="Receiver" )
        span.floated Receiver
        //small.text-danger {{ errors.receiver }}
    .offset-sm-2.col-sm-8.col-md-8
      label.form-field
        input.form-control(v-model='date', name='receiver' placeholder="Receiver" type="date")
        span.floated Date
        //small.text-danger {{ errors.receiver }}
    .offset-sm-2.col-sm-8.col-md-8.mt-3
      Button.primary.mb-3.w-100(type='submit' :suffix-loading="loading") Sign In
</template>

<script lang="ts" setup>
</script>
