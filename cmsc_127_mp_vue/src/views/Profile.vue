<template>
<div class="container">
  <div class="main-body" style="color: white;">

    <div class="row gutters-sm">
      <div class="col-md-4 mb-3">
          <div class="col-12 rounded">
              <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
                  <div class="d-flex flex-column align-items-center text-center">
                      <img :src="userDetails.profile_picture"
                          alt="User" class="rounded-circle" style="min-width: 150px; width: 150px; max-width: 150px; min-height: 150px; height: 150px; max-height: 150px;">
                      <div class="mt-3">
                          <h4>{{userDetails.username}}</h4>
                          <p class="text-secondary mb-1">{{userDetails.email}}</p>
                          <p class="text-muted font-size-sm">{{userDetails.address}}</p>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-12 rounded mt-3">
              <h1 style="text-align: center; padding-top: 20px; font-family: Quicksand;">{{activeCards.length + inactiveCards.length}}</h1>
              <br>
              <h5 style="text-align: center;">Total Cards</h5>
              <hr>
              <h1 style="text-align: center; padding-top: 20px; font-family: Quicksand;">{{inactiveCards.length}}</h1>
              <br>
              <h6 style="text-align: center; text-transform:uppercase; letter-spacing: 2px;">Active Cards</h6>
              <h1 style="text-align: center; padding-top: 20px; font-family: Quicksand;">{{inactiveCards.length}}</h1>
              <br>
              <h6 style="text-align: center; text-transform:uppercase; letter-spacing: 2px;">Inactive Cards</h6>
              <br>
          </div>
      </div>
      <div class="col-md-8">
        <div class="col-12 rounded mb-3">
          <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Username</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails.username}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Email</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails.email}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Bio</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                <span v-if="userDetails.bio !== '' && userDetails.bio !== null">{{userDetails.bio}}</span>
                <span v-else>N/A</span>
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Plan Level</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails.plan_level}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Date Joined</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails.date_joined.substring(0, 10)}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-12" style="text-align: left;">
                <a class="btn btn-info" target="__blank"
                    href="https://www.bootdey.com/snippets/view/profile-edit-data-and-skills">Edit</a>
              </div>
            </div>
          </div>
        </div>
        <div class="row gutters-sm">
          <div class="col-sm-8 mb-3">
            <div class="col-12 rounded h-100">
              <div class="col-12 rounded" style="padding: 20px 10px 20px 10px;">
                <h6 class="d-flex align-items-center mb-3">Recent Activity:</h6>
                <hr>
                <!-- <OrderSummary
                    v-for='order in orders'
                    :key='order.id'
                    :order='order'
                /> -->
              </div>
            </div>
          </div>
          <div class="col-sm-4 mb-3" style="max-height: 270px; min-height: 270px; height: 270px;">
            <div class="col-12 rounded h-100">
              <div class="col-12 rounded"
                style="height: 255px; padding: 20px 10px 20px 10px;">
                <h6 class="d-flex align-items-center mb-3">Quote of the
                  Day</h6>
                <hr>
                <i class="fa fa-quote-left"></i>
                <br>
                <span v-if="userDetails.quote === '' || userDetails.quote === null" style="position: relative; left: 90px;">N/A</span>
                <span v-else>{{userDetails.quote}}</span>
                <br>
                <i class="fa fa-quote-right" style="float: right;"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Profile',
    components: {
    },
    data () {
        return {
            orders: [],
            userDetails: {},
            activeCards: [],
            inactiveCards: []
        }
    },
    mounted () {
      document.title = 'Profile | Synergy'

      this.getCards()
      this.getMyDetails()
    },
    watch: {
      userDetails () {
        console.log(this.userDetails)
      }
    },
    methods: {
      async getCards () {
        this.$store.commit('setIsLoading', true)

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
      logout () {
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        localStorage.removeItem('userid')
        this.$store.commit('removeToken')
        this.$router.push('/')
      },
      async getMyDetails () {
        this.$store.commit('setIsLoading', true)
        await axios
          .get('api/v1/users/')
          .then(response => {
              this.userDetails = response.data[0]
          })
          .catch(error => {
              console.log(error)
          })
        
        this.$store.commit('setIsLoading', false)
      },
    }
}
</script>

<style scoped>
body {
  margin-top: 20px;
  color: #1a202c;
  text-align: left;
  background-color: #e2e8f0;
}
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
</style>