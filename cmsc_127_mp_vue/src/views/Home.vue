<template>
<div class="home">
  <TopSection viewType="Home" />
  <router-link to='/your-cards' class='button is-success col-12' style="color: white; border-radius: 10px; padding: 6px; margin-bottom: 0; position: relative; bottom: 20px;" id='update-button'>
    Check Your Cards Here
  </router-link>
  <swiper id='top-cards-swiper' v-if="activeCards.length !== 0" class="swiper mt-5" style="height: 300px" :options="swiperOption">
      <swiper-slide
        v-for="(card, index) in activeCards"
        :key="index"
      >
        <CardBox
          :card="card"
          :myDetails="myDetails"
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
            :myDetails="myDetails"
            v-on:resendGet="resendGet"
          />
        </swiper-slide>
      </template>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>

  <!-- Title -->
  <div class="wrapper" style="background: hsl(0, 0%, 21%); border-radius: 10px; position: relative; bottom: 15px;">
    <div class="container-fluid">
        <div class="row welcome text-center">
            <div class="col-12">
                <h1 class="display-4" id="minishop_title">JOINING PERKS</h1>
            </div>
        </div>
    </div>
    <!-- MINISHOP ITEMS -->
    <div class="container-fluid">
        <div class="row padding">
            <!-- Card 1 -->
            <div class="col-md-4">
                <div class="col-12 card" style="background-color: #d4af37;">
                    <img class="card-img-top" src="">
                    <div class="card-body">
                        <h4 class="card-title">Plans</h4>
                        <p class="card-text">We offer very low prices for our services, come check them out in detail here!</p>
                        <br>
                        <a @click="$router.push('/plans')" class="btn-j btn btn-j btn-outline-secondary">View More</a>
                    </div>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="col-md-4">
                <div class="col-12 card" style="background-color: #d4af37;">
                    <img class="card-img-top" src="">
                    <div class="card-body">
                        <h4 class="card-title">Care & Tools</h4>
                        <p class="card-text">Even with a free plan you'll get the whole experience from our site, premium is optional!</p>
                        <a @click="$router.push('/your-cards')" class="btn-j btn btn-j btn-outline-secondary">View More</a>
                    </div>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="col-md-4">
                <div class="col-12 card" style="background-color: #d4af37;">
                    <img class="card-img-top" src="">
                    <div class="card-body">
                        <h4 class="card-title">Community</h4>
                        <p class="card-text">Come see what other users are doing and chat with our friendly community members!</p>
                        <br>
                        <a @click="$router.push('/global')" class="btn-j btn btn-j btn-outline-secondary">View More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <hr class="my-4" id="welcome_hr">

    <!-- WELCOME SECTION -->
    <div class="container-fluid padding" id="welcome">
        <div class="row welcome text-center">
            <div class="col-12">
                <h1 class="display-4">COME PLAN WITH US!</h1>
            </div>
            <div class="col-12">
                <p class ="lead">A goal without a plan is just a wish - Antoine de Saint-Exupéry</p>
            </div>
        </div>
    </div>
    <hr class="my-4">
    <!-- WELCOME SECTION ITEMS -->
    <div class="container-fluid padding" id="welcome_items">
        <div class="row text-center padding">
            <div class="col-xs-12 col-sm-6 col-md-4">
                <i class="fas fa-seedling"></i>
                <h3>GROW</h3>
                <p>Relationships define the quality of your life. We're here to nurture connections between people and make a place for each to thrive.</p>
            </div>
            <div class="col-xs-12 col-sm-6 col-md-4">
                <i class="fas fa-leaf"></i>
                <h3>LIVE</h3>
                <p>Planning comes with life, in each and every moment our minds make decisions faster than we realize, come harness planning to its full potential.</p>
            </div>
            <div class="col-sm-12 col-md-4">
                <i class="fas fa-globe-asia"></i>
                <h3>HELP</h3>
                <p>Cultivating our spaces - both in our personal and communal lives, allow us to maximize our potential and help others in doing so.</p>
            </div>
        </div>
        <hr class="my-4">
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.min.css'

import TopSection from '@/components/TopSection.vue'
import CardBox from '@/components/CardBox.vue'

