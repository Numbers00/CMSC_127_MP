<template>
<div class='d-flex flex-row' style='justify-content: space-around;'>
    <div class='addpage-body d-flex flex-column col-4'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center; border-radius: 10px 0 0 10px;'>Add</h1>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center; border-radius: 0 10px 10px 0;'>Card</h2>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='left-section'>
        <form v-on:submit.prevent='addCard'>
          <div class='field d-flex flex-row'>
            <label class='label'>Name</label>
            <div class='control'>
              <input class='input' type='text' v-model='name' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Description</label>
            <div class='control'>
              <input class='input' type='text' v-model='description'>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Image</label>
            <div class='control'>
              <input class='input' type='text' v-model='image'>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Marked</label>
            <div class='select'>
              <select v-model='isMarked' required>
                <option value='Yes' selected='selected'>Yes</option>
                <option value='No'>No</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Visible </label>
            <div class='select'>
              <select v-model='isVisible' required>
                <option value='Yes'>Yes</option>
                <option value='No' selected='selected'>No</option>
              </select>
            </div>
          </div>

          <div class="notification is-danger mt-4" v-if="addErrors.length">
            <p v-for="addError in addErrors" :key="addError">{{ addError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button add-button' id='add-card-button'><span class='btn btn-success' style='min-width: 100%; position: absolute;'>Add Card</span></button>
            </div>
          </div>
        </form>

      </section>
    </div>

    <div class='addpage-body d-flex flex-column col-4'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center; border-radius: 10px 0 0 10px;'>Remove</h1>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center; border-radius: 0 10px 10px 0;'>Card</h2>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='right-section'>
        <form v-on:submit.prevent='removeCard'>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Target</label>
            <div class='select'>
              <select v-model='targetID' required>
                  <option v-for='activeCard in activeCards' :value='activeCard.id' :key='activeCard.id'>{{activeCard.name}}</option>
              </select>
            </div>
          </div>
          
          <div class="notification is-danger mt-4" v-if="removeErrors.length">
            <p v-for="removeError in removeErrors" v-bind:key="removeError">{{ removeError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button remove-button' id='remove-card-button'><span class='btn btn-danger' style='min-width: 100%; position: absolute;'>Remove Card</span></button>
            </div>
          </div>
        </form>
      </section>
    </div>
    
    <div class='addpage-body d-flex flex-column col-4'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center; border-radius: 10px 0 0 10px;'>Update</h1>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center; border-radius: 0 10px 10px 0;'>Card</h2>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='left-section'>
        <form v-on:submit.prevent='updateCard'>
          <div class='field d-flex flex-row'>
            <label class='label select-label'>Target</label>
            <div class='select'>
              <select v-model='targetID' required>
                  <option v-for='activeCard in activeCards' :value='activeCard.id' :key='activeCard.id'>{{activeCard.name}}</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Name</label>
            <div class='control'>
              <input class='input' type='text' v-model='name' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Description</label>
            <div class='control'>
              <input class='input' type='text' v-model='description'>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Image</label>
            <div class='control'>
              <input class='input' type='text' v-model='image'>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Marked</label>
            <div class='select'>
              <select v-model='isMarked' required>
                <option value='Yes' selected='selected'>Yes</option>
                <option value='No'>No</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Visible</label>
            <div class='select'>
              <select v-model='isVisible' required>
                <option value='Yes'>Yes</option>
                <option value='No' selected='selected'>No</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>History</label>
            <div class='select'>
              <select v-model='isHistory' required>
                <option value='Yes'>Yes</option>
                <option value='No' selected='selected'>No</option>
              </select>
            </div>
          </div>

          <div class="notification is-danger mt-4" v-if="updateErrors.length">
            <p v-for="updateError in updateErrors" :key="updateError">{{ updateError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button update-button' id='update-card-button'><span class='btn btn-info' style='min-width: 100%; position: absolute; color: white;'>Update Card</span></button>
            </div>
          </div>
        </form>

      </section>
    </div>

</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'ChangeSection',
  props: {
    activeCards: Array
  },
  data () {
    return {
      name: '',
      targetID: '',
      description: '',
      image: '',
      isMarked: '',
      isVisible: '',
      isHistory: '',
      addErrors: [],
      removeErrors: [],
      updateErrors: [],
      slug_checker: new RegExp(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)
    }
  },
  methods: {
    async addCard () {
      this.$store.commit('setIsLoading', true)

      this.removeErrors = []
      this.updateErrors = []

      if (this.name.length > 32) {
        this.addErrors.push("The Name Field's Maximum Length is 32!")
      }

      if (this.description.length > 500) {
        this.addErrors.push("The Name Field's Maximum Length is 500!")
      }

      if (!this.addErrors.length) {
        let isMarked = (this.isMarked === 'Yes' ? true : false)
        let isVisible = (this.isVisible === 'Yes' ? true : false)

        let image = this.image

        const randomBGs = [
          'https://danbooru.donmai.us/data/original/08/5e/__hanamaru_hareru_hanayori_jyoshiryou_drawn_by_wonderfullight__085e164ec249cc29100346d88e6500b0.jpg',
          'https://i1.sndcdn.com/artworks-6LfDj07xr8aByVAB-gvb87Q-t500x500.jpg',
          'https://danbooru.donmai.us/data/original/08/c3/08c37aa0e5f9766cef070fb61458f3d0.jpg',
          'https://i.ytimg.com/vi/TB48BAtygoU/maxresdefault.jpg',
          'https://danbooru.donmai.us/data/original/8d/ec/__hanamaru_hareru_hanayori_jyoshiryou_drawn_by_nichaokeai__8decae781ff176c8520ea112b49ef0d0.jpg',
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQigTOpSMgxtLKjVGkm_VN3uvIHL9oFw0fasQ&usqp=CAU'
        ]

        const randomBG = randomBGs[Math.floor(Math.random() * randomBGs.length)]

        if (image === '' || image === null) {
          image = randomBG
        }

        await axios({
        method: 'post',
        url: '/api/v1/cards/view/',
        data: {
          name: this.name,
          description: this.description,
          image: image,
          is_marked: isMarked,
          is_visible: isVisible,
          slug: this.slugify(this.name)
        }
        }).then(response => {
          this.addErrors = []

          this.$emit('resendGet')

          toast({
            message: 'The card was added to the database',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
          })
          this.targetID = ''
          this.name = ''
          this.description = ''
          this.image = ''
          this.isMarked = ''
          this.isVisible = ''
          this.isHistory = ''
        })
        .catch(error => {
          console.log(error)
        })

        this.$store.commit('setIsLoading', false)
      }

      this.$store.commit('setIsLoading', false)
    },
    async removeCard () {
      this.$store.commit('setIsLoading', true)

      this.addErrors = []
      this.updateErrors = []

      if (this.name.length > 32) {
        this.removeErrors.push("The Name Field's Maximum Length is 32!")
      }

      if (!this.removeErrors.length) {

        await axios({
          method: 'delete',
          url: '/api/v1/cards/view/',
          data: {
            target_card_id: this.targetID
          }
        }).then(response => {
          this.removeErrors = []

          this.$emit('resendGet')

          toast({
                message: 'The card was removed from the database',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'bottom-right',
          })
          this.targetID = ''
          this.name = ''
          this.description = ''
          this.image = ''
          this.isMarked = ''
          this.isVisible = ''
          this.isHistory = ''
        })
        .catch(error => {
          console.log(error)
        })

        this.$store.commit('setIsLoading', false)
      }

      this.$store.commit('setIsLoading', false)
    },
    async updateCard () {
      this.$store.commit('setIsLoading', true)

      this.addErrors = []
      this.removeErrors = []

      if (this.name.length > 32) {
        this.updateErrors.push("The Name Field's Maximum Length is 32!")
      }

      if (!this.updateErrors.length) {
        let isMarked = (this.isMarked === 'Yes' ? true : false)
        let isVisible = (this.isVisible === 'Yes' ? true : false)
        let isHistory = (this.isHistory === 'Yes' ? true : false)

        let image = this.image

        const randomBGs = [
          'https://danbooru.donmai.us/data/original/08/5e/__hanamaru_hareru_hanayori_jyoshiryou_drawn_by_wonderfullight__085e164ec249cc29100346d88e6500b0.jpg',
          'https://i1.sndcdn.com/artworks-6LfDj07xr8aByVAB-gvb87Q-t500x500.jpg',
          'https://danbooru.donmai.us/data/original/08/c3/08c37aa0e5f9766cef070fb61458f3d0.jpg',
          'https://i.ytimg.com/vi/TB48BAtygoU/maxresdefault.jpg',
          'https://danbooru.donmai.us/data/original/8d/ec/__hanamaru_hareru_hanayori_jyoshiryou_drawn_by_nichaokeai__8decae781ff176c8520ea112b49ef0d0.jpg',
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQigTOpSMgxtLKjVGkm_VN3uvIHL9oFw0fasQ&usqp=CAU'
        ]

        const randomBG = randomBGs[Math.floor(Math.random() * randomBGs.length)]

        if (image === '' || image === null) {
          image = randomBG
        }

        await axios({
        method: 'put',
        url: '/api/v1/cards/view/',
        data: {
          target_card_id: this.targetID,
          name: this.name,
          description: this.description,
          image: image,
          is_marked: isMarked,
          is_visible: isVisible,
          is_history: isHistory,
          slug: this.slugify(this.name)
        }
        }).then(response => {
          this.updateErrors = []

          this.$emit('resendGet')

          this.targetID = ''
          this.name = ''
          this.description = ''
          this.image = ''
          this.isMarked = ''
          this.isVisible = ''
          this.isHistory = ''
          
          toast({
            message: 'The card was updated in the database',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
          })
        })
        .catch(error => {
          console.log(error)
        })

        this.$store.commit('setIsLoading', false)
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
  }
}
</script>

<style scoped>
.addpage-body {
  position: relative;
  top: 20px;
}
.black-section {
  min-height: 500px;
  max-height: 500px;
  padding: 20px;
}
#left-section {
  min-height: 0;
}
.field {
  min-width: 100%;
  margin-bottom: 20px;
}
.image-field {
  margin-bottom: 20px;
}
.label {
  background-color: hsl(0, 0%, 21%);
  min-height: 30px;
  max-height: 30px;
  min-width: 25%;
  padding: 5px 5px 5px 5px;
  color: white;
  text-align: center;
  border-radius: 10px 0 0 10px;
}
.select-label {
  min-height: 40px;
  max-height: 40px;
}
.input,  .select, select, option {
  border-radius: 0 10px 10px 0;
  min-width: 320px;
  background-color: #eeeeee;
}
.input {
  max-height: 30px;
}
.add-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 10px;
}
.remove-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 10px;
}
.update-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 10px;
}
</style>