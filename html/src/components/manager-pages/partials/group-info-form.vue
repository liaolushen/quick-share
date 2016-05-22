<template>
	<div class="groups">	
		<group title="群名称">
			<x-input title="" :value.sync='form.room_name'></x-input>
		</group>
		<group title="群介绍">
			<x-textarea :value.sync="form.description" :max="300" :show-counter="false"></x-textarea>
		</group>
		<group title="开始时间">
      <cell title="" primary="content">
        <calendar slot="value" :value.sync="form.start_time | date" hours disable-past></calendar>
      </cell>
		</group>
		<group title="结束时间">
      <cell title="" primary="content">
        <calendar slot="value" :value.sync="form.end_time | date" hours disable-past></calendar>
      </cell>
		</group>
	</div>
	<div class="btn-wrapper">
		<x-button type="primary" @click="editRoom">保存</x-button>
	</div>
</template>

<style>

.groups {
	background: #FFFFFF;
	margin-top: 20px;
	padding: 20px;
	border: 1px solid #DDD;
	border-radius: 10px;
	box-shadow: 1px 1px 2px #ccc;
}

.btn-wrapper {
	margin-top: 15%;
}

.left-part {
	width: 45%;
	float: left;
}

.right-part {
	width: 45%;
	float: right;
}
</style>

<script>
import {Group, Cell, XInput, XTextarea, Datetime, XButton, Calendar} from 'vux'
import { getCurRoom, getForm } from "./../../../vuex/getters"
import { setCurRoom, setMessages, createRoom, leaveRoom } from "./../../../vuex/actions"
import { validator } from "./../../../api/validator"
import { networkApi } from "./../../../api/networkApi"

export default {
/*	props: {
		groupid 
	},*/
	data() {
		return {

		}
	},
	vuex: {
		getters: {
			form: getForm 
		},
		actions: {
			setCurRoom,
			createRoom
		}
	},
	filters: {
		date: (value) => {
			return value === "选择时间" ? value : new Date(value).toLocaleString();
		}
	},
	ready() {
	},
	methods: {
  	editRoom: function() {
			if(!form.room_id) {
	  		var room = {
	  			room_name: this.form.room_name,
	  			description: this.form.description,
	  			start_time: this.form.start_time,
	  			end_time: this.form.end_time
	  		};
	  		var err = validator.group_info(room);
	  		if(!err) {	
	  			networkApi.createRoom(this, "POST", room)
	  				.catch((err) => {
	  					console.log(err);
  				})
	  		} else {
	  			alert(err);
	  		}
  		} else {
  			var room = {
  				room_id: form.room_id,
  				modified_items: {
  					description: form.description,
  					start_time: form.start_time,
  					end_time: form_end_time
  				}
  			}
  			networkApi.modifyRoom(this, "POST", room)
					.catch((err) => {
						console.log(err);
					})
  		}
  	}	
	},
	 components: {
    Cell,
    Group,
    XInput,
    XTextarea,
    Datetime,
    XButton,
    Calendar
  }
}

function checkData(formData) {
	for(let item in formData) {
		if((item === "startTime" || item === 'endTime') && formData[item] === '选择时间') {
			return '请选择时间';
		}
		if(formData[item] === "") {
			return "请填写信息";
		}
	}
	if(new Date(formData['startTime']) > new Date(formData['endTime'])) {
		return "时间前后关系错误"
	}
	return "格式正确";
}
</script>