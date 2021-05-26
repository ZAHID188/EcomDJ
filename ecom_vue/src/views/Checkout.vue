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
                              <!-- REMEMBER THIS NEED TO HAVE AN INTERNET CONNECTION
                              THERE IS AN ERROR IN THE CART AND CHECKOUT WITHOUT INTERNET-->
                              <th>Product</th>
                              <th>Price</th>
                              <th>Quantity</th>
                              <th>Total</th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr v-for="item in cart.items"
                          v-bind:key="item.product.id"
                          >
                          <td>{{item.product.name}}</td>
                          <td>{{item.product.price}}</td>  
                          <td> {{item.quantity}}</td>
                          <td> {{ getItemTotal(item).toFixed(2)}}</td>
                              
                          </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td colspan="2">Total</td>
                                <td>{{cartTotalLength}} </td>
                                <td> {{ cartTotalPrice.toFixed(2)}}</td>
                            </tr>
                        </tfoot>

                          
                  </table>

                  <p v-else>You Don't have any products in your cart..</p> 

              <div class="column is-12 box">
                  <h2 class="subtitle">Shipping details</h2>
                  <p class="has-text-grey mb-4">* All fields required</p>
                  <div class="columns is-multiline">
                      <div class="column is-6">
                          <div class="field">
                              <label>First Name*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="first_name">
                              </div>
                          </div>

                          <div class="field">
                              <label>Last Name*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="last_name">
                              </div>
                          </div>

                          <div class="field">
                              <label>Email*</label>
                              <div class="control">
                                  <input type="email" class="input" v-model="email">
                              </div>
                          </div>
                          <div class="field">
                              <label>Phone*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="phone">
                              </div>
                          </div>
                      </div>
                        <div class="column is-6">
                          <div class="field">
                              <label>Address*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="address">
                              </div>
                          </div>

                          <div class="field">
                              <label>Zip Code*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="zipcode">
                              </div>
                          </div>
                          <div class="field">
                              <label>Place*</label>
                              <div class="control">
                                  <input type="text" class="input" v-model="place">
                              </div>
                           </div>
                        </div>
                  </div>
                  <div class="notification is-danger mt-4" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                        </div>
                       <hr>
                       <div id="card-element" class="mb-5"></div>
                       <template v-if="cartTotalLength">
                           <hr>
                           <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                       </template> 
                        
                      

              </div>
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

        if(this.cartTotalLength > 0){ //we check there is products in the cart
        //then we have new instance of stripe
            this.stripe=Stripe('pk_test_51Its92E4KCF5DGAErz4PmqiZQLLrxsaNIRPZsySjZmeKVJONAUGfGhyF3S69ZwDHko8fNJMWWCKWJq3wGSs59KrM00exnO2ozi')
            // new instance of element
            const elements=this.stripe.elements();
            //hide the postal code from the stupid form
            this.card= elements.create('card',{ hidePostalCode:true })    
            //then we mounted to the element-- look at the line 102
            this.card.mount('#card-element')
        }
        
    },
    methods:{
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm(){
            this.errors=[]
            if(this.first_name==='')
            {
                this.errors.push('The First name field is missing')
            }
            if(this.last_name==='')
            {
                this.errors.push('The last_name field is missing')
            }
            if(this.phone==='')
            {
                this.errors.push('The phone field is missing')
            }
            if(this.email==='')
            {
                this.errors.push('The email field is missing')
            }
            if(this.address==='')
            {
                this.errors.push('The address field is missing')
            }
            if(this.zipcode==='')
            {
                this.errors.push('The zipcode field is missing')
            }
            if(this.place==='')
            {
                this.errors.push('The place field is missing')
            }
  
             
            if(!this.errors.length){  // meaning if there is no error we can go into this
                this.$store.commit('setIsLoading',true)
                // create stripe token based on the card
                this.stripe.createToken(this.card).then(result=>{
                    if(result.error){
                        // if there is error we remove the loading
                        this.$store.commit('setIsLoading',false)
                        this.errors.push('something went wrong here in stripe')
                        console.log(result.error.message)
                    }
                    else{
                        // if there is no error we will continue this function
                        this.stripeTokenHandler(result.token)
                    }

                    
                })
            }
        },
        async stripeTokenHandler(token){
            const items=[]

            //then we loop through the all of the item
            //that's good for the backend
            for(let i=0; i<this.cart.items.length;i++){
                const item=this.cart.items[i]
                const obj={
                    product:item.product.id,
                    quantity:item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
                const data={
                 
                  'first_name':this.first_name,
                  'last_name': this.last_name,
                  'email':this.email,
                  'phone':this.phone,
                  'address':this.address,
                  'zipcode': this.zipcode,
                  'place':this.place,
                  'items':items,
                  'stripe_token':token.id

                    }
            await axios
                  .post('/api/v1/checkout/',data)
                  .then(response =>{
                     
                      this.$store.commit('clearCart')
                      this.$router.push('/cart/success')

                  })
                  .catch(error => {
                      this.errors.push('Something Wrong')
                      console.log(error)
                  })
                  this.$store.commit('setIsLoading',false)

        }
  
    },
   computed:{
       cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal) => {
                return acc += curVal.product.price * curVal.quantity
            },0)
        },
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.quantity
            },0)
        },
        
        
    }

}
</script>