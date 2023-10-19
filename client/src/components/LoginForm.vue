<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password'
import Button from 'primevue/button';

const username = ref('')
const password = ref('')
const errors = ref([])

const emit = defineEmits(['success'])

const checkFormErrors = () => {
    errors.value = []
    
    if (username.value.length == 0) {
        errors.value.push("Username must not be empty")
    }

    if (password.value.length == 0) {
        errors.value.push("Password must not be empty")
    }
}

const onSubmit = async () => {
    checkFormErrors()
    if (errors.value.length > 0) return

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

    errors.value.push(data.detail)
}

</script>

<template>
    <p>{{ message }}</p>
    <form @submit.prevent="onSubmit">
        <div class="flex flex-column gap-2">
            <div v-for="error in errors">
                <span class="text-red-800">{{ error }}</span>
            </div>
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
            <Button type="submit" label="Login" />
        </div>
    </form>
</template>