export default {
  name: 'Home',
  components: {
    Swiper,
    SwiperSlide,
    TopSection,
    CardBox
  },
  data () {
    return {
      activeCards: [],
      myDetails: {},
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
  mounted () {
    this.getActiveCards()
    this.getMyDetails()

    document.title = 'Home | Synergy'
  },
  watch: {
    myDetails () {
      console.log(this.myDetails)
    }
  },
  methods: {
    resendGet () {
      this.activeCards = []

      this.getActiveCards()

      this.$emit('resendGet')
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
    async getMyDetails () {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('api/v1/users/')
        .then(response => {
          console.log(response.data[0])
          this.myDetails = response.data[0]
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
#top-cards-swiper {
  width: 100%;
  position: relative;
  background: #A0A0A0;
  min-height: 180px;
  max-height: 180px;
  height: 180px;
  border-radius: 10px;
  bottom: 30px;
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
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,700');

/* HANDLE USER */
nav span{
  position:sticky;
  font-size: 1.1em;
  color:#636e5a;
  top: 26px;
}

/* CAROUSEL */
.carousel-inner img{
  margin: auto;
  width: 100%;
  height: 100%;
}
.carousel-caption{
  margin: auto;
  position:absolute;
  top: 53%;
  transform: translateY(-60%);
  text-align:right;
  text-shadow: 5px 10px 10px #31352E;
}
.carousel-caption h1{
  font-family: "Berlin Sans FB Demi Bold", sans-serif;
  font-size: 650%;
}
.carousel-caption h3{
  font-size: 200%;
  font-weight: 500;
  padding-bottom: 1rem;
}
#carousel-caption-2{
  margin: auto;
  position:absolute;
  top: 50%;
  transform: translateY(-60%);
  color: #31352E;
  text-align:left;
}
#carousel-caption-2 h1{
  font-family: "Berlin Sans FB Demi Bold", sans-serif;
  font-size: 650%;
  text-shadow: none;
}
#carousel-caption-2 h3{
  font-size: 200%;
  font-weight: 500;
  padding-bottom: 1rem;
  text-shadow: none;
}
#carousel-caption-3{
  margin: auto;
  position:absolute;
  top: 53%;
  transform: translateY(-60%);
  color: #31352E;
  text-align:right;
}
#carousel-caption-3 h1{
  font-family: "Berlin Sans FB Demi Bold", sans-serif;
  font-size: 650%;
  text-shadow: none;
}
#carousel-caption-3 h3{
  font-size: 200%;
  font-weight: 500;
  padding-bottom: 1rem;
  text-shadow: none;
}
.carousel-control-prev:hover{
  background-color: rgba(220,220,220, 0.3);
}
.carousel-control-next:hover{
  background-color: rgba(220,220,220, 0.3);
}
.btn-j{
  font-size: 125%;
  position:relative;
  color: white;
  font-weight: 200;
  background-color: #708238;
  border: 1px solid #677933;
  filter: drop-shadow(0px 3px 5px #31352E);
}
.btn-j:hover{
  top: -3px;
  background-color: rgba(112,130,56, 0.8);
  color: white;
}
#start-btn-j{
  padding: 8px 18px;
}
#browse-btn-j{
  padding: 8px 16px;
}
#offer-btn-j{
  padding: 8px 22px;
}
#sign-up-btn-j{
  padding: 8px 40px;
}

/* MINISHOP */
.display-4{
  position:relative;
  font-family: "Berlin Sans FB Demi Bold", "sans serif";
  font-size: 75px;
  top:20px;
}
.card-title{
  font-family: "Berlin Sans FB Demi Bold", "sans serif";
  font-size: 30px;
}
.card-text{
  font-size: 20px;
  text-align: justify;
  text-justify: inter-word;
}
#minishop_hr{
  padding-bottom:3rem;
  color: white;
}
#minishop_title{
  padding-bottom:1.5rem;
}

/* WELCOME */
.card{
  width: 100%;
  height: 100%;
}
#welcome p{
  font-size: 35px;
}
#welcome_items p{
  font-size: 20px;
  text-align: justify;
  text-justify: inter-word;
}
.fa-seedling, .fa-leaf, .fa-globe-asia{
  color: #708238;
  font-size: 4em;
  margin: 1rem;
}
#welcome_hr{
  padding-bottom:3rem;
  color: white;
}

