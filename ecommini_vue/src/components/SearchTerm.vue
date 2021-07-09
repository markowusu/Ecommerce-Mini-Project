<template>
<div class="search-term ">
<div class="box column is-2 ">
<figure class="image">
        <img :src="search.thumbnail_image" alt="">
</figure>


<h3 class="is-size-4"> 
{{search.name}}</h3>
<h3 class="is-size-4">
    {{search.price}}
</h3>
</div>

<div>
</div>

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