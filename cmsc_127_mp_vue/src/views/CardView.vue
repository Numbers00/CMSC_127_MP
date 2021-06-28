<template>
<div class="wrapper">
  <div class="twin-board-columns">
    <section class="boards-container">
      <template v-for="(board, index) in card.boards">
        <BoardBox
          v-if="index % 2 !== 0"
          :key="index"
          :board="board"
          :tasks="board.tasks"
        />
      </template>
    </section>
    <section class="boards-container">
      <template v-for="(board, index) in card.boards">
        <BoardBox
          v-if="index % 2 === 0"
          :key="index"
          :board="board"
          :tasks="board.tasks"
        />
      </template>
    </section>
  </div>
</div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

import BoardBox from '@/components/BoardBox.vue'

export default {
  name: 'CardView',
  data () {
    return {
      card: {}
    }
  },
  components: {
    BoardBox
  },
  mounted () {
    this.getChosenCard()

    document.title = 'Card View | Synergy'
  },
  watch: {
    $route(to, from) {
        to.name === 'CardView' ? this.getChosenCard() : ''
    },
    card () {
      console.log(this.card)
    }
  },
  methods: {
    async getChosenCard () {
      this.$store.commit('setIsLoading', true)

      console.log(this.$route.params.user_slug)
      console.log(this.$route.params.card_slug)

      let user_slug = this.$route.params.user_slug
      let card_slug = this.$route.params.card_slug

      await axios
          .get(`/api/v1/cards/${card_slug}`)
          .then(response => {
            this.card = response.data
          })
          .catch(err => {
              console.log(err)
              
              toast({
                  message: 'Something went wrong while getting your current card. Please try again.',
                  type: 'is-danger',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 3000,
                  position: 'bottom-right',
              })
          })

      this.$store.commit('setIsLoading', false)
    },
  }
}
</script>

<style scoped>
.twin-board-columns {
  display: flex;
  flex-direction: row;
}

.boards-container::-webkit-scrollbar {
	height: 2.4rem;
}

.boards-container::-webkit-scrollbar-thumb {
	background-color: #66a3c7;
	border: 0.8rem solid #0079bf;
	border-top-width: 0;
}

.boards-container {
	display: flex;
  flex-direction: column;
	align-items: start;
	padding: 0 0.8rem 0.8rem;
	overflow-x: auto;
	height: calc(100vh - 8.6rem);
}

</style>