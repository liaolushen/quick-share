<style scoped>
.form {
	width: 70%;
	border: 1px solid #ccc;
	margin: 30px auto 0 auto;
	border-radius: 6px
}
.info {
	margin-top: 30px;
	text-align: center;
}
.info label{
	display: inline-block;
	width: 70px;
}
.info input {
	width: 50%;
	line-height: 2em;
	border: 1px solid #8cca12;
	padding-left: 15px;
	font-size: 15px;
	border-radius: 6px;
	box-shadow: 2px 2px 2px #ccc;
}
button {
	width: 30%;
	margin-top: 30px;
	margin-bottom: 30px;
	background-color: #4A90E2;
	color: white;
}
</style>

<template>
<div class="view-page">
	<div class="form">
		<div class="info">
			<label for="email">email</label>
			<input class="" type="text" id="email" v-model="manager_email">		
		</div>
		<div class="info">
			<label for="password">password</label>
			<input class="" type="password" id="password" v-model="manager_password">		
		</div>
		<div>
			<button class="weui_btn" @click="login">登录</button>
		</div>		
	</div>
</div>
</template>

<script>
import { networkApi } from "./../../api/networkApi"
import { validator } from "./../../api/validator"
import { setName, setId, setRooms } from "./../../vuex/actions"
//import {} from './../vuex/getter'


export default {
	data() {
		return {
			manager_password: "123456",
			manager_email: "123456@qq.com",
		}
	},
	vuex: {
		getters: {
		},
		actions: {
			setName,
			setId
		}
	},
	methods: {
		login: function() {
			var data = {
				manager_email: this.manager_email,
				manager_password: this.manager_password
			};
			console.log(data);
			var err = validator.login(data);
			if (!err) {	
				networkApi.login(this,"POST", data)
					.then(() => {
						router.go({name: 'home'});
					})
					.catch((err) => {
						alert(err);
				})
			} else {
				alert(err);
			}
		}
	}
}
</script>