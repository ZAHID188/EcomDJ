<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Login</h1>

                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Username:</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username"><!-- v-model means vue model that refers to the data(){} in the scripts-->
                    </div>
                    </div>

                    <div class="field">
                        <label>Password:</label>
                      <div class="control">
                         <input type="password" class="input" v-model="password"><!-- v-model means vue model that refers to the data(){} in the scripts-->
                       </div>
                    </div>

                    

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                    </div>

                    
                        <div class="field">
                         <div class="control">
                          <button class="button is-dark">Login</button>
                         </div>
                      </div>

                      <hr>
                      or <router-link to="/log-in">click here</router-link> to SignUp!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name:'LogIn',
    data() {

    return{


        username:'',
            password:'',
            password2:'',
            errors:[]

 }
        
    },
    mounted(){
        document.title='Login || EcomDJ'

    },
}
</script>