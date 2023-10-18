<script setup>
    import { ref, watch } from "vue";

    const emit = defineEmits(['checkout'])
    
    const cart = ref([])
    const cartTotal = ref(0)
    const disableCheckout = ref(false)

    // TODO prevent user from checking out if their cart is empty
    watch(cart, (newCart) => {console.log(newCart); disableCheckout.value = newCart.length < 1}, {deep: true})

    const addToCart = (addedPlate) => {
        // Update the quantity of the product in the cart, adding it to the cart
        // if it is not already present.
        cartTotal.value += addedPlate.price

        const cartPlateIndex = cart.value.findIndex(cartPlate => cartPlate.plate_id == addedPlate.plate_id)

        if (cartPlateIndex == -1) {
            cart.value.push({ ...addedPlate, quantity: 1 })
            return
        }

        cart.value[cartPlateIndex].quantity += 1
    }

    const removeFromCart = (removedPlate, plateIndex) => {
        cartTotal.value -= removedPlate.price

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
    <p>Your cart {{ disableCheckout }}</p>
    <div v-for="plate, plateIndex in cart">
        <span>{{ plate.plate_name }} x{{ plate.quantity }}</span>
        <span>{{ plate.price * plate.quantity }} €</span>
        <button @click="removeFromCart(plate, plateIndex)" :disabled="disableCheckout">-</button>
    </div>
    <p>Total: {{ cartTotal }} €</p>
    <button @click.prevent="onCheckout">Checkout</button>
</template>