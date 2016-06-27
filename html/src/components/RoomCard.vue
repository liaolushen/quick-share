<style scoped>
	.ui_card {
		float: left;
		display: inline-block;
		background: #FFFFFF;
		width: 15%;
		height: 180px;
		padding: 10px 20px 0 20px;
		margin: 10px 15px;
		overflow: hidden;
		transition: background-color, 0.8s
	}
	.ui_card:hover {
		background-color: #8DD7FF;
	}
	.ui_card_hd {
		width: 90%;
		font-size: 20px;
		height: 30%;
		color: black;
		margin-bottom: 10px;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	.ui_card_hd p {
		padding-top: 10%;
	}
	.ui_card_ft {
		color: gray;
		border-top: 1px solid #D7D5D3;
		width: 100%;
		height: 70%;
		font-size: 15px;
		line-height: 1.2;
		padding-top: 10px;
	}
	.room_time {
		text-indent: 15px;
		padding-bottom: 10px;
	}
	p.add {
		font-size: 70px;
		margin-top: 15%;
		text-align: center
	}
</style>

<template>
	<template v-if="room">
		<div class="ui_card" @click="enterRoom">
			<div class="ui_card_hd">
				<p>{{room.room_name}}</p>
			</div>
			<div class="ui_card_ft">
				<p>开始时间：</p>
				<p class="room_time">{{room.start_time | date}}</p>
				<p>结束时间 :</p>
				<p class="room_time">{{room.end_time | date}}</p>
			</div>
		</div>
	</template>
	<template v-else>
		<div class="ui_card" @click="createRoom">
			<div class="ui_card_add">
				<p class="add">+</p>
			</div>
		</div>
	</template>
</template>

<script>

import {setCurRoom, receiveMembers, receiveMessages, leaveRoom,receiveFiles } from "./../vuex/actions"
import { getCurRoom, getMembers, getId } from "./../vuex/getters"
import { networkApi } from "./../api/networkApi"

export default {
	props: ['room'],
	filters: {
		date: (value) => {
			return new Date(value).toLocaleString();
		}
	},
	vuex: {
		getters: {
			curRoom: getCurRoom,
			id: getId
		},
		actions: {
			setCurRoom,
			receiveMembers,
			receiveMessages,
			leaveRoom,
			getMembers,
			receiveFiles
		}
	},
	methods: {
		enterRoom: function() {
			//当前房间存在，如果选择的与上次选择的一样就直接进入；否则就重置
			if(this.curRoom) {
				if(this.room.room_id === this.curRoom.room_id) {
					router.go({name: 'group-management', params: {room_id: this.room.room_id}});
					return;
				} else {
					socket.emit('leave room', {room_id: this.curRoom.room_id});			
					socket.emit('disconnect');
					socket = null;
					this.leaveRoom();
				}
			}
			this.setCurRoom({
				room_name: this.room.room_name,
				description: this.room.description,
				room_id: this.room.room_id,
				start_time: this.room.start_time,
				end_time: this.room.end_time,
			});

			networkApi.getMembers(this, "GET", this.room.room_id)
				.then(() => {
					return networkApi.getMessages(this, "GET", this.room.room_id, "10");
				})
				.then(() => {
					return networkApi.getFiles(this, "GET", this.room.room_id);
				})
				.then(() => {
					router.go({name: "group-management", params: {room_id: this.room.room_id}})
				})
				.catch((err)=>{console.log(err)});
		},
		createRoom: function() {
			if(this.curRoom) {
				socket.emit('leave room', {room_id: this.curRoom.room_id});			
				this.leaveRoom();
				socket = null;
			}
			router.go({name: 'group-management', params: {room_id: "-1"}});
		}
	}
}
</script>