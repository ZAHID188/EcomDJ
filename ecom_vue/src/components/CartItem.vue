<template>
  <tr>
    <td>

       <!--MAJOR BUG , I WAS STUCK WITH THIS LINE FOR 2 DAYS-->
      <router-link to="item.product.get_absolute_url">{{ item.product.name}}</router-link>
      <!--<router-link:to = "item.product.get_absolute_url">{{item.product.name}}</router-link> -->
    </td>
    <td>{{ item.product.price }} Tk</td>
    <td>
      {{ item.quantity }}
      <a class="is-size-2" @click="decrementQuantity(item)"> -</a>
      <a class="is-size-2" @click="incrementQuantity(item)">+</a>
    </td>
    <td>{{ getItemTotal(item).toFixed(2) }} Tk</td>
    <td><button class="delete" @click="removeFromCart(item)"></button></td>
  </tr>
</template>
<script>
import axios from 'axios'
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }
      this.updateCart();
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>