<template>
<div style="margin-top: 25px;">
    <div class="container-fluid">
      <div class="row no-gutter">
        <div class="col-md-6 d-none d-md-flex bg-image" style="border-radius: 10px 0 0 10px;"></div>
        <div class="col-md-6" style="background-color: black; border-radius: 0 10px 10px 0;">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-lg-7 col-xl-6 mx-auto">
                  <h3
                    class="display-4"
                    style="color: white; letter-spacing: 4px"
                  >
                    LOGIN
                  </h3>
                  <br />
                  <form @submit.prevent="submitForm">
                    <div class="form-group mb-3">
                      <input
                        id="inputUsername"
                        type="username"
                        v-model="username"
                        placeholder="username"
                        required
                        autofocus=""
                        class="form-control rounded-pill border-0 shadow-sm px-4"
                      />
                    </div>
                    <div class="form-group mb-3 d-flex flex-row">
                      <input
                        id="inputPassword"
                        :type="isHidden"
                        v-model="password"
                        placeholder="Password"
                        style="border-radius: 20px 0 0 20px;"
                        required
                        class="form-control border-0 shadow-sm px-4 text-danger"
                      />
                      <button type="button" @click="isHidden === 'text' ? isHidden = 'password' : isHidden = 'text'" class="btn btn-danger position-relative" style="color: white; border-radius: 0 20px 20px 0;">
                        <span class="icon">
                        <i class="far fa-eye"></i>
                        </span>
                      </button>
                      <br />
                    </div>
                    <button
                      type="submit"
                      class="btn btn-danger btn-block text-uppercase mb-2 rounded-pill shadow-sm"
                    >
                      Sign in
                    </button>
                    <div style="padding-top: 10px">
                      <p class="signup">
                        <a @click="$router.push({ name: 'Signup' })" style="text-decoration: none"
                          >New User? Register here!</a
                        >
                      </p>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div
            class="row px-3 text-center justify-content-center mb-0 social"
            style="padding-top: 70px; transform: translateY(-150px)"
          >
            <a @click="$router.push({ name: 'Home' })"
              ><span
                class="fa fa-home"
                style="font-size: 2rem; color: white"
              ></span
            ></a>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      isHidden: 'password',
      takenSlugs: []
    }
  },
  mounted () {
    this.getUsernames()

    document.title = 'Login | Code & Chill'
  },
  methods: {
    async getUsernames () {
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
          for (let user in response.data) {
            this.takenSlugs.push(response.data[user].username)
          }
        })
        .catch(error => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data))
          } 
          else if (error.message) {
            console.log(JSON.stringify(error))
          }

          toast({
            message: 'Something went wrong while getting the taken usernames...',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
      
      this.$store.commit('setIsLoading', false)
    },
    async submitForm () {
      axios.defaults.headers.common['Authorization'] = ''

      localStorage.removeItem('token')

      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
        .post('/api/v1/token/login/', formData)
        .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
            localStorage.setItem('token', token)
            
            const toPath = this.$route.query.to || '/'
            this.$router.push(toPath)
        })
        .catch(error => {
          for (let takenSlug in this.takenSlugs) {
            if (this.slugify(this.username) === this.takenSlugs[takenSlug]) {
              toast({
                message: 'Username and Password do not match, please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 5000,
                position: 'bottom-right',
              })
              break
            }
          }

          if (error.response) {
            console.log(JSON.stringify(error.response.data))
          } 
          else {
            console.log(JSON.stringify(error))
          }
        })
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
}
</script>

<style>
.login,
.image {
  min-height: 100vh;
}

.bg-image {
  background-image: url("https://images.pexels.com/photos/3879495/pexels-photo-3879495.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  background-size: cover;
  background-position: center;
}

.signup {
  text-decoration: none;
  color: white;
  text-align: right;
}

.signup:hover {
  text-decoration: none;
  color: white;
}

</style>
