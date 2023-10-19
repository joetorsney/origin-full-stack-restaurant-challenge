<script setup>
import Dialog from 'primevue/dialog'
import { ref } from 'vue';
import LoginForm from './LoginForm.vue';
import RegisterForm from './RegisterForm.vue';
import Button from 'primevue/button';

const visible = ref(false);
const showLoginForm = ref(true)

const emit = defineEmits(['loginSuccess'])

const getSwitchFormButtonLabel = () => {
    return showLoginForm.value 
        ? "Don't have an account? Register here" 
        : "Already have an account? Login here"
}

const getModalHeader = () => {
    return showLoginForm.value
        ? "Login"
        : "Register"
}

const handleShowLoginForm = () => {
    showLoginForm.value = !showLoginForm.value
}

const handleLoginSuccess = () => {
    visible.value = false
    emit('loginSuccess')
}

</script>

<template>
    <Button label="Log in" icon="pi pi-key" @click="visible = true" />
    <Dialog v-model:visible="visible" :header="getModalHeader()" modal>
        <LoginForm v-if="showLoginForm" @success="handleLoginSuccess"></LoginForm>
        <RegisterForm v-else @success="handleShowLoginForm"></RegisterForm>
        <Button class="bg-primary-reverse" :label="getSwitchFormButtonLabel()" @click="handleShowLoginForm" link />
    </Dialog>
</template>00