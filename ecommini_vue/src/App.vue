<template>
    <div id="wrapper">

  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://bulma.io">
      <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="showmobileMenu = !showmobileMenu">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu" v-bind:class="{'is-active': showmobileMenu}">
  <div class="navbar-start">
  <div class="navbar-item ">
    <form method="get"  action="/search">
  <div class="field has-addons">
  <div class="control">
  <input type="text" class="input"  name="query" placeholder="search based on keywords">
  </div>
  <div class="control">
  <button class="is-success button">
  <span class="icon">
  <i class="fas fa-search">
  </i>
  </span>
  </button>
  </div>
  </div>

    </form>
  </div>
  
  </div>
    <div class="navbar-end">
    
    <router-link  to="/" class=" navbar-item is-light">
        winter
      </router-link>
      <router-link  to="/" class="navbar-item ml-4 is-light">
        summer
      </router-link>
      
      <div class="navbar-item">
      <div class="buttons">
      <router-link  to="/" class="button is-light">
        Login 
      </router-link>
      <router-link  to="/" class="button is-success">
        Cart ({{cartTotalLength}})
      </router-link>
      </div>
      </div>
    
      
    </div>

   
  </div>
</nav>

<div class="is-loading-bar has-text-centred" v-bind:class="{'is-loading': this.$store.state.isLoaded}">
<div class="dual-ring">
</div>

</div>

  <section class="section">
  <router-view/>
  </section>

  <footer class="footer">
  <span>
  Copyright@ 2020
  </span>
  </footer>

    </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  data() {
    return {
      showmobileMenu: false,
      cart:{
        item:[]
      },
      
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')
  },

  mounted() { 
      this.cart = this.$store.state.cart
      
  },

  computed:{        
      cartTotalLength(){
        
        let totalLength = 0;

        for ( let i = 0; i < this.cart.item.length; i++){
          totalLength += this.cart.item[i].quantity 
          console.log(totalLength)
        }
        
        return totalLength;
      },

      
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.dual-ring{
  display: inline-block;
  width: 80px;
  height:  64px;
}

.dual-ring:after{
  content:"";
  display: block;
  height:64px;
  width:64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation:  dual-ring 1.2s linear infinite;
}
@keyframes dual-ring  {
  0% {
    transform: rotate(0deg);
    }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar{
    height: 0;
    overflow: hidden;

    -webkit-transition: all 0.4s;
    transition: all 0.4s;

    &.is-loading {
      height: 80px;
    }

  }
  

</style>

