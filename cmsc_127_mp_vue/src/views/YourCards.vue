<template>
<div class="wrapper">
  <TopSection viewType="YourCards" />
  <swiper id='top-cards-swiper' v-if="activeCards.length !== 0" class="swiper mt-5" style="height: 300px" :options="swiperOption">
      <swiper-slide
        v-for="card in activeCards"
        :key="card.id"
      >
        <CardBox
          :card="card"
          v-on:resendGet="resendGet"
        />
      </swiper-slide>
      <template v-if="activeCards.length < 6">
        <swiper-slide 
          v-for="n in 6 - activeCards.length"
          :key="n"
        >
          <CardBox
            :card="emptyCard"
          />
        </swiper-slide>
      </template>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
  <swiper id='top-cards-swiper' v-if="inactiveCards.length !== 0" class="swiper mt-5" style="height: 300px" :options="swiperOption">
      <swiper-slide
        v-for="card in inactiveCards"
        :key="card.id"
      >
        <CardBox
          :card="card"
          v-on:resendGet="resendGet"
        />
      </swiper-slide>
      <template v-if="inactiveCards.length < 12">
        <swiper-slide 
          v-for="n in 6 - inactiveCards.length"
          :key="n"
        >
          <CardBox
            :card="emptyCard"
          />
        </swiper-slide>
      </template>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
  <ChangeSection 
    :activeCards="activeCards"
    v-on:resendGet='resendGet'
  />
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.min.css'

import TopSection from '@/components/TopSection.vue'
import ChangeSection from '@/components/ChangeSection.vue'
import CardBox from '@/components/CardBox.vue'
import LowerCardBox from '@/components/LowerCardBox.vue'

export default {
  name: 'Home',
  components: {
    Swiper,
    SwiperSlide,
    TopSection,
    ChangeSection,
    CardBox,
    LowerCardBox
  },
  data () {
    return {
      myDetails: {},
      activeCards: [],
      inactiveCards: [],
      emptyCard: {
        name: 'Empty Slot',
        image: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAAAA1BMVEVxeX67CaE5AAAAR0lEQVR4nO3BAQEAAACCIP+vbkhAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO8GxYgAAb0jQ/cAAAAASUVORK5CYII=',
        is_marked: false,
        is_visible: false,
        get_absolute_url: '/your-cards'
      },
      addToggle: false,
      removeToggle: false,
      updateToggle: false,
      swiperOption: {
        slidesPerView: 5,
        spaceBetween: 40,
        loop: false,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      }
    }
  },
  watch: {
    activeCards () {
      console.log(this.activeCards)
    }
  },
  mounted () {
    this.getMyDetails()

    this.getCards ()

    document.title = 'Your Cards | Synergy'
  },
  methods: {
    async getMyDetails () {
        this.$store.commit('setIsLoading', true)

        await axios
          .get('api/v1/users/')
          .then(response => {
              this.myDetails = response.data[0]
          })
          .catch(error => {
              console.log(error)
          })

        this.$store.commit('setIsLoading', false)
    },
    async getCards () {
      this.$store.commit('setIsLoading', true)

      this.activeCards = []
      this.inactiveCards = []

      await axios
          .get('/api/v1/cards/view')
          .then(response => {
            for (let card in response.data) {
              if (!response.data[card].is_history) 
                this.activeCards.push(response.data[card])
              else this.inactiveCards.push(response.data[card])
            }
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
    countActiveCards () {
      let counter = 0
      for (let card in this.activeCards) {
        if (!this.activeCards[card].is_history) counter += 1
      }
      return counter
    },
    resendGet () {
      
      this.getCards()

      this.$emit('resendGet')
    }
  }
}
</script>

<style scoped>
#top-cards-swiper {
  width: 100%;
  position: relative;
  background: #A0A0A0;
  min-height: 180px;
  max-height: 180px;
  height: 180px;
  border-radius: 10px;
  bottom: 10px;
}
.swiper-slide {
  width: 60%;
  transform: translate(0, -50px);
}
.swiper-slide:nth-child(2n) {
  width: 40%;
}
.swiper-slide:nth-child(3n) {
  width: 20%;
}
</style>