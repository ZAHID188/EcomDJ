<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

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

                    <div class="field">
                        <label>Repeat Password:</label>
                      <div class="control">
                         <input type="password" class="input" v-model="password2"><!-- v-model means vue model that refers to the data(){} in the scripts-->
                       </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                    </div>

                    
                        <div class="field">
                         <div class="control">
                          <button class="button is-dark">Sign up</button>
                         </div>
                      </div>

                      <hr>
                      or <router-link to="/log-in">click here</router-link> to Log in!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name:'SignUp',
    data() {
        return{
            username:'',
            password:'',
            password2:'',
            errors:[]
        }
        
    },
    methods:{
        submitForm(){
            this.errors=[]
            if(this.username === ''){
                this.errors.push('The username is missing')
            }

        }
    }
}
</script>