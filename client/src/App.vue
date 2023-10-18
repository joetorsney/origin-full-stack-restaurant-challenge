<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue';
import LoginOrRegisterButton from './components/LoginOrRegisterButton.vue';

const items = ref([
  {label: 'Menu', to: '/'},
  {label: 'Orders', to: '/orders'},
  {label: 'User', to: '/user'}
]);

const token = ref(localStorage.getItem('access_token'))

const updateToken = () => {
  token.value = localStorage.getItem('access_token')
}

const handleLogout = () => {
  localStorage.clear()
  updateToken()
}

</script>

<template>
  <div class="top-0">
    <p v-if="token">Welcome, {{ token }}</p>
    <button v-if="token" @click="handleLogout">Log out</button>
    <LoginOrRegisterButton v-else @loginSuccess="updateToken"></LoginOrRegisterButton>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<style scoped>

</style>
