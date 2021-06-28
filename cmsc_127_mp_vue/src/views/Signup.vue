<template>
<div id="contents">
 <div class="container px-2 px-md-4 py-5 mx-auto">
   <div class="row">
   <div class="col-12 border-0">
     <div class="row d-flex">
       <div class="col-lg-5" style="min-height: 600px; height: 600px;">
         <div class="card1 pb-5">
           <div class="row px-3">
             <div class="col-12">
               <a
                 @click="$router.push({ name: 'Home' })"
                 style="text-align: right; text-decoration: none"
                 ><span
                   class="fa fa-home"
                   style="font-size: 2.5rem; color: white; padding-top: 20px"
                 ></span>
                 <span style="color: white; font-size: 1.5rem"
                   >&nbsp; Synergy</span
                 ></a
               >
             </div>
           </div>
           <div class="row px-3 justify-content-center mt-4 mb-5">
             <div
                id="carouselExampleIndicators"
                class="carousel slide"
                data-ride="carousel"
                data-interval="5000"
              >
                <ol class="carousel-indicators">
                  <li
                    data-target="#carouselExampleIndicators"
                    data-slide-to="0"
                    id="li1"
                  ></li>
                  <li
                    data-target="#carouselExampleIndicators"
                    data-slide-to="1"
                    id="li2"
                  ></li>
                  <li
                    data-target="#carouselExampleIndicators"
                    data-slide-to="2"
                    id="li3"
                    class="active"
                  ></li>
                  <li
                    data-target="#carouselExampleIndicators"
                    data-slide-to="3"
                    id="li4"
                  ></li>
                  <li
                    data-target="#carouselExampleIndicators"
                    data-slide-to="4"
                    id="li5"
                  ></li>
                </ol>
                <div class="carousel-inner">
                  <div class="carousel-item col-12 card border-0 card-0">
                    <div class="text-center">
                      <img
                        src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                        class="img-fluid profile-pic"
                      />
                    </div>
                    <h6 class="font-weight-bold mt-5">Joackin Santos</h6>
                    <small class="mb-2">Joackin</small>
                    <hr width="50%" />
                    <p class="content mt-2 mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipisicing
                      elit, sed do eiusmod incididunt ut labore et dolore
                      magna aliqua.<br />Duis aute irure dolor in
                      reprehenderit in voluptate velit esse cillum dolore eu
                      fugiat nulla pariatur.
                    </p>
                  </div>
                  <div class="carousel-item col-12 card border-0 card-0">
                    <div class="text-center">
                      <img
                        src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                        class="img-fluid profile-pic"
                      />
                    </div>
                    <h6 class="font-weight-bold mt-5">Kyle Aquino</h6>
                    <small class="mb-2">Kyle</small>
                    <hr width="50%" />
                    <p class="content mt-2 mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipisicing
                      elit, sed do eiusmod incididunt ut labore et dolore
                      magna aliqua.<br />Duis aute irure dolor in
                      reprehenderit in voluptate velit esse cillum dolore eu
                      fugiat nulla pariatur.
                    </p>
                  </div>
                  <div class="carousel-item active col-12 card border-0 card-0">
                    <div class="text-center">
                      <img
                        src="https://icons.iconarchive.com/icons/grafikartes/adobe-cc/128/CC-icon.png"
                        class="img-fluid profile-pic"
                      />
                    </div>
                    <h6 class="font-weight-bold mt-5">Plan for the Future</h6>
                    <small class="mb-2">Who are we?</small>
                    <hr width="50%" />
                    <p class="content mt-2 mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipisicing
                      elit, sed do eiusmod incididunt ut labore et dolore
                      magna aliqua.<br />Duis aute irure dolor in
                      reprehenderit in voluptate velit esse cillum dolore eu
                      fugiat nulla pariatur.
                    </p>
                  </div>
                  <div class="carousel-item col-12 card border-0 card-0">
                    <div class="text-center">
                      <img
                        src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                        class="img-fluid profile-pic"
                      />
                    </div>
                    <h6 class="font-weight-bold mt-5">Joackin Santos</h6>
                    <small class="mb-2">Joackin</small>
                    <hr width="50%" />
                    <p class="content mt-2 mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipisicing
                      elit, sed do eiusmod incididunt ut labore et dolore
                      magna aliqua.<br />Duis aute irure dolor in
                      reprehenderit in voluptate velit esse cillum dolore eu
                      fugiat nulla pariatur.
                    </p>
                  </div>
                  <div class="carousel-item col-12 card border-0 card-0">
                    <div class="text-center">
                      <img
                        src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                        class="img-fluid profile-pic"
                      />
                    </div>
                    <h6 class="font-weight-bold mt-5">Kyle Aquino</h6>
                    <small class="mb-2">Kyle</small>
                    <hr width="50%" />
                    <p class="content mt-2 mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipisicing
                      elit, sed do eiusmod incididunt ut labore et dolore
                      magna aliqua.<br />Duis aute irure dolor in
                      reprehenderit in voluptate velit esse cillum dolore eu
                      fugiat nulla pariatur.
                    </p>
                  </div>
                </div>
              </div>
           </div>
         </div>
       </div>
       <div class="col-lg-7">
         <div class="col-12 border-0 border-light px-4 px-sm-5 py-5 position-relative" style="right: 24px; background-color: #A0A0A0; border-radius: 0 3% 3% 0; min-height: 600px; height: 600px;">
           <small class="text-right mb-3"
             ><a @click="$router.push({ name: 'Login' })"
               ><u>I already have an account</u></a
             ></small
           >
           <h3 class="mb-1" style="text-transform: uppercase; letter-spacing: 3px;">Sign up</h3>
           <p class="mb-4 text-sm">We're glad you're here with us today!</p>
           <form @submit.prevent="submitForm">
            <div class="row mt-3">
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm label-required">Username:</h6>
                </label>
                <input 
                  type="text" 
                  v-model="username" 
                  name="username" 
                  placeholder="John Doe" 
                  required 
                />
              </div>
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm label-required">Email:</h6>
                </label>
                <input
                  type="text"
                  v-model="email"
                  name="email"
                  placeholder="john.doe@email.com"
                  required
                />
              </div>
            </div>
            <div class="row px-3">
              <label class="mb-0 position-relative" style="right: 10px;">
                <h6 class="mb-0 text-sm">Profile Picture:</h6>
              </label>
              <input 
                type="text" 
                v-model="profile_picture" 
                name="number" 
                placeholder="https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png" 
              />
            </div>
            <div class="row px-3">
              <label class="mb-0 position-relative" style="right: 10px;">
                <h6 class="mb-0 text-sm">Background Image:</h6>
              </label>
              <input 
                type="text" 
                v-model="bg_image" 
                name="number" 
                placeholder="https://img.pngio.com/calming-blue-by-shadowscorcher-on-deviantart-soothing-background-png-1280_800.png" 
              />
            </div>
            <div class="row mt-3 position-relative" style="bottom: 15px;">
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm label-required">Password:</h6><span v-if="passwordIsChanged" class="password-strength-checker" :class="{'is-very-strong': this.passwordStrength === 'Very Strong', 'is-strong': this.passwordStrength === 'Strong', 'is-moderate': this.passwordStrength === 'Moderate', 'is-weak': this.passwordStrength === 'Weak', 'is-bad': !this.passwordStrength.includes('Strong') && !this.passwordStrength.includes('Moderate') && !this.passwordStrength.includes('Weak')}">({{this.passwordStrength}})</span>
                </label>
                <div class="d-flex flex-row">
                  <input 
                    :type="isHidden" 
                    v-model="password1" 
                    name="password1" 
                    placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;" 
                    style="border-radius: 10px 0 0 10px;"
                    required 
                  />
                  <button type="button" @click="isHidden === 'text' ? isHidden = 'password' : isHidden = 'text'" class="button position-relative" style="background: #4402cf; color: white; border-radius: 0 10px 10px 0; top: 3px; border: 1px solid #4402cf; padding: 20px;">
                      <span class="icon">
                      <i class="far fa-eye"></i>
                      </span>
                  </button>
                </div>
              </div>
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm label-required">Retype Password:</h6>
                </label>
                <div class="d-flex flex-row">
                  <input
                    :type="isHidden"
                    v-model="password2"
                    name="password2"
                    placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;"
                    style="border-radius: 10px 0 0 10px;"
                    required
                  />
                  <button type="button" @click="isHidden === 'text' ? isHidden = 'password' : isHidden = 'text'" class="button position-relative" style="background: #4402cf; color: white; border-radius: 0 10px 10px 0; top: 3px; border: 1px solid #4402cf; padding: 20px;">
                      <span class="icon">
                      <i class="far fa-eye"></i>
                      </span>
                  </button>
                </div>
              </div>
            </div>
            <p style="color: red; position: relative; bottom: 20px;">Fields with * are required.</p>
            <div class="row px-3 mb-3 position-relative" style="bottom: 15px;">
              If you're okay with the details you have provided, you may now click the button below.
            </div>
            <div class="row mb-4 position-relative" style="bottom: 15px;">
              <div class="col-md-12">
                <button type="submit" class="btn btn-blue text-center mb-1 py-2">
                  Create Account
                </button>
              </div>
            </div>
           </form>
         </div>
       </div>
       </div>
     </div>
   </div>
 </div>
 <link
   href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
   rel="stylesheet"
 />
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'Signup',
  data () {
    return {
      isHidden: 'password',
      username: '',
      email: '',
      bio: '',
      profile_picture: '',
      bg_image: '',
      plan_level: 'bronze',
      password1: '',
      password2: '',
      takenSlugs: [],
      passwordStrength: '',
      passwordIsChanged: false,
      errors: []
    }
  },
  mounted () {
    this.getUsernames()

    document.title = 'Signup | Synergy'
  },
  watch: {
    takenSlugs () {
      console.log(this.takenSlugs)
    },
    password1 () {
      this.passwordIsChanged = true

      this.passwordStrengthChecker()
    }
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
            this.takenSlugs.push(response.data[user].get_absolute_url)
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
            duration: 5000,
            position: 'bottom-right',
          })
        })
      
      this.$store.commit('setIsLoading', false)
    },
    async submitForm () {
      this.$store.commit('setIsLoading', true)

      this.errors = []

      if (this.username === '') {
        this.errors.push('The Username Field is Required!')
      }

      if (this.username.length > 32) {
        this.errors.push("The Username Field's maximum length is only 32!")
      }

      for (let takenSlug in this.takenSlugs) {
        if (this.slugify(this.username) === this.takenSlugs[takenSlug]) {
          this.errors.push("The Username is already taken! Please try another username.")
          break
        }
      }

      if (this.email === '') {
        this.errors.push('The Email Field is Required!')
      }

      if (this.email.length > 128) {
        this.errors.push("The Email Field's maximum length is only 128!")
      }

      if (this.password1 === '') {
        this.errors.push("The Password Field is Required!")
      }

      if (this.password1.length < 8) {
        this.errors.push("The Password Field should have a minimum of 8 characters!")
      }

      if (this.password1.length > 128) {
        this.errors.push("The Password Field's maximum length is only 128!")
      }

      if (this.passwordStrength.includes('same') || this.passwordStrength.includes('similar')) {
        this.errors.push("The Password, Username, and Email must not be too similar!")
      }

      if (this.password2 === '') {
        this.errors.push("The Retype Password Field is Required!")
      }

      if (this.password1 !== this.password2) {
        this.errors.push("The Retype Password Field should have the same input as the Password Field!")
      }

      if (!this.errors.length) {
        let profile_picture = ''
        let bg_image = ''

        if (this.profile_picture === '' || this.profile_picture === null) {
          profile_picture = 'https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png'
        }

        if (this.bg_image === '' || this.bg_image === null) {
          bg_image = 'https://img.pngio.com/calming-blue-by-shadowscorcher-on-deviantart-soothing-background-png-1280_800.png'
        }

        const formData = {
          username: this.username,
          email: this.email,
          bio: this.bio,
          profile_picture: profile_picture,
          bg_image: bg_image,
          plan_level: this.plan_level,
          password: this.password1,
          slug: this.slugify(this.username)
        }

        await axios
          .post('/api/v1/users/', formData)
          .then(response => {
            this.$store.commit('setIsLoading', false)

            toast({
              message: 'Account created, please log in!',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 5000,
              position: 'bottom-right',
            })
            
            this.$router.push('/login')
          })
          .catch(error => {
            toast({
              message: 'Something went wrong while sending the input fields to the backend, please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 5000,
              position: 'bottom-right',
            })

            this.$store.commit('setIsLoading', false)

            if (error.response) {
              console.log(JSON.stringify(error.response.data))
            } 
            else if (error.message) {
              console.log(JSON.stringify(error))
            }
          })
      } else {
        for (let error in this.errors) {
          toast({
            message: this.errors[error],
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 5000,
            position: 'bottom-right',
          })
        }
      }

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
    passwordStrengthChecker () {
      let password = this.password1
      let username = this.username
      let email = this.email

      let strongPassword = new RegExp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})')
      let mediumPassword = new RegExp('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))')

      if (this.getSimilarity(username, password) + this.getSimilarity(email, password) === 2) {
        this.passwordStrength = 'Password is the same as Username and Email, please change it.'
      }
      else if (this.getSimilarity(username, password) === 1) {
        this.passwordStrength = 'Password is the same as Username, please change it.'
      }
      else if (this.getSimilarity(email, password) === 1) {
        this.passwordStrength = 'Password is the same as Email, please change it.'
      }
      else if (username.includes(password) && password !== '' || password.includes(username) && username !== '' || this.getSimilarity(username, password) >= 0.5) {
        this.passwordStrength = 'Password is too similar to Username, please change it.'
      }
      else if (email.includes(password) && password !== '' || password.includes(email) && email !== '' || this.getSimilarity(email, password) >= 0.5) {
        this.passwordStrength = 'Password is too similar to Email, please change it.'
      }
      else if (strongPassword.test(password) && this.getSimilarity(username, password) <= 0.1 && this.getSimilarity(email, password) <= 0.1) {
        this.passwordStrength = 'Very Strong'
      } 
      else if (strongPassword.test(password)) {
        this.passwordStrength = 'Strong'
      }
      else if (mediumPassword.test(password)) {
        this.passwordStrength = 'Moderate'
      }
      else {
        this.passwordStrength = 'Weak'
      }
    },
    getSimilarity(s1, s2) {
      // based on Levenshtein distance
      let longer = s1;
      let shorter = s2;
      if (s1.length < s2.length) {
        longer = s2;
        shorter = s1;
      }
      let longerLength = longer.length;
      if (longerLength == 0) {
        return 1.0;
      }
      return (longerLength - this.editDistance(longer, shorter)) / parseFloat(longerLength);
    },
    editDistance(s1, s2) {
      s1 = s1.toLowerCase();
      s2 = s2.toLowerCase();

      let costs = new Array();
      for (let i = 0; i <= s1.length; i++) {
        let lastValue = i;
        for (let j = 0; j <= s2.length; j++) {
          if (i == 0)
            costs[j] = j;
          else {
            if (j > 0) {
              let newValue = costs[j - 1];
              if (s1.charAt(i - 1) != s2.charAt(j - 1))
                newValue = Math.min(Math.min(newValue, lastValue),
                  costs[j]) + 1;
              costs[j - 1] = lastValue;
              lastValue = newValue;
            }
          }
        }
        if (i > 0)
          costs[s2.length] = lastValue;
      }
      return costs[s2.length];
    }
  }
}
</script>

