<template>
<div class="box column ">
<figure class="image">
        <img :src="search.thumbnail_image" alt="">
</figure>


<h3 class="is-size-6"> 
{{search.name}}</h3>
<h3 class="is-size-6">
    {{search.price}}
</h3>
</div>

    
</template>
<script>
export default {
 name: 'SearchTerm',
 props:{
     search: Object
 }

}
</script>