/* FOOTER */
footer{
  background-color: #D1E2C4;
  filter: drop-shadow(0px 3px 5px #31352E);
  padding-top: 2rem;
}
footer div{
  color:#31352E;
  font-size: 20px;
}
footer h5{
  font-weight: bold;
}
hr.light{
  border-top: 1px solid black;
  width: 80%;
  margin-top: .8rem;
  margin-bottom: 1rem;
  margin-left: 3rem;
}
hr.light-100{
  border-top: 1px solid black;
  width: 100%;
  margin-top: .8rem;
  margin-bottom: 1rem;
}
.footer-logo{
  width: 60%;
  height:auto;
}
#logo-text{
  font-weight:bold;
}
.navigation a{
  text-decoration: none;
}
.navigation a:link{
  color: #6b4112;
}
.navigation a:hover{
  color: black;
}

/*---Media Queries --*/
@media (max-width: 1500px) {
  .btn-j {
    font-size: 110%;
  }
  .carousel-caption{
    margin: auto;
    top: 50%;
  }
  .carousel-caption h1{
    font-size: 575%
  }
  .carousel-caption h3{
    font-size: 170%
  }

  #carousel-caption-2{
    margin: auto;
    top: 48%;
  }
  #carousel-caption-2 h1{
    font-size: 575%
  }
  #carousel-caption-2 h3{
    font-size: 170%
  }


  #carousel-caption-3{
    margin: auto;
    top: 50%;
  }
  #carousel-caption-3 h1{
    font-size: 575%
  }
  #carousel-caption-3 h3{
    font-size: 170%
  }
}
@media (max-width: 1350px) {
  .carousel-caption{
    margin: auto;
    top: 48%;
  }
  .carousel-caption h1{
    font-size: 500%
  }
  .carousel-caption h3{
    font-size: 140%
  }

  #carousel-caption-2{
    margin: auto;
    top: 45%;
  }
  #carousel-caption-2 h1{
    font-size: 500%
  }
  #carousel-caption-2 h3{
    font-size: 140%
  }


  #carousel-caption-3{
    margin: auto;
    top: 48%;
  }
  #carousel-caption-3 h1{
    font-size: 500%
  }
  #carousel-caption-3 h3{
    font-size: 140%
  }
}
@media (max-width: 1080px) {
  .carousel-caption{
    margin: auto;
    top: 49%;
  }
  .carousel-caption h1{
    font-size: 490%
  }
  .carousel-caption h3{
    display: none;
  }

  #carousel-caption-2{
    margin: auto;
    top: 48%;
  }
  #carousel-caption-2 h1{
    font-size: 490%
  }
  #carousel-caption-2 h3{
    display: none;
  }


  #carousel-caption-3{
    margin: auto;
    top: 49%;
  }
  #carousel-caption-3 h1{
    font-size: 490%
  }
  #carousel-caption-3 h3{
    display: none;
  }

  .display-4{
    font-size: 55px;
  }
  #welcome p{
    font-size: 25px;
  }
}
@media (max-width: 875px) {
  .carousel-caption{
    margin: auto;
    top: 47%;
  }

  #carousel-caption-2{
    margin: auto;
    top: 46%;
  }

  #carousel-caption-3{
    margin: auto;
    top: 47%;
  }

  #start-btn-j{
    padding: 6px 16px;
  }
  #browse-btn-j{
    padding: 6px 14px;
  }
  #offer-btn-j{
    padding: 6px 20px;
  }
  #sign-up-btn-j{
    padding: 6px 38px;
  }
}
@media (max-width: 750px) {
  .carousel-caption{
    margin: auto;
    top: 42%;
  }

  #carousel-caption-2{
    margin: auto;
    top: 41%;
  }

  #carousel-caption-3{
    margin: auto;
    top: 42%;
  }
}
  
  
  
  
  /*
  Extra small (xs) devices (portrait phones, less than 576px)
  No media query since this is the default in Bootstrap
  
  Small (sm) devices (landscape phones, 576px and up)
  @media (min-width: 576px) { ... }
  
  Medium (md) devices (tablets, 768px and up)
  @media (min-width: 768px) { ... }
  
  Large (lg) devices (desktops, 992px and up)
  @media (min-width: 992px) { ... }
  
  Extra (xl) large devices (large desktops, 1200px and up)
  @media (min-width: 1200px) { ... }
  */
