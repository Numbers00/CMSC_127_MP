<template>
  <div id='wrapper'>
    <section class='section'>
    <nav class="navbar is-dark" id='top-nav'>
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Synergy</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item mr-2">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Search" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <template v-if="$store.state.isAuthenticated">
            <template v-if="countMarkedCards() !== 0">
              <template v-for="card in cards">
                <router-link
                  :to="'/cards/' + card.get_absolute_url + '/'"
                  class='navbar-item'
                  v-if="card.is_marked"
                  :key="card.id"
                >{{getFirstStr(card.name)}}</router-link>
              </template>
              <router-link to="/history" class="navbar-item">History</router-link>
              <router-link to="/your-cards" class="navbar-item">Your Cards</router-link>
            </template>
            <template v-else>
              <div class="navbar-item navbar-no-marked-cards-notice">
                <b>Mark up to 3 cards and navigate to them easily here!</b>
              </div>
              <router-link to="/history" class="navbar-item">History</router-link>
              <router-link to="/your-cards" class="navbar-item">Your Cards</router-link>
            </template>
          </template>
          <template v-else>
            <div class="navbar-item navbar-logged-out-notice">
              <b>You are logged out, log in to unlock other features</b>
            </div>
          </template>
        </div>

        <div class="navbar-end">
          <router-link to="/plans" class="navbar-item">Plans</router-link>
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/global" class="navbar-item">Global</router-link>
            <router-link to="/quotes" class="navbar-item">Quotes</router-link>
            <router-link to="/profile" class="navbar-item">Profile</router-link>
            <router-link to="/login" class="navbar-item"><p @click="logout()">Logout</p></router-link>
          </template>
          <template v-else>
            <router-link to="/quotes" class="navbar-item">Quotes</router-link>
            <router-link to="/login" class="navbar-item">Login</router-link>
            <router-link to="/signup" class="navbar-item">Signup</router-link>
          </template>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <router-view/>

    </section>

    <footer class="footer">
      <p class="has-text-centered">Hounds of Parerun, Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
  data () {
    return {
      showMobileMenu: false,
      cards: []
    }
  },
  beforeCreate () {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  created () {
    window.addEventListener(
      'resize',
      this.$store.commit('setWindowWidth')
    )
  },
  watch: {
    cards () {
      console.log(this.cards)
    }
  },
  mounted () {
    this.getCards()

    console.log(this.$store.state.isAuthenticated)
  },
  methods: {
    async getCards () {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/cards/view')
          .then(response => {
            console.log(response.data)
            this.cards = response.data
          })
          .catch(err => {
              console.log(err)
              
              toast({
                  message: 'Something went wrong. Please try again.',
                  type: 'is-danger',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
              })
          })

      this.$store.commit('setIsLoading', false)
    },
    logout () {
      axios.defaults.headers.common['Authorization'] = ''

      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')

      this.$store.commit('removeToken')
      this.$router.push('/')
    },
    countMarkedCards () {
      let counter = 0
      for (let card in this.cards) {
        if (this.cards[card].is_marked) counter += 1
      }
      console.log('counter ' + counter)
      return counter
    },
    getFirstStr (text) {
      return text.split(' ')[0]
    }
  },
  computed: {
    cardViews () {
      let cardViews = []
      for (let card in this.cards) {
        cardViews.push(this.cards[card].name)
      }

      return cardViews
    }
  }
}
</script>

<style>
.navbar {
  padding-top: 0;
  padding-bottom: 0;
  border-radius: 10px;
}
.navbar-logged-out-notice {
  height: 100%;
  background: #d9534f;
  color: white;
}
.navbar-no-marked-cards-notice {
  height: 100%;
  background: #5bc0de;
  color: white;
}
.navbar-item {
  height: 100%;
}
.navbar-item:hover {
  background: #eeeeee;
  text-decoration: none;
}
</style>

<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
