<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password'

const username = ref('')
const password = ref('')
const message = ref('')

const onSubmit = async () => {
    const body = JSON.stringify({username: username.value, password: password.value})
    const URL = "https://localhost:8443/api/register/"
    const response = await fetch(URL, {
        method: "POST",
        headers: {"Content-type": "application/json"},
        body
    });

    const data = await response.json();
    console.log(data)
    message.value = data.message 
    
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
            <Password v-model="password" details.password placeholder="Password" />
        </div>
        <button type="submit" label="Submit">Register</button>
    </form>
</template>