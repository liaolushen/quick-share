<template>
	<div class="groups">	
		<group title="群名称">
			<x-input title="" :value.sync='form.name'></x-input>
		</group>
		<group title="群介绍">
			<x-textarea :value.sync="form.introduction" :max="300" :show-counter="false"></x-textarea>
		</group>
		<group title="开始时间">
      <cell title="" primary="content">
        <calendar slot="value" :value.sync="form.startTime" hours disable-past></calendar>
      </cell>
		</group>
		<group title="结束时间">
      <cell title="" primary="content">
        <calendar slot="value" :value.sync="form.endTime" hours disable-past></calendar>
      </cell>
		</group>
	</div>
	<div class="btn-wrapper">
		<x-button type="primary" @click="storeGroupInfo">保存</x-button>
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

export default {
/*	props: {
		groupid 
	},*/
	data() {
		return {
			form: {
    		name: '',
    		introduction: '',
    		startTime: '选择时间',
    		endTime: '选择时间'
    	}
		}
	},

	methods: {
  	storeGroupInfo: function() {
  		var formData = {
  			name: this.form.name,
  			introuduction: this.form.introduction,
  			startTime: this.startTime,
  			endTime: this.endTime,
  			//groupId: this.groupId
  		};
  		var result ;
  		if(result = "格式正确") {
  			alert('OK');
  			//后台请求
  		} else {
  			alert(result);
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