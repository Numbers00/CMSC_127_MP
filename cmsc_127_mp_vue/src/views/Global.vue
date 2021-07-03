<template>
<div class='wrapper'>
Global
</div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
  name: 'Global',
  data () {
    return {
      otherUsers: []
    }
  },
  mounted () {
    this.getOtherUsers()
    
    document.title = 'Global | Synergy'
  },
  methods: {
    async getOtherUsers () {
      this.$store.commit('setIsLoading', true)

      await axios({
        method: 'get',
        url: '/api/v1/users/',
        auth: {
          username: 'Pupumaru00',
          password: 'Parerun806!'
        }
        })
        .then(response => {
          console.log(response.data)
          this.otherUsers = response.data
        })
        .catch(err => {
            console.log(err)
            
            toast({
                message: 'Something went wrong while getting your active cards. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        })

      this.$store.commit('setIsLoading', false)
    },
  }
}
</script>