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
        Cart
      </router-link>
      </div>
      </div>
    
      
    </div>

   
  </div>
</nav>

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
export default {
  data() {
    return {
      showmobileMenu: false,
    }
  },
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>

