import Vue from 'vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueAwesomeSwiper from 'vue-awesome-swiper'

// import style (>= Swiper 6.x)
import 'swiper/swiper-bundle.min.css'

import UUID from "vue-uuid"

import axios from 'axios'

import App from './App.vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueAwesomeSwiper)

Vue.use(UUID)

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
