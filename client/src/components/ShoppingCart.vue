<script setup>
    import { ref } from "vue";
    import OrderList from 'primevue/orderlist';
    import Button from 'primevue/button';

    const emit = defineEmits(['checkout'])
    
    const cart = ref([])
    const cartTotal = ref(0)

    const disableCheckout = () => {
        return cart.value.length == 0
    }

    const addToCart = (addedPlate) => {
        // Update the quantity of the product in the cart, adding it to the cart
        // if it is not already present.
        cartTotal.value += addedPlate.price

        const cartPlateIndex = cart.value.findIndex(cartPlate => cartPlate.plate_id == addedPlate.plate_id)

        if (cartPlateIndex == -1) {
            cart.value.push({ ...addedPlate, quantity: 1 })
        } else {
            cart.value[cartPlateIndex].quantity += 1
        }

        updateDisableCheckout()
    }

    const removeFromCart = (removedPlate) => {
        cartTotal.value -= removedPlate.price
        const plateIndex = cart.value.findIndex(plate => plate.plate_id == removedPlate.plate_id)

        if (cart.value[plateIndex].quantity > 1) {
            cart.value[plateIndex].quantity -= 1
            return
        }

        cart.value.splice(plateIndex, 1)
    }

    const onCheckout = () => {
        emit('checkout', cart.value )
    }

    defineExpose({ addToCart })
</script>

<template>
    <OrderList v-model="cart" listStyle="height:auto" dataKey="i">
        <template #header>
            <div class="flex gap-5 justify-content-between">
                <div class="flex gap-5">
                    <span class="flex align-items-center">My Cart</span>
                    <span class="flex align-items-center">Total: {{ cartTotal }} €</span>
                </div>
                <Button label="Checkout" iconPos="left" icon="pi pi-shopping-cart" @click.prevent="onCheckout" :disabled="disableCheckout()"></Button> 
            </div>
        </template>

        <template #item="slotProps">
            <div class="flex flex-wrap p-2 align-items-center gap-3">
                <div class="flex-1 flex flex-column gap-2">
                    <span class="font-bold w-10rem">{{ slotProps.item.quantity }} x {{ slotProps.item.plate_name }}</span>
                </div>
                <span class="font-bold text-900">{{ slotProps.item.price * slotProps.item.quantity }} €</span>
                <Button icon="pi pi-minus" routnded @click="removeFromCart(slotProps.item)"></Button>
            </div>
        </template>
    </OrderList>
</template>