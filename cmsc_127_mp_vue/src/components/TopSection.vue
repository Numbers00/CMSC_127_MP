<template>
<section class='hero is-medium is-dark mb-6' id='top-section'>
  <div class='hero-body has-text-centered'>
    <p class='title mb-5' id='title'>
      <template v-if="$store.state.isAuthenticated">
        Welcome {{myDetails[0].username}} !!
      </template>
      <template v-else>
        Welcome to Synergy !!
      </template>
    </p>
    <p class='subtitle' v-for='content in subtitleContent' :key='content'>
      {{ viewType === content.type ? content.text : '' }}
    </p>
  </div>
</section>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'TopSection',
    props: {
        viewType: String,
        cardName: String
    },
    data () {
        return {
            subtitleContent: [
                {type: 'Home', text: 'This is the Home Page'},
                {type: 'CardView', text: 'You are Viewing: ' + this.cardName},
                {type: 'YourCards', text: 'You can Add, Delete, or Modify your Cards Here!'},
                {type: 'History', text: 'Below are all of your Available Previous Cards'}
            ],
            myDetails: {}
        }
    },
    mounted () {
      this.getMyDetails()

      document.title = 'Home | Synergy'
    },
    methods: {
      async getMyDetails () {
        this.$store.commit('setIsLoading', true)

        await axios
          .get('api/v1/users/')
          .then(response => {
              this.myDetails = response.data
          })
          .catch(error => {
              console.log(error)
          })

        this.$store.commit('setIsLoading', false)
      }
    }
}
</script>

<style>
#top-section {
  position: relative;
  top: 20px;
  height: 300px;
  border-radius: 10px;
}
#title {
  position: relative;
  bottom: 50px;
}
</style>