<template>
<div class="board">

  <div 
    class="board-title-div is-fullwidth d-flex flex-row" 
    style="justify-content: space-between;"
    @click="selectBoard(board)"
  >
    <div class="change-board">
      <input 
        class='input input-board' 
        :placeholder="board.name" 
        type='text' 
        v-model='newBoard'
        v-on:keyup.enter='!card.is_history ? (isEmpty ? addBoard(newBoard) : changeBoardName(newBoard)) : historyError'
        ref="inputBoard"
      >
    </div>
    <span v-if="!isEmpty">
    <i 
      class="times-icon fa fa-times is-size-3 mr-3 mt-3" 
      style='color: white;'
      @click="!card.is_history ? removeBoard(board.name) : historyError">
    </i>
    </span>
    <span v-else>
    <i 
      class="plus-icon fa fa-plus is-size-3 mr-3 mt-3" 
      style='color: white;'
      @click="$refs.inputBoard[0].focus()">
    </i>
    </span>
  </div>

	<ul class="board-items">
    <template v-for="task in tasks">
		  <li 
        class="d-flex flex-row" 
        style="justify-content: space-between;"
        v-if="task.is_marked && task.status === 'todo'"
        :key="task.id"
        @click="selectTask(task)"
      >
        {{task.name}}
        <div class="d-flex flex-row">
          <i class="far fa-circle"
            @click="!card.is_history ? markTask(task) : historyError"
            v-if="!task.is_marked"
          >
          </i>
          <i 
            class="fas fa-circle"
            @click="!card.is_history ? markTask(task) : historyError"
            v-if="task.is_marked"
          >
          </i>
          <i 
            class="times-icon fa fa-times ml-2" 
            aria-hidden="true" 
            @click="!card.is_history ? finishTask(task) : historyError"
          >
        </i>
        </div>
		  </li>
    </template>
    <template v-for="task in tasks">
		  <li 
        class="d-flex flex-row" 
        style="justify-content: space-between;"
        v-if="!task.is_marked && task.status === 'todo'"
        :key="task.id"
        @click="selectTask(task)"
      >
        {{task.name}}
        <div class="d-flex flex-row">
          <i class="far fa-circle"
            @click="!card.is_history ? markTask(task) : historyError"
            v-if="!task.is_marked"
          >
          </i>
          <i 
            class="fas fa-circle"
            @click="!card.is_history ? markTask(task) : historyError"
            v-if="task.is_marked"
          >
          </i>
          <i 
            class="times-icon fa fa-times ml-2" 
            aria-hidden="true"
            @click="!card.is_history ? finishTask(task) : historyError"
          >
        </i>
        </div>
		  </li>
    </template>
	</ul>

	<div class="add-task">
    <input 
      class='input input-task' 
      placeholder="Add a task..." 
      type='text' 
      v-model='newTask'
      v-on:keyup.enter='!card.is_history ? addTask : historyError'
    >
  </div>

  <b-modal id="taskModal">
    Clicked {{selectedTask.name}}!
  </b-modal>
