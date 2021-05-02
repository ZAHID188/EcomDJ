<template>
    <div class="page-category">
        <div class="columns is-multiline">
          <div class="column is-12">
              <h2 class="is-size-2 has-text-centered">{{category.name}}</h2>

          </div>
        </div>


    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name:'Category',
    data() {
        return{
            category:{
                products:[]
            }
        }
        
    },
    mounted(){
        this.getCategory()
    },
    methods:
    {
        async getCategory(){
            const category_slug=this.$route.params.category_slug
            this.$store.commit('setIsLoading',true)

            axios
            .get(`/api/v1/products/${category_slug}/`)
            .then(response =>{
                this.category= response.data
                document.title=this.category.name +'|EcomDJ'
            })
            .catch(error => {
                     console.log(error)

                     toast({
                message:'Error .Try again',
                type:'is-success',
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right'
            })
                 })
            this.$store.commit('setIsLoading',false)

        }

    }
}
</script>
