<template>
    
<div class="page-checkout">
     <div class="columns is-multiline">
         <div class="column is-12">
             <h1 class="title">Checkout</h1>
         </div>

             <div class="column is-12 box">

                  <table class="table is-fullwidth" v-if="cartTotalLength">
                      <thead>
                          <tr>
                              <th>Product</th>
                              <th>Price</th>
                              <th>Quantity</th>
                              <th>Total</th>
                          </tr>
                      </thead>
                      <tbody>
                          
                      </tbody>
                  </table>

                  <p v-else>You Don't have any products in your cart..</p> 
            </div>


     </div>
</div>
</template>
<script>

import axios from 'axios'
export default {
    name:'Checkout',
    data(){
        return{
            cart:{
                items:[]
            },
            stripe:{},
            card:{},
            first_name:'',
            last_name:'',
            email:'',
            phone:'',
            address:'',
            zipcode:'',
            place:'',
            errors:[],
        }
    },
    mounted(){
        document.title= 'Checkout || Ecomdj'
        this.cart=this.$store.state.cart
    },
    methods:{
        getItemTotal(item){
            return item.quantity * item.product.price
        }

    },
   computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc +=    curVal.product.price * curVal.quantity
            },0)
        },
        
    }

}
</script>