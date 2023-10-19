<script setup>
import { ref } from 'vue';
import TabMenu from 'primevue/tabmenu';
import Button from 'primevue/button';
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
    <div class="flex flex-row-reverse justify-content-between">
      <Button icon="pi pi-key" v-if="token" label="Log out" @click="handleLogout" />
      <LoginOrRegisterButton v-else @loginSuccess="updateToken"></LoginOrRegisterButton>
      <span class="flex align-items-center" v-if="token">Hello, {{ token }}</span>
    </div>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<style scoped>

</style>