<style scoped>
#contents {
  color: #000;
  overflow-x: hidden;
  height: 100%;
  background-repeat: no-repeat;
  text-align: left;
}

#contents a {
  color: #000;
}

.card0 {
  box-shadow: 0px 4px 8px 0px #757575;
  border-radius: 20px;
}

.card1 {
  border-bottom-left-radius: 20px;
  border-top-left-radius: 20px;
  background: rgb(43, 42, 42);
  height: 100%;
  color: #fff;
  padding-left: 13%;
  padding-right: 13%;
}

.logo {
  margin-top: 30px;
  margin-left: 15px;
  cursor: pointer;
  text-decoration: none;
}

.card2 {
  border-bottom-right-radius: 20px;
  border-top-right-radius: 20px;
}

.social-connect .fa-home {
  color: #df4b37;
  padding: 10px 12px;
  font-size: 20px;
}

.social-connect .fa-facebook-square {
  color: #3b5998;
  padding: 10px 15px;
  font-size: 20px;
}

.social-connect {
  padding: 3px 0px 3px 3px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid #e0e0e0;
}

.social-connect:hover {
  background-color: blue;
}

.line {
  height: 1px;
  width: 45%;
  background-color: #e0e0e0;
  margin-top: 10px;
}

.or {
  width: 10%;
}

