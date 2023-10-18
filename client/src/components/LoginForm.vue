<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password'

const username = ref('')
const password = ref('')
const message = ref('')

const emit = defineEmits(['success'])

const onSubmit = async () => {
    const body = new URLSearchParams({
        username: username.value,
        password: password.value
    })
    
    const URL = "https://localhost:8443/api/login"
    const response = await fetch(URL, {
        method: "POST",
        headers: {"Content-type": "application/x-www-form-urlencoded"},
        body
    })

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem('access_token', data.access_token)
        localStorage.setItem('token_type', data.token_type)
        emit('success')
        return
    }

    message.value = data.detail
}

</script>

<template>
    <p>{{ message }}</p>
    <form @submit.prevent="onSubmit">
        <div class="p-inputgroup flex-1">
            <span class="p-inputgroup-addon">
                <i class="pi pi-user"></i>
            </span>
            <InputText v-model="username" placeholder="Username" />
        </div>
    
        <div class="p-inputgroup flex-1">
            <span class="p-inputgroup-addon">
                <i class="pi pi-key"></i>
            </span>
            <Password v-model="password" details.password placeholder="Password" :feedback="false" toggleMask/>
        </div>
        <button type="submit" label="Submit">Login</button>
    </form>
</template>