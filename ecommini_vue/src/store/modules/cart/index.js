// import axios from "axios";

// const state = { 
//     cart: {
//     item: [],
// }
// ,
// token:'',
// isAuthencated: false,
// isLoaded: false,
//  }


// const mutations = { 
//     InitializeStore(state){
//         if(localStorage.getItem('cart')){
//             state.cart = JSON.parse(localStorage.getItem('cart') )
//             // This actually serializes the JavaScript object
//         }
//         else{
//              localStorage.setItem('cart', JSON.stringify(state.cart))
//         }
//     },
//     addToCart (state , item){
//         const exist = state.cart.item.filter(i => i.product.id == item.product.id)

//         if(exist.length){
//             exist[0].quantity = parseInt(exist[0].quantity )+ parseInt(item.quantity)
//         }
//         else {
//             state.cart.item.push(item)
//         }

//         localStorage.setItem('cart', JSON.stringify(state.cart))


//     }
//  }

// const actions ={ 
//     get_cartList({ commit }){
//   axios.get('/api/v1/latest_cart').then((response) => {
//       commit('UPADTE_PRODUCT_LIST',response.data)
//     }).catch((error) => {
//            console.log(error)
//     })
// }
// }

// const getter = { 
//     // cartItems: state => state.cart.item
// }

// const cartModule = {
//     state,
//     mutations,
//     actions,
//     getter,

// }

// export default cartModule;