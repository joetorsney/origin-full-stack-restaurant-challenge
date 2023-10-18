<template>
    {{ user }}
</template>

<script setup>
import { ref, onMounted } from 'vue';

const user = ref(null);

onMounted(async () => {
    const token = localStorage.getItem('access_token')

    // fetch this user from server
    const URL = "https://localhost:8443/api/user/me"
    const response_orders = await fetch(URL, {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
    const data_orders = await response_orders.json();
    user.value = data_orders;
});

</script>