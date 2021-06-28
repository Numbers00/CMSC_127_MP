<template>
<div class="board">

	<h3 class="board-title">{{board.name}}</h3>

	<ul class="board-items">
		<li v-for="task in tasks" :key="task">
      {{task.name}}
		</li>
	</ul>

	<div class="add-task">
        <input 
          class='input input-task' 
          placeholder="Add a task..." 
          type='text' 
          v-model='newTask'
          v-on:keyup.enter='addTask'
        >
    </div>
</div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
    name: 'BoardBox',
    props: {
        board: {},
        tasks: []
    },
    data () {
      return {
        newTask: ''
      }
    },
    methods: {
      async addTask () {
        this.$store.commit('setIsLoading', true)

        await axios({
        method: 'post',
        url: '/api/v1/tasks/view/',
        data: {
          board: this.board.name,
          name: this.newTask,
          description: '',
          is_marked: false,
          status: 'todo',
          slug: this.slugify(this.name)
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
	word-wrap: break-word;
	cursor: pointer;
}

.board-items li:last-of-type {
	margin-bottom: 0;
}

.board-items li:hover {
	background-color: #eee;
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

::placeholder {
    color: white;
}
</style>