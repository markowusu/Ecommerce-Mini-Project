<template>
    <div class="page-search columns">

    <div >

    <h2>Search:{{query}}</h2>
    </div>

<div
 v-for="product in products"
    v-bind:key="product.id"
   
>

  <SearchTerm
    v-bind:search="product"
   
     />

</div>
  
</div>
    
</template>
<script>
import axios from 'axios'
import  SearchTerm from '@/components/SearchTerm.vue'
export default {
    name: 'Search', 
    components: {
        SearchTerm
    },
    data() {
        return {
            products:[],
            query:''
        }
    },
    mounted() {
        document.title = 'Search | '

        let uri = window.location.search.substring(1)
        let param = new URLSearchParams(uri)

        if (param.get('query')){
            this.query = param.get('query')
            this.getSearch()
            
        }
    },
    methods:{
 async getSearch(){
            await axios.post('/api/v1/product/search/' , {'query': this.query})
            .then( response =>{
                this.products = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        }
    }
        
}
</script>

