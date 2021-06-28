import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    token: '',
    isLoading: false,
    windowWidth: window.innerWidth
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    setWindowWidth(state) {
      state.windowWidth = window.innerWidth;
    }
  },
  actions: {
  },
  modules: {
  }
})
