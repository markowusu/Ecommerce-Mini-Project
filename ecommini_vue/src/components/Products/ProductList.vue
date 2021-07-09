<template>
<div class="product-list">

<div
v-for="productItem in productItems"
:key="productItem.id" 
class = "product-list--item" >

<ProductItemList :productItem = "productItem" />
</div>

</div>


</template>

<script>
import {mapGetters} from 'vuex';
import ProductItemList from './ProductItemList';

export default {
    name: 'ProductList',
    mounted() {
        this.$store.dispatch("get_productList");
    },

    computed:{
        ...mapGetters([
            'productItems'
            ])
    },

    components: {
        ProductItemList,
    }


}
</script>

<style>

</style>