</div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
    name: 'BoardBox',
    props: {
      card: Object,
      board: Object,
      tasks: Array,
      isEmpty: Boolean
    },
    data () {
      return {
        newTask: '',
        newBoard: '',
        addBoardToggle: false,
        selectedTask: {}
      }
    },
    methods: {
      historyError () {
        toast({
          message: 'You are not allowed to edit history cards. You can try making the card active again in Your Cards by making History: No.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
      },
      selectTask (task) {
        console.log('task')
        this.$emit('selectTask', task, this.board)
      },
      selectBoard (board) {
        this.$emit('selectBoard', board)
      },
      async addTask () {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'post',
        url: '/api/v1/tasks/view/',
        data: {
          target_board_id: this.board.id,
          name: this.newTask,
          description: '',
          is_marked: false,
          status: 'todo',
          slug: this.slugify(this.newTask)
        }
        }).then(response => {
          toast({
            message: 'The task was added to the database',
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
              message: 'Something went wrong while uploading the new task. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right',
          })
        })
        this.$store.commit('setIsLoading', false)
      },
      async finishTask (task) {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'put',
        url: '/api/v1/tasks/view/',
        data: {
          target_task_id: task.id,
          target_board_id: this.board.id,
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
          this.newTask = ''

          this.$emit('resendGet')
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
      async markTask (task) {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'put',
        url: '/api/v1/tasks/view/',
        data: {
          target_task_id: task.id,
          target_board_id: this.board.id,
          name: task.name,
          description: task.description,
          is_marked: !task.is_marked,
          status: task.status,
          slug: this.slugify(task.name)
        }
        }).then(response => {
          toast({
            message: "The task's mark has been successfully changed",
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
              message: 'Something went wrong while removing the new task. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right',
          })
        })
        this.$store.commit('setIsLoading', false)
      },
      async addBoard () {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'post',
        url: '/api/v1/boards/view/',
        data: {
          target_card_id: this.card.id,
          name: this.newBoard,
          description: '',
          slug: this.slugify(this.newBoard)
        }
        }).then(response => {
          toast({
            message: 'The board was added in the database',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
          })
          this.newBoard = ''

          this.$emit('resendGet')
        })
        .catch(error => {
          console.log(error)
          toast({
              message: 'Something went wrong while adding the board. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right',
          })
        })
        this.$store.commit('setIsLoading', false)
      },
      async removeBoard () {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'delete',
        url: '/api/v1/boards/view/',
        data: {
          target_card_id: this.card.id,
          id: this.board.id
        }
        }).then(response => {
          toast({
            message: 'The board was removed from the database',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
          })
          this.newBoard = ''

          this.$emit('resendGet')
        })
        .catch(error => {
          console.log(error)
          toast({
              message: 'Something went wrong while removing the board. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right',
          })
        })
        this.$store.commit('setIsLoading', false)
      },
      async changeBoardName () {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'put',
        url: '/api/v1/boards/view/',
        data: {
          target_board_id: this.board.id,
          target_card_id: this.card.id,
          name: this.newBoard,
          description: '',
          slug: this.slugify(this.newBoard)
        }
        }).then(response => {
          toast({
            message: 'The board was updated in the database',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'bottom-right',
          })
          this.newBoard = ''

          this.$emit('resendGet')
        })
        .catch(error => {
          console.log(error)
          toast({
              message: 'Something went wrong while updating the board. Please try again.',
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
}
</script>

<style scoped>
.board {
	flex: 0 0 27rem;
	display: flex;
	flex-direction: column;
	background-color: hsl(0,0%,21%);
	max-height: calc(100vh - 11.8rem);
  min-width: 300px;
  max-width: 300px;
  width: 300px;
	border-radius: 0.3rem;
    margin-top: 20px;
}

.board:last-of-type {
	margin-right: 0;
}

.board-title {
	font-size: 1.4rem;
	font-weight: 700;
	color: white;
	padding: 1rem;
}

.board-items {
	flex: 1;
	display: flex;
	flex-direction: column;
	align-content: start;
	padding: 0 0.6rem 0.5rem;
	overflow-y: auto;
}

.board-items::-webkit-scrollbar {
	width: 1.6rem;
}

.board-items::-webkit-scrollbar-thumb {
	background-color: #c4c9cc;
	border-right: 0.6rem solid #e2e4e6;
}

.board-items li {
	font-size: 1rem;
	font-weight: 400;
	line-height: 1.3;
	background-color: #fff;
	padding: 0.65rem 0.6rem;
	color: #4d4d4d;
	border-bottom: 0.1rem solid #ccc;
	border-radius: 0.3rem;
	margin-bottom: 0.6rem;
  max-width: 300px;
  overflow: auto;
	cursor: pointer;
}

.board-items li:last-of-type {
	margin-bottom: 0;
}

.board-items li:hover {
	background-color: #eee;
}

.change-board {
	color: white;
	padding: 1rem;
	cursor: pointer;
  font-size: 1.4rem;
	font-weight: 700;
}

.change-board:hover {
	background-color: #A0A0A0;
	color: #4d4d4d;
	text-decoration: underline;
}

.add-task {
	font-size: 1rem;
	font-weight: 400;
	color: #838c91;
	padding: 1rem;
	cursor: pointer;
}

.add-task:hover {
	background-color: #A0A0A0;
	color: #4d4d4d;
	text-decoration: underline;
}

.add-board {
	flex: 0 0 27rem;
	font-size: 1.4rem;
	font-weight: 400;
	background-color: #006aa7;
	color: #a5cae0;
	padding: 1rem;
	border-radius: 0.3rem;
	cursor: pointer;
	transition: background-color 150ms;
}

.add-board:hover {
	background-color: #005485;
}

.input-task {
    background-color: hsl(0,0%,21%);
    border: none;
    color: white;
}

.input-board {
    background-color: hsl(0,0%,21%);
    width: 220px;
    height: 40px;
    border: none;
    color: white;
}

.input-board::placeholder {
  color: white;
  padding: 1rem;
	cursor: pointer;
  font-size: 1.4rem;
	font-weight: 700;
}

::placeholder {
    color: white;
}

.plus-icon:hover {
  cursor: pointer;
}

.times-icon:hover {
  cursor: pointer;
}
</style>