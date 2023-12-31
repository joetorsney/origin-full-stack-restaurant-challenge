<template>
    <Message v-if="displayMustLoginMessage" severity="error">You must be logged in to checkout</Message>
    <div class="card">
        <ShoppingCart ref="cartRef" @checkout="onCheckoutCart"/>
    </div>
    <div class="card">
        <DataView :value="plates" :layout="layout">
            <template #header>
                <div class="flex justify-content-end">
                    <DataViewLayoutOptions v-model="layout" />
                </div>
            </template>

            <template #list="slotProps">
                <div class="col-12">
                    <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
                        <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
                        <div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                            <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                                <div class="text-2xl font-bold text-900">{{ slotProps.data.plate_name }}</div>
                            </div>
                            <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                                <span class="text-2xl font-semibold">{{ slotProps.data.price }} € </span>
                                <Button icon="pi pi-shopping-cart" rounded @click.prevent="addToCart(slotProps.data)"></Button>
                            </div>
                        </div>
                    </div>
                </div>
            </template>

            <template #grid="slotProps">
                <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2">
                    <div class="flex flex-column justify-content-between p-4 border-1 surface-border surface-card border-round h-full">
                        <div class="flex flex-column align-items-center gap-3 py-5">
                            <img class="w-9 shadow-2 border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
                            <div class="text-2xl font-bold">{{ slotProps.data.plate_name }}</div>
                        </div>
                        <div class="flex align-items-center justify-content-between">
                            <span class="text-2xl font-semibold">{{ slotProps.data.price }} €</span>
                            <Button icon="pi pi-shopping-cart" rounded @click.prevent="addToCart(slotProps.data)"></Button>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Button from 'primevue/button';
import Message from 'primevue/message';

import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional

import ShoppingCart from './ShoppingCart.vue';

const plates = ref();
const cartRef = ref(null);
const layout = ref('grid');
const displayMustLoginMessage = ref(false)

const access_token = localStorage.getItem('access_token')

const addToCart = (plate) => {
    cartRef.value.addToCart(plate)
}

onMounted(async () => {
    // fetch data from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;
});

const onCheckoutCart = async (cart) => {
    if (!access_token) {
        displayMustLoginMessage.value = true;
        return
    }

    const body = JSON.stringify({plates: cart})
    const URL = "https://localhost:8443/api/orders"
    const response = await fetch(URL, {
        method: "POST",
        headers: {
            Authorization: `Bearer ${access_token}`,
            "Content-type": "application/json"},
        body
    })

    const data = await response.json()

    console.log(data)
}

</script>