</style>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,700');

@font-face {
  font-family: 'Berlin Sans FB Demi Bold';
  font-style: normal;
  font-weight: normal;
  src: local('Berlin Sans FB Demi Bold');
}

/* NAVBAR CSS */
.navbar{
  background-color: #D1E2C4;
  padding: .5rem;
  top:10;
  filter: drop-shadow(0px 3px 5px #31352E);
}
.navbar-brand{
  margin-left: 20px;
}
.navbar-nav li{
  padding-right: 14px;
}
#nav-link-each-active{
  position: relative;
  color: #31352E;
}
#nav-item #nav-link-each, #dropdown #navbarDropdown{
  position: relative;
  color: #636e5a;
}
#nav-item #nav-link-each:hover,#nav-item #nav-link-each-active:hover, #dropdown:hover #navbarDropdown{
  top: -3px;
  color: #31352E;
}
.nav-link{
  padding: 17px 14px;
  font-size: 1.4em !important;
}
.navbar-toggler{
  margin-right: 20px;
}
.navbar-collapse{
  margin-right: 20px;
  padding-left: 40px;
}

/* ICONS */
.fa-store-alt{
  padding-right: 0.6rem;
}
.fa-store{
  padding-right: 0.7rem;
}
.fa-user-circle{
  padding-right: 0.2rem;
}
.fa-sign-out-alt{
  padding-right: 0.5rem;
}
.fa-user-alt{
  color: #31352E;
  margin-left: 2px;
  padding-right: 0.6rem;
}
.fa-user-edit{
  color: #31352E;
  margin-left: 2px;
  padding-right: 0.36rem;
}
/* .fa-history{
  color: #31352E;
  margin-left: 1.5px;
  padding-right: 0.66rem;
} */
.fa-shopping-cart{
  color: #31352E;
  margin-left: 0.7px;
  padding-right: 0.53rem;
}
.fa-sign-in-alt{
  color: #31352E;
  margin-left: 3.8px;
  padding-right: 0.54rem;
}
.fa-user-plus{
  color: #31352E;
  margin-left: 3.6px;
  padding-right: 0.215rem;
}


/* DROPDOWN (ACCOUNT) */
#dropdown{
  float: left;
}
#dropdown #navbarDropdown{
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}
.dropdown-menu{
  font-size: 18px;
  display: none;
  position: absolute;
  background-color: #f5f5f5;
  min-width: 190px;
  box-shadow: 0px 2px 4px 0px #333;
}
.dropdown-menu a{
  float: none;
  color:#31352E;
  padding: 14px 18px;
  text-decoration: none;
  display: block;
  text-align: left;
}
.dropdown-menu a:hover{
  background-color: #ddd;
}
#dropdown:hover .dropdown-menu{
  display:block;
}

/*---Media Queries --*/
@media (max-width: 818px) {
  .navbar-brand{
    margin-left: 15px;
  }
  .nav-link{
    padding: 13px 10px;
    font-size: 1.3em !important;
  }
}
@media (max-width: 768px) {
}
@media (max-width: 576px) {
}

/*---Firefox Bug Fix --*/
.carousel-item {
  transition: -webkit-transform 0.5s ease;
  transition: transform 0.5s ease;
  transition: transform 0.5s ease, -webkit-transform 0.5s ease;
  -webkit-backface-visibility: visible;
  backface-visibility: visible;
}
/*--- Fixed Background Image --*/
figure {
  position: relative;
  width: 100%;
  height: 60%;
  margin: 0!important;
}
.fixed-wrap {
  clip: rect(0, auto, auto, 0);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
#fixed {
  background: hsl(0, 0%, 21%) !important;
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
  will-change: transform;
}
/*--- Bootstrap Padding Fix --*/
[class*="col-"] {
    padding: 1rem;
}

/*
Extra small (xs) devices (portrait phones, less than 576px)
No media query since this is the default in Bootstrap

Small (sm) devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

Medium (md) devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

Large (lg) devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

Extra (xl) large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
*/

</style>