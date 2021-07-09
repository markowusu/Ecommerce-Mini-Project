import { createStore } from 'vuex';
// import product from './modules/product';
// import cart from './modules/cart';

export default createStore({
  // modules:{ 
  // product,
  // cart
// }

state :{ 
  cart: {
    item:[]
  },

token:'',
isAuthencated: false,
isLoaded: false,
}
,
mutations :{ 
  initializeStore(state){
      if(localStorage.getItem('cart')){
          state.cart = JSON.parse(localStorage.getItem('cart') )
          // This actually serializes the JavaScript object
      }
      else{
           localStorage.setItem('cart', JSON.stringify(state.cart))
      }
  },

  addToCart (state , item){
      const exist = state.cart.item.filter( element => element.product.id === item.product.id)

      if(exist.length){
          exist[0].quantity = parseInt(exist[0].quantity) + parseInt(item.quantity)
      }
      else {
          state.cart.item.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))


  },

  stateIsLoading(state, status){
    state.isLoaded = status
  }

},

actions:{},

modules:{}

});