.text-center {
  text-align: center;
}

.text-sm {
  font-size: 14px !important;
}

.label-required:after {
  content: " *";
  color: red;
}

.password-strength-checker {
  position: absolute;
  z-index: 10;
  top: 88px;
  left: 200px;
  white-space: nowrap;
}

.is-very-strong { 
  color: green;
}

.is-strong {
  color: #14f75d;
}

.is-moderate {
  color: #ffff00;
}

.is-weak {
  color: #ff2509;
}

.is-bad {
  color: #ff2509;
}

input {
  padding: 10px 12px 10px 12px;
  border: 1px solid lightgrey;
  border-radius: 10px;
  margin-bottom: 25px;
  margin-top: 2px;
  width: 100%;
  box-sizing: border-box;
  color: #2c3e50;
  font-size: 14px;
  letter-spacing: 1px;
}

input:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  border: 1px solid #512da8;
  outline-width: 0;
}

::placeholder {
  color: #eeeeee;
  opacity: 1;
}

:-ms-input-placeholder {
  color: #eeeeee;
}

::-ms-input-placeholder {
  color: #eeeeee;
}

button:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  outline-width: 0;
}

.btn-blue {
  background-color: #512da8;
  width: 100%;
  color: #fff;
  border-radius: 6px;
}

.btn-blue:hover {
  background-color: #311b92;
  color: #fff;
  cursor: pointer;
}

.card-0 {
  color: #311b92;
  background-color: #fff;
  border-radius: 20px;
  min-height: 352px;
  margin-top: 80px;
  padding: 30px;
}

.carousel-indicators {
  position: absolute;
  bottom: -100px;
  display: -webkit-box !important;
}

.carousel-indicators li {
  cursor: pointer;
  border-radius: 50% !important;
  width: 40px !important;
  height: 40px !important;
  opacity: 0.5;
  margin: 5px !important;
}

.carousel-indicators li.active {
  opacity: 1;
  width: 50px !important;
  height: 50px !important;
  margin-top: 0px !important;
  border: 2px solid #fff;
}

.carousel-indicators li#li1 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-group-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li2 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li3 {
  background: url("https://icons.iconarchive.com/icons/grafikartes/adobe-cc/128/CC-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li4 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li5 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.profile-pic {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: absolute;
  top: -50px;
  left: calc(50% - 50px);
}

.content {
  color: #000;
  font-size: 14px;
}

.social {
  margin-top: 150px;
}

</style>
