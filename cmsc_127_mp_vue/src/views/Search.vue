<template>
  <div class='d-flex flex-column'>
    <div class='is-fullwidth d-flex flex-row' style='height: 50px; margin: 20px 0 20px 0;'>
      <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 200px; min-width: 200px; padding: 15px 10px 10px 10px; text-align: center;'>Search Term</h1>
      <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px;'>{{query}}</h2>
    </div>

    <div class='d-flex flex-row'>
      <div class='d-flex flex-col col-2'>
        <SearchCard 
            v-for="card in activeCards"
            :key="card.id"
            :card="card"
        />
      </div>

      <div class='d-flex flex-col col-2'>
        <SearchCard 
            v-for="card in inactiveCards"
            :key="card.id"
            :card="card"
        />
      </div>
      
      <div class='d-flex col-7' style="flex-direction: column;">
        <table v-if='boards.length != 0' class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
          <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
              <th style='color: white;'>Name (Active Boards)</th>
              <th style='color: white;'>Card</th>
              <th style='color: white;'>User(s)</th>
            </tr>
          </thead>

          <tbody>
            <template v-for='board in boards'>
            <tr
                  v-if="getActiveMatchingCard(board.id) !== '' && getActiveMatchingCard(board.id) !== null"
                  :key='board.id'
              >
                  <td id='title-overflow'>{{board.name}}</td>
                  <td>{{getActiveMatchingCard(board.id)}}</td>
                  <td>{{userDetails.username}}</td>
            </tr>
            </template>
          </tbody>
        </table>

        <table v-if='boards.length != 0' class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
          <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
              <th style='color: white;'>Name (Inactive Boards)</th>
              <th style='color: white;'>Card</th>
              <th style='color: white;'>User(s)</th>
            </tr>
          </thead>

          <tbody>
            <template v-for='board in boards'>
            <tr
                  v-if="getInactiveMatchingCard(board.id) !== '' && getInactiveMatchingCard(board.id) !== null"
                  :key='board.id'
              >
                  <td id='title-overflow'>{{board.name}}</td>
                  <td>{{getInactiveMatchingCard(board.id)}}</td>
                  <td>{{userDetails.username}}</td>
            </tr>
            </template>
          </tbody>
        </table>

        <table v-if='tasks.length != 0' class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
          <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
              <th style='color: white;'>Name (Active Tasks)</th>
              <th style='color: white;'>Board</th>
              <th style='color: white;'>User(s)</th>
            </tr>
          </thead>

          <tbody>
            <template v-for='task in tasks'>
            <tr
                  v-if="getActiveMatchingBoard(task.id) !== '' && getActiveMatchingBoard(task.id) !== null"
                  :key='task.id'
              >
                  <td id='title-overflow'>{{task.name}}</td>
                  <td>{{getActiveMatchingBoard(task.id)}}</td>
                  <td>{{userDetails.username}}</td>
            </tr>
            </template>
          </tbody>
        </table>

        <table v-if='tasks.length != 0' class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
          <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
              <th style='color: white;'>Name (Inactive Tasks)</th>
              <th style='color: white;'>Board</th>
              <th style='color: white;'>User(s)</th>
            </tr>
          </thead>

          <tbody>
            <template v-for='task in tasks'>
            <tr
                  v-if="getInactiveMatchingBoard(task.id) !== '' && getInactiveMatchingBoard(task.id) !== null"
                  :key='task.id'
              >
                  <td id='title-overflow'>{{task.name}}</td>
                  <td>{{getInactiveMatchingBoard(task.id)}}</td>
                  <td>{{userDetails.username}}</td>
            </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>

    <h2 v-if='activeCards.length == 0 && inactiveCards.length == 0 && boards.length == 0 && tasks.length == 0'>There are no matches with saved cards, boards, and tasks, please try another search</h2>
  </div>
</template>

<script>
import axios from 'axios'
import SearchCard from '@/components/SearchCard.vue'

export default {
    name: 'Search',
    components: {
        SearchCard
    },
    data() {
        return {
            totalActiveCards: [],
            totalInactiveCards: [],
            activeCards: [],
            inactiveCards: [],
            boards: [],
            tasks: [],
            userDetails: {},
            query: ''
        }
    },
    mounted() {
      this.getMyDetails()

      this.getCards()

      document.title = 'Search | Synergy'

      let uri = window.location.search.substring(1)
      let params = new URLSearchParams(uri)
      if (params.get('query')) {
          this.query = params.get('query')
          this.performSearch()
      }
    },
    methods: {
      getActiveMatchingCard (boardID) {
        for (let card in this.totalActiveCards) {
          for (let board in this.totalActiveCards[card].boards) {
            if (boardID === this.totalActiveCards[card].boards[board].id) {
              console.log('active: ' + this.totalActiveCards[card].name)
              return this.totalActiveCards[card].name
            }
          }
        }
      },
      getInactiveMatchingCard (boardID) {
        for (let card in this.totalInactiveCards) {
          for (let board in this.totalInactiveCards[card].boards) {
            if (boardID === this.totalInactiveCards[card].boards[board].id) {
              console.log('inactive: ' + this.totalInactiveCards[card].name)
              return this.totalInactiveCards[card].name
            }
          }
        }
      },
      getActiveMatchingBoard (taskID) {
        for (let card in this.totalActiveCards) {
          for (let board in this.totalActiveCards[card].boards) {
            for (let task in this.totalActiveCards[card].boards[board].tasks) {
              if (taskID === this.totalActiveCards[card].boards[board].tasks[task].id) {
                return this.totalActiveCards[card].boards[board].name
              }
            }
          }
        }
      },
      getInactiveMatchingBoard (taskID) {
        for (let card in this.totalInactiveCards) {
          for (let board in this.totalInactiveCards[card].boards) {
            for (let task in this.totalInactiveCards[card].boards[board].tasks) {
              if (taskID === this.totalInactiveCards[card].boards[board].tasks[task].id) {
                return this.totalInactiveCards[card].boards[board].name
              }
            }
          }
        }
      },
      async getCards () {
        this.$store.commit('setIsLoading', true)

        this.totalActiveCards = []
        this.totalInactiveCards = []

        await axios
            .get('/api/v1/cards/view')
            .then(response => {
              for (let card in response.data) {
                if (!response.data[card].is_history) 
                  this.totalActiveCards.push(response.data[card])
                else this.totalInactiveCards.push(response.data[card])
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
      async performSearch() {
        this.$store.commit('setIsLoading', true)

        await axios
          .post('/api/v1/cards/search/', {'query': this.query})
          .then(response => {
              this.activeCards = response.data.filter(elem => {
                return !elem.is_history
              })
              this.activeCards = response.data.filter(elem => {
                return elem.is_history
              })
          })
          .catch(error => {
              console.log(error)
          })
        
        await axios
          .post('/api/v1/boards/search/', {'query': this.query})
          .then(response => {
              this.boards = response.data
          })
          .catch(error => {
              console.log(error)
          })

        await axios
          .post('/api/v1/tasks/search/', {'query': this.query})
          .then(response => {
              this.tasks = response.data
          })
          .catch(error => {
              console.log(error)
          })
          
        this.$store.commit('setIsLoading', false)
      }
    }
}
</script>