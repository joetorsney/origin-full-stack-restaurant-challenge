<script setup>
import Dialog from 'primevue/dialog'
import { ref } from 'vue';
import LoginForm from './LoginForm.vue';

const visible = ref(false);

</script>

<template>
    <button @click="visible = true">Register</button>
    <Dialog v-model:visible="visible" modal header="Login">
        <LoginForm></LoginForm>
    </Dialog>
</template>