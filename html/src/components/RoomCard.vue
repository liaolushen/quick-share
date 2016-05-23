<style scoped>
	.ui_card {
		float: left;
		display: inline-block;
		background: #FFFFFF;
		width: 20%;
		min-height: 150px;
		padding: 20px 20px 0 20px;
		margin: 10px 15px;
	}
	.ui_card_hd {
		width: 90%;
		font-size: 25px;
		color: black;
		margin-bottom: 10px
	}
	.ui_card_ft {
		color: #D7D5D3;
		border-top: 1px solid #D7D5D3;
		width: 50%;
		font-size: 15px;
		line-height: 1.2
	}
	
	.ui_card_add  {
	}
	p.add {
		font-size: 70px;
		text-align: center
	}
</style>

<template>
	<template v-if="room_name !== ''">
		<div class="ui_card" @click="enterRoom">
			<div class="ui_card_hd">
				<p>{{room_name}}</p>
			</div>
			<div class="ui_card_ft">
				<p>{{start_time | date}}</p>
				<p>{{end_time | date}}</p>
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

import {setCurRoom, receiveMembers, receiveMessages, leaveRoom } from "./../vuex/actions"
import { getCurRoom, getMembers } from "./../vuex/getters"
import { networkApi } from "./../api/networkApi"

export default {
	props: {
		room_name: {
			type: String,
			default: ''
		},
		start_time: {
			type: Number,
			default: ''
		},
		end_time: {
			type: Number,
			default: ''
		},
		room_id: {
			type: String,
			default: ''
		},
		description: {
			type: String,
			default: ''
		}
	},
	filters: {
		date: (value) => {
			//python and js difference
			return new Date(value).toLocaleString();
		}
	},
	vuex: {
		getters: {
			room: getCurRoom
		},
		actions: {
			setCurRoom,
			receiveMembers,
			receiveMessages,
			leaveRoom,
			getMembers,
		}
	},
	methods: {
		enterRoom: function() {
			//当前房间存在，如果选择的与上次选择的一样就直接进入；否则就重置
			if(this.room) {
				if(this.room.room_id) {
					if(this.room_id === this.room.room_id) {
						router.go({name: 'group-management', params: {room_id: this.room.room.room_id}});
					} else {
						//socket.emit('leave room', {room_id: this.room.room_id});					
						this.leaveRoom();
					}
				}
			}
			this.setCurRoom({
				room_name: this.room_name,
				description: this.description,
				room_id: this.room_id,
				start_time: this.start_time,
				end_time: this.end_time,
			});

			networkApi.getMembers(this, "GET", this.room_id)
				.then(() => {
					return networkApi.getMessages(this, "GET", this.room_id, "10");
				})
				.then(() => {
					router.go({name: "group-management", params: {room_id: this.room_id}})
				})
				.catch((err)=>{console.log(err)});
		},
		createRoom: function() {
			if(this.room) {
				this.leaveRoom();
				//socket.emit('leave room', {room_id: this.room.room_id})
			}
			router.go({name: 'group-management', params: {room_id: "-1"}});
		}
	}
}
</script>