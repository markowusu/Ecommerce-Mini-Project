import axios from "axios";

const state= { productList : [] };
const mutations = { UPDATE_PRODUCT_LIST(state, payload){
    state.productList = payload;
}
 };
const actions ={ get_productList({commit}){
  axios.get('/api/v1/latest_product').then((response) => {
      commit('UPADTE_PRODUCT_LIST',response.data);
    }).catch((error) => {
           console.log(error);
    })
}
};

const getter={ 
    productItems: state => state.productList
};

const productModule = {
    state,
    mutations,
    actions,
    getter,

}

export default productModule;