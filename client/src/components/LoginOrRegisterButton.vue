<script setup>
import Dialog from 'primevue/dialog'
import { ref } from 'vue';
import LoginForm from './LoginForm.vue';
import RegisterForm from './RegisterForm.vue';

const visible = ref(false);
const showLoginForm = ref(true)

const emit = defineEmits(['loginSuccess'])

const handleShowLoginForm = () => {
    showLoginForm.value = !showLoginForm.value
}

const handleLoginSuccess = () => {
    visible.value = false
    emit('loginSuccess')
}

</script>

<template>
    <button @click="visible = true">Log in</button>
    <Dialog v-model:visible="visible" modal>
        <LoginForm v-if="showLoginForm" @success="handleLoginSuccess"></LoginForm>
        <RegisterForm v-else @success="handleShowLoginForm"></RegisterForm>
        <button @click="handleShowLoginForm">
            {{showLoginForm ? "Don't have an account? Register here" : "Already have an account? Login here"}}
        </button>
    </Dialog>
</template>00