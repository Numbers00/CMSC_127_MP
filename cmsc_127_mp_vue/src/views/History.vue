<template>
<div class="wrapper">
  <TopSection v-if="activeCards.length" viewType="CardView" :cardName="card.name" />
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
      <template v-if="inactiveCards.length < 6">
        <swiper-slide 
          v-for="n in 6 - inactiveCards.length"
          :key="n + card.name"
        >
          <CardBox
            :card="emptyCard"
          />
        </swiper-slide>
      </template>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
  <div class="is-fullwidth d-flex flex-row justify-content-between">
    <div class="d-flex flex-column">
      
      <div v-if="toggleBoard" class="col-12 rounded mb-3">
        <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Card</h6>
            </div>
            <div class="col-sm-9" style="color: white;">
              {{card.name}}
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Name</h6>
            </div>
            <div class="col-sm-9" style="color: white;">
              {{selectedBoard.name}} (Board)
            </div>
          </div>
          <hr>
          <div class="row">
          </div>
        </div>
      </div>

      <div v-if="toggleTask" class="col-12 rounded mb-3">
        <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Board</h6>
            </div>
            <div class="col-sm-9" style="color: white;">
              {{selectedBoard.name}}
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Name</h6>
            </div>
            <div class="col-sm-9" style="color: white;">
              {{selectedTask.name}} (Task) ({{selectedTask.is_marked ? 'Marked' : 'Unmarked'}})
            </div>
          </div>
          <hr>
          <div class="row">
          </div>
        </div>
      </div>

      <div class="twin-board-columns">
      <section class="boards-container">
        <template v-for="(board, index) in card.boards">
          <BoardBox
            v-if="index % 2 === 0"
            :key="board.id"
            :card="card"
            :board="board"
            :tasks="board.tasks"
            :isEmpty="false"
            v-on:resendGet="resendGet"
            v-on:selectTask="selectTask"
            v-on:selectBoard="selectBoard"
          />
        </template>
        <template v-for="n in 6 - Math.ceil(card.boards.length / 2)">
          <BoardBox
            :key="n + card.name"
            :card="card"
            :board="emptyBoard"
            :tasks="[]"
            :isEmpty="true"
            v-on:resendGet="resendGet"
          />
        </template>
      </section>
      <section class="boards-container">
        <template v-for="(board, index) in card.boards">
          <BoardBox
            v-if="index % 2 !== 0"
            :key="board.id"
            :card="card"
            :board="board"
            :tasks="board.tasks"
            :isEmpty="false"
            v-on:resendGet="resendGet"
            v-on:selectTask="selectTask"
            v-on:selectBoard="selectBoard"
          />
        </template>
        <template v-for="n in 6 - Math.floor(card.boards.length / 2)">
          <BoardBox
            :key="n + card.name"
            :card="card"
            :board="emptyBoard"
            :tasks="[]"
            :isEmpty="true"
            v-on:resendGet="resendGet"
          />
        </template>
      </section>
    </div>

    </div>
    <div class="right-col d-flex flex-column">
      <table class='table is-fullwidth table-striped' style='margin-top: 20px;'>
        <thead>
          <tr style='background-color: hsl(0, 0%, 21%);'>
            <th style='color: white;'>Name</th>
            <th style='color: white;'>Board</th>
            <th style='color: white;'>User(s)</th>
          </tr>
        </thead>
        
        <tbody>
          <template v-for='board in card.boards'>
            <template v-for='task in board.tasks'>
              <tr
                  v-if="task.is_marked && task.status === 'todo'"
                  :key='task.id'
              >
                <td id='title-overflow'>{{task.name}}</td>
                <td>{{board.name}}</td>
                <td class='desc-col'>{{userDetails.username}}</td>
                <i 
                  @click="!card.is_history ? finishTask(task, board) : ''"
                  class="times-icon fa fa-times ml-2 mt-1 position-absolute"
                >
                </i>
              </tr>
            </template>
          </template>
        </tbody>
      </table>

      <div class="col-12 rounded">
        <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
          <div class="d-flex flex-column align-items-center text-center">
            <img :src="profilePicture"
              alt="User" class="rounded-circle" style="min-width: 150px; width: 150px; max-width: 150px; min-height: 150px; height: 150px; max-height: 150px;">
            <div class="mt-3">
              <h4 style="color: white;">{{userDetails.username}}</h4>
              <p class="mb-1" style="color: white;">{{userDetails.email}}</p>
            </div>
          </div>
        </div>
      </div>

      <table class='table is-fullwidth table-striped' style='margin-top: 20px;'>
        <thead>
          <tr style='background-color: hsl(0, 0%, 21%);'>
            <th style='color: white;'>Name</th>
            <th style='color: white;'>Board</th>
            <th style='color: white;'>User(s)</th>
          </tr>
        </thead>
        
        <tbody>
          <template v-for='board in card.boards'>
            <template v-for='task in board.tasks'>
              <tr
                  v-if="task.status === 'done'"
                  :key='task.id'
              >
                <td id='title-overflow'>{{task.name}}</td>
                <td>{{board.name}}</td>
                <td class='desc-col'>
                  {{userDetails.username}}
                </td>
                <i 
                  @click="!card.is_history ? removeTask(task, board) : ''"
                  class="times-icon fa fa-times ml-2 mt-1 position-absolute"
                >
                </i>
              </tr>
            </template>
          </template>
        </tbody>
      </table>

    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'
import { uuid } from 'vue-uuid'

import TopSection from '@/components/TopSection.vue'
import CardBox from '@/components/CardBox.vue'
import BoardBox from '@/components/BoardBox.vue'

export default {
  name: 'CardView',
  data () {
    return {
      card: {},
      activeCards: [],
      inactiveCards: [],
      selectedBoard: {},
      selectedTask: {},
      toggleBoard: false,
      toggleTask: false,
      uuid: uuid.v4(),
      emptyBoard: {
        "name": "Empty Board",
        "description": "this is an empty board",
        "tasks": []
      },
      emptyCard: {
        name: 'Empty Slot',
        image: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAAAA1BMVEVxeX67CaE5AAAAR0lEQVR4nO3BAQEAAACCIP+vbkhAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO8GxYgAAb0jQ/cAAAAASUVORK5CYII=',
        is_marked: false,
        is_visible: false,
        get_absolute_url: '/your-cards'
      },
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
  components: {
    BoardBox,
    TopSection,
    CardBox
  },
  mounted () {
    this.getCards()
    this.getMyDetails()
    this.getChosenCard()

    document.title = 'History | Synergy'
  },
  watch: {
    $route(to, from) {
      if (to.name === 'CardView') {
        this.getCards()
        this.getChosenCard()
      }
    },
  },
  computed: {
    profilePicture () {
      if (this.userDetails.profile_picture === '' || this.userDetails.profile_picture === null) {
        return 'https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png'
      }
      else return this.userDetails.profile_picture
    }
  },
  methods: {
    async getMyDetails () {
      this.$store.commit('setIsLoading', true)
      await axios({
        method: 'get',
        url: 'api/v1/users/'
        })
        .then(response => {
          console.log(response.data)
          console.log(this.$store.state.token)
          console.log(localStorage.getItem('username'))
          for (let data in response.data) {
            console.log(response.data[data])
            if (localStorage.getItem('username') === response.data[data].username) {
              this.userDetails = response.data[data]
            }
          }
        })
        .catch(error => {
            console.log(error)
        })
      
      this.$store.commit('setIsLoading', false)
    },
    selectTask (task, board) {
      if (this.selectedTask === task) {
        this.selectedTask = ''
        this.selectedBoard = ''

        this.toggleTask = false
        this.toggleBoard = false
      }
      else {
        this.selectedTask = task
        this.selectedBoard = board

        this.toggleTask = true
        this.toggleBoard = false
      }
    },
    selectBoard (board) {
      if (this.selectedBoard === board) {
        this.selectedTask = ''
        this.selectedBoard = ''

        this.toggleTask = false
        this.toggleBoard = false
      }
      else {
        this.selectedBoard = board
        
        this.toggleTask = false
        this.toggleBoard = true
      }
    },
    async getChosenCard () {
      this.$store.commit('setIsLoading', true)
      
      this.card = {}

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

      console.log(this.card)

      this.$store.commit('setIsLoading', false)
    },
    async getCards () {
      this.$store.commit('setIsLoading', true)

      this.activeCards = []
      this.inactiveCards = []

      await axios
          .get('/api/v1/cards/view')
          .then(response => {
            this.activeCards = response.data.filter(elem => {
              return !elem.is_history
            })
            this.inactiveCards = response.data.filter(elem => {
              return elem.is_history
            })
          })
          .catch(err => {
              console.log(err)
              
              toast({
                  message: 'Something went wrong while getting your cards. Please try again.',
                  type: 'is-danger',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
              })
          })

      this.$store.commit('setIsLoading', false)
    },
    async finishTask (task, board) {
      this.$store.commit('setIsLoading', true)

      await axios({
      method: 'put',
      url: '/api/v1/tasks/view/',
      data: {
        target_task_id: task.id,
        target_board_id: board.id,
        name: task.name,
        description: task.description,
        is_marked: task.is_marked,
        status: 'done',
        slug: this.slugify(task.name)
      }
      }).then(response => {
        toast({
          message: 'The task is now set to done in the database',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
        this.resendGet()
      })
      .catch(error => {
        console.log(error)
        toast({
            message: 'Something went wrong while setting the task to done. Please try again.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
        })
      })

      this.$store.commit('setIsLoading', false)
    },
    async removeTask (task, board) {
      this.$store.commit('setIsLoading', true)

      await axios({
      method: 'delete',
      url: '/api/v1/tasks/view/',
      data: {
        target_board_id: board.id,
        id: task.id
      }
      }).then(response => {
        toast({
          message: 'The task has been removed from the database',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
        this.newTask = ''
        this.$emit('resendGet')
      })
      .catch(error => {
        console.log(error)
        toast({
            message: 'Something went wrong while removing the task. Please try again.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
        })
      })

      this.resendGet()

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
    resendGet () {

      this.getChosenCard()
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

<style scoped>
.twin-board-columns {
  display: flex;
  flex-direction: row;
}

.boards-container {
	display: flex;
  flex-direction: column;
	align-items: start;
	padding: 0 0.8rem 0.8rem;
	overflow-x: auto;
	height: 1360px;
}

.right-col {
  width: 750px;
}

.desc-col {
  max-width: 50%;
  width: 50%;
  max-height: 120px;
  overflow: auto;
}
</style>

<style scoped>
.main-body {
  padding: 15px;
}
.col-12 {
  background-color: hsl(0,0%,21%);
  border-radius: 10px;
}
.card {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 0 solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}

.card-body {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 1rem;
}

.gutters-sm {
  margin-right: -8px;
  margin-left: -8px;
}

.gutters-sm > .col,
.gutters-sm > [class*="col-"] {
  padding-right: 8px;
  padding-left: 8px;
}
.mb-3,
.my-3 {
  margin-bottom: 1rem !important;
}

.bg-gray-300 {
  background-color: #e2e8f0;
}
.h-100 {
  height: 100% !important;
}
.shadow-none {
  box-shadow: none !important;
}

.times-icon {
  right: 60px;
  background-color: none;
  border: none;
  z-index: 9;
}

.times-icon:hover {
  cursor: pointer;
}
</style>