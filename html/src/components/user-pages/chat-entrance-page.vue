
<style scoped>
.enter-page {
	background-color: #EEFFFF;
}
.enter-header {
	height: 40%;
	background-color: #32314D;
	color: white;
	text-align: center;
}

.enter-header h3, .enter-header p {
	position: relative;
	top: 40%;
}

.enter-input {
	position: relative;
	top: -30px;
	left: 7%;
	z-index: 9889;
}

.enter-input input {
	padding-left: 15px; 
	display: inline-block;
	height: 50px;
	width: 80%;
	background-color: white;
	border-radius: 10px;
	border-color: #F2F2EF;	
}

.enter-input span {
	display: block;
	color: #C8C3BF;
}

.enter-chat {
	margin-top: 20%;
	margin-bottom: 20%
}
.enter-chat button {
	display: block;
	margin: 0 auto -20% auto;
	height: 40px;
	width: 80%;
	background-color: #4A90E2;
	color: white;
}
</style>

<template>
	<div class="view-page enter-page">
		<div class="enter-header">
			<h3>{{room.name}}</h3>
			<p>{{room.start_time | date}}</p>
			<p>{{room.end_time | date}}</p>
		</div>

		<div class="enter-input">
			<input class="weui_input" title="" v-model="username" placeholder="给自己起个名字吧">
			<span>好的名字容易让人记住</span>
		</div>

		<div class="enter-chat">
			<button class="weui_btn" @click="getName">进入聊天</button>
		</div>
	</div>
</template>

<script>
import {XButton, XInput} from 'vux'
import { setName, setId, receiveMessages, receiveMembers, setCurRoom } from './../../vuex/actions'
import { getCurRoom } from './../../vuex/getters'
import { networkApi } from './../../api/networkApi'
import { util } from './../../api/util'

export default {
	data() {
		return {
			username: ''
/*			room: {
				name: '123123',
				start_time: 1463939797682,
				end_time: 1463939797682
			}*/
		}
	},
	filters: {
		date: (value) => {
			var time = new Date(parseInt(value));
			var str = "" + (time.getMonth() + 1) + '月' + time.getDate() + '日' + "  " + time.toLocaleString().substr(-11);
			console.log('computed')
			return str;
		}
	},
	methods: {
		getName: function() {
			console.log(this.username)
			if(this.username !== "" && this.$route.params.room_id) {
				var data = {
					nick_name : this.username,
					room_id: this.$route.params.room_id
				}
				networkApi.getRoom(this, 'GET', this.$route.params.room_id)
					.then(() => { 
						return networkApi.createName(this, 'POST', data)
					})
					.then(() => {
						return networkApi.getMembers(this, 'GET', this.$route.params.room_id);
					})
					.then(() => {
						return networkApi.getMessages(this, 'GET', this.$route.params.room_id, 100);
					})
					.then(() => {
						console.log('router');
						router.go({name: 'room', params: {room_id: this.$route.params.room_id}});
					})
					.catch((err) => {
						console.log(err);
					})
			}
		}
	},
	components: {
		XButton,
		XInput
	},
	vuex: {
		getters: {
			room: getCurRoom
		},
		actions: {
			setName,
			setId,
			receiveMessages, 
			receiveMembers,
			setCurRoom
		}
	},
	created: function() {
		networkApi.getRoom(this, 'GET', this.$route.params.room_id)
			.catch((err) => {
				console.log(err);
			})
	},
	ready() {
		//cookie暂时不考虑,messages, members, id, name
		console.log('chat-entrance')
		if(this.$route.params.room_id) {
			console.log(this.$route.params.room_id);
			//getName如果成功的话，表明是有cookie的
			networkApi.getName(this, 'GET',this.$route.params.room_id)
				.then(() => {
					return networkApi.getMembers(this, 'GET', this.$route.params.room_id)
				})
				.then(() => {
					return networkApi.getMessages(this, 'GET', this.$route.params.room_id, 100);
				})
				.then(() => {
					//成功直接跳到聊天界面
					router.go({name: 'room', params: {room_id: this.$route.params.room_id}})
				})
				.catch((err) => {
					console.log(err)
				})
		}
	}
}
</script>