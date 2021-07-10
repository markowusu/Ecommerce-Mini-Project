<template>
  <div class="home">
   <span>Home</span>
  <div v-if="latestproduct">
 <div class="column is-3" 
 v-for="product in latestproduct"
   v-bind:key="product.id"
   >
   <!-- <div class="box">
   <figure class="image mb-4">
   <img :src="product.thumbnail_image" alt="thumbnail image">
   </figure>


   <p> {{ product.name}}  |  <em class="success">Brand: {{product.brand}}</em></p>
   <p> Price: $<span v-if="product.price > product.old_price">{{ product.price}} </span> <span v-else>{{ product.old_price}}  </span>
    </p>
    
   </div>
   -->
    <ProductItemList :productItem="product" />
  

   <router-link v-bind:to="product.url" class="button is-dark mt-6">View Details</router-link>
   
  </div>
  
  
  </div>
  </div>

</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ProductItemList from '/src/components/Products/ProductItemList';

export default {
  name: 'Home',
  data() {
    return {
      latestproduct : []
    }
  },
  components: {
   ProductItemList,
  },
  mounted(){
    this.getProductList()

    document.title = 'Home | Confirm '
  },
  methods:{
    async getProductList(){
      await axios.get('api/v1/latest-product/')
      .then(response =>{
   
        this.latestproduct = response.data.results
        // console.log(this.latestproduct)
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
 }
</script>
