<template>
	<div class="view-page">
		<div class="enter-header">
			<h3>{{groupName}}</h3>
			<p>{{time}}</p>
		</div>

		<div class="enter-input">
			<input class="weui_input" title="" :value.sync="username" placeholder="给自己起个名字吧">
			<span>好的名字容易让人记住</span>
		</div>

		<div class="enter-chat">
			<button class="weui_btn" @click="setName">进入聊天</button>
		</div>
	</div>
</template>

<style scoped>
.view-page {
	width: 100%;
	height: 100%;
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

export default {
	data() {
		return {
			groupName: '2016国际体验设计大会',
			time: '6月20日 10:00~16:00',
			username: ''
		}
	},
	methods: {
		setName: function() {
			if(this.username !== "") {
				//
			}
		}
	},
	components: {
		XButton,
		XInput
	}
}
</script>