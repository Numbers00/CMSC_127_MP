<template>
<div class="wrapper column is-3 position-relative" style="top: 20px;">
  <i @click="markCard" v-if="card.is_marked" class="fas fa-star"></i>
  <i @click="markCard" v-if="!card.is_marked" class="far fa-star"></i>

  <figure class="image">
    <img 
      @click="!card.is_history ? $router.push({path: '' + card.get_absolute_url, append: false}) : $router.push({path: '/history/' + card.get_absolute_url, append: false})" 
      :src="card.image" 
      id="card-img" 
    />
  </figure>

  <div class="image-text">
    <p class="is-size-5"><b>{{ card.name }}</b></p>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: "CardBox",
  props: {
    card: Object,
    myDetails: Object
  },
  methods: {
    async markCard () {
      this.$store.commit('setIsLoading', true)

      await axios({
      method: 'put',
      url: '/api/v1/cards/view/',
      data: {
        target_card_id: this.card.id,
        name: this.card.name,
        description: this.card.description,
        image: this.card.image,
        is_marked: !this.card.is_marked,
        is_visible: this.card.is_visible,
        is_history: this.card.is_history,
        slug: this.slugify(this.card.name)
      }
      }).then(response => {
        toast({
          message: "The card's mark has been successfully changed",
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
        this.newcard = ''
        this.$emit('resendGet')
      })
      .catch(error => {
        console.log(error)
        toast({
            message: 'Something went wrong while marking the card. Please try again.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
        })
      })

      this.$store.commit('setIsLoading', false)
    },
    slugify (text) {
      return text
        .toLowerCase()
        .replace(/ /g,'-')
        .replace(/[-]+/g, '-')
        .replace(/[^\w-]+/g,'')
        .replace(/_/g, '')
    },
  }
};
</script>

<style scoped>
.wrapper:hover {
  cursor: pointer;
}
.image {
  max-width: 240px;
  width: 240px;
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  border-radius: 10px;
  position: relative;
  top: 50px;
  left: 20px;
}
.image-text {
  z-index: 10;
  position: absolute;
  color: black;
  text-align: center;
  overflow: hidden;
  top: 110px;
  left: 20px;
  min-width: 220px;
  width: 220px;
  min-height: 70px;
  height: 70px;
  max-height: 70px;
}
#card-img {
  max-width: 240px;
  width: 240px;
  max-height: 160px;
  height: 160px;
  border-radius: 10px;
}
.button {
  width: 90%;
}
</style>

<style scoped>
.fa-star {
  position: absolute;
  top: 50px;
  left: 215px;
  z-index: 12;
  font-size: 22px;
}
</style>
