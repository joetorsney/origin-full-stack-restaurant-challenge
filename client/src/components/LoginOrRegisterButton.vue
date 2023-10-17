<script setup>
import Dialog from 'primevue/dialog'
import { ref } from 'vue';
import LoginForm from './LoginForm.vue';
import RegisterForm from './RegisterForm.vue';

const visible = ref(false);
const showLoginForm = ref(false)

const handleShowLoginForm = () => {
    showLoginForm.value = !showLoginForm.value

}

</script>

<template>
    <button @click="visible = true">Register</button>
    <Dialog v-model:visible="visible" modal>
        <LoginForm v-if="showLoginForm"></LoginForm>
        <RegisterForm v-else></RegisterForm>
        <button @click="handleShowLoginForm">
            {{showLoginForm ? "Don't have an account? Register here" : "Already have an account? Login here"}}
        </button>
    </Dialog>
</template>00