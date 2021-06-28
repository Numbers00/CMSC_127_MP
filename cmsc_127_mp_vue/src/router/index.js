import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import store from '../store'

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
    props: true
  },
  {
    path: '/:user_slug/:card_slug/',
    name: 'CardView',
    component: () => import('../views/CardView.vue'),
    props: true
  },
  {
    path: '/quotes',
    name: 'Quotes',
    component: () => import('../views/Quotes.vue')
  },
  {
    path: '/history',
    name: 'History',
    component: () => import('../views/History.vue')
  },
  {
    path: '/your-cards',
    name: 'YourCards',
    component: () => import('../views/YourCards.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: 'Login', query: {to: to.path}})
  } else {
    next()
  }
})

export default router
