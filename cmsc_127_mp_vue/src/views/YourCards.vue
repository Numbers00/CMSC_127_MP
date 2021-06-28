<template>
<div class="wrapper">
  <TopSection viewType="YourCards" />
  <swiper id='top-cards-swiper' v-if="countMarkedCards() !== 0" class="swiper mt-5" style="height: 300px" :options="swiperOption">
      <swiper-slide
        v-for="(card, index) in activeCards"
        :key="index"
      >
        <CardBox
          :card="card"
        />
      </swiper-slide>
      <template v-if="countMarkedCards() < 6">
        <swiper-slide 
          v-for="n in 6 - countMarkedCards()"
          :key="n"
        >
          <CardBox
            :card="emptyCard"
          />
        </swiper-slide>
      </template>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
  <ChangeSection :activeCards="activeCards" />
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
  mounted () {
    this.getMyDetails()

    this.getActiveCards()

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
    async getActiveCards () {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/cards/view')
          .then(response => {
            for (let card in response.data) {
              if (!response.data[card].is_history) 
                this.activeCards.push(response.data[card])
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
    countMarkedCards () {
      let counter = 0
      for (let card in this.activeCards) {
        if (this.activeCards[card].is_marked) counter += 1
      }
      console.log('counter ' + counter)
      return counter
    },
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