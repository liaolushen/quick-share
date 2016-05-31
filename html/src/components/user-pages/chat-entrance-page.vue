<template>
	<div class="view-page enter-page">
		<div class="enter-header">
			<h3>{{room.room_name}}</h3>
			<p>{{start_time}}</p>
			<p>{{end_time}}</p>
		</div>

		<div class="enter-input">
			<input class="weui_input" title="" :value.sync="username" placeholder="给自己起个名字吧">
			<span>好的名字容易让人记住</span>
		</div>

		<div class="enter-chat">
			<button class="weui_btn" @click="getName">进入聊天</button>
		</div>
	</div>
</template>

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
	margin-top: 40%;
}
.enter-chat button {
	display: block;
	margin: 0 auto;
	height: 40px;
	width: 80%;
	background-color: #4A90E2;
	color: white;
}
</style>

<script>
import {XButton, XInput} from 'vux'
import { setName, setId, setMessages, setMembers, setCurRoom } from './../../vuex/actions'
import { getCurRoom } from './../../vuex/getters'
import { networkApi } from './../../api/networkApi'


export default {
	data() {
		return {
			groupName: '2016国际体验设计大会',
			time: '6月20日 10:00~16:00',
			username: ''
		}
	},
	methods: {
		//cookie暂时不考虑
		getName: function() {
			if(this.username !== "" && $route.params.room_id) {
				var data = {
					nick_name : this.username,
					room_id: $route.params.room_id
				}
				networkApi.getRoom(this, 'Post', $route.params.room_id)
					.then(() => { 
						return networkApi.createName(this, 'POST', data)
					})
					.then(() => {
						return networkApi.getMembers(this, 'GET', $route.params.room_id);
					})
					.then(() => {
						return networkApi.getMessages(this, 'GET', $route.params.room_id, 100);
					})
					.then(() => {
						router.go({name: 'room', params: {room_id: $route.params.room_id}});
					})
					.catch((err) => {
						console.log(err);
					})
			}
		}
	},
	computed: {
		start_time: () => {
			var start = new Date(this.room.start_time);
			var str_start = "" + (start.getMonth() + 1) + '月' + start.getDate() + '日' + "  " + start.toLocaleString().substring(0,5);
			return str_start;
		},
		end_time: () => {
			var end = new Date(this.room.end_time);			
			var str_end = "" + (end.getMonth() + 1) + '月' + end.getDate() + '日' + "  " + end.toLocaleString().substring(0,5);
			return str_end;
		}
	},
	components: {
		XButton,
		XInput
	},
	vuex: {
		getters: {
			room: getCurRoom,
		},
		actions: {

		}
	},
	created: function() {
		networkApi.getRoom(this, 'GET', $route.params.room_id)
			.catch((err) => {
				console.log(err);
			})
	},
	ready() {
		//cookie暂时不考虑,messages, members, id, name
		if($route.params.room_id) {
			console.log($route.params.room_id);
			//getName如果成功的话，表明是有cookie的
			networkApi.getName(this, 'GET',$route.params.room_id)
				.then(() => {
					return networkApi.getMembers(this, 'GET', $route.params.room_id)
				})
				.then(() => {
					return networkApi.getMessages(this, 'GET', $route.params.room_id, 100);
				})
				.then(() => {
					//成功直接跳到聊天界面
					router.go({name: 'room', params: {room_id: $route.params.room_id}})
				})
				.catch((err) => {
					console.log(err)
				})
		}
	}
}
</script>