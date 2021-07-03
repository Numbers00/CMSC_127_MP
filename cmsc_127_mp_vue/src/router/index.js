import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import store from '../store'

import {toast} from 'bulma-toast'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/Signup.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/plans',
    name: 'Plans',
    component: () => import('../views/Plans.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
    props: true,
    meta: {requireLogin: true}
  },
  {
    path: '/:user_slug/:card_slug/',
    name: 'CardView',
    component: () => import('../views/CardView.vue'),
    props: true,
    meta: {requireLogin: true}
  },
  {
    path: '/quotes',
    name: 'Quotes',
    component: () => import('../views/Quotes.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/history/:user_slug/:card_slug/',
    name: 'History',
    component: () => import('../views/History.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/your-cards',
    name: 'YourCards',
    component: () => import('../views/YourCards.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/global',
    name: 'Global',
    component: () => import('../views/Global.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue'),
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.length === 0) {
    next({path: '/'})
    toast({
      message: "The previous url does not exist, you have been redirected to the Homepage",
      type: 'is-danger',
      dismissible: true,
      pauseOnHover: true,
      duration: 3000,
      position: 'bottom-right',
    })
  }
  else {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
      next({path: '/login', query: {to: to.path}})
    } else {
      next()
    }
  }
})

export default router
