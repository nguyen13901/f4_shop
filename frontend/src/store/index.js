import { createStore } from 'vuex'

export default createStore({
  strict: true,
  state: {
    current_product: {},
    isViewProduct: false,
  },
  getters: {
    getCurrentProduct(state) {
      return state.current_product;
    }
  },
  mutations: {
    viewProduct(state, product) {
      state.current_product = product;
      state.isViewProduct = true;
    },
    cancelViewProduct(state) {
      state.isViewProduct = false;
    }
  },
  actions: {
    viewProduct(context, product) {
      setTimeout(() => {
        context.commit("viewProduct", product);
    }, 100);
    },
    cancelViewProduct(context) {
      setTimeout(() => {
        context.commit("cancelViewProduct");
    }, 100);
    }
  }
})