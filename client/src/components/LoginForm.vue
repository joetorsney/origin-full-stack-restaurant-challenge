<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password'

const username = ref('')
const password = ref('')
const message = ref('')

const onSubmit = async () => {
    console.log(username, password)

    const URL = "https://localhost:8443/api/login"
    const response = await fetch(URL, {method: "POST"});
    const data = await response.json();

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
            <InputText placeholder="Username" />
        </div>
    
        <div class="p-inputgroup flex-1">
            <span class="p-inputgroup-addon">
                <i class="pi pi-key"></i>
            </span>
            <Password v-model="password" details.password placeholder="Password" :feedback="false" toggleMask/>
        </div>
        <button type="submit" label="Submit">Go</button>
    </form>
</template>