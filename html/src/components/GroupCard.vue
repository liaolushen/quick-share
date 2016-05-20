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
	<div class="ui_card" @click="enterGroup">
		<template v-if="room_name !== ''">
			<div class="ui_card_hd">
				<p>{{room_name}}</p>
			</div>
			<div class="ui_card_ft">
				<p>{{start_time}}</p>
				<p>{{end_time}}</p>
			</div>
		</template>
		<template v-else>
			<div class="ui_card_add">
				<p class="add">+</p>
			</div>
		</template>
	</div>
</template>

<script>

import {setCurRoom, receiveMembers, receiveMessages, leaveRoom } from "./../vuex/actions"
import { getCurRoom } from "./../vuex/getters"
import { networkApi } from "./../api/networkApi"

export default {
	props: {
		room_name: {
			type: String,
			default: ''
		},
		start_time: {
			type: String,
			default: ''
		},
		end_time: {
			type: String,
			default: ''
		},
		room_id: {
			type: Number,
			default: ''
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
			leaveRoom
		}
	},
	methods: {
		enterGroup: function() {
			if(this.room_id === room.room_id) {
				router.go({name: 'group-management'});
			} else {
				this.leaveRoom();
			}
			if(this.room_id !== "") {
				this.setCurRoom({
					room_name: this.room_name,
					room_id: this.room_id,
					start_time: this.start_time,
					end_time: this.end_time
				});

				//networkApi.getMembers(this, "GET", this.room_id).networkApi.getMessages(this, "GET", this.room_id, "10").then(() => {router.go({name: "group-management"})}).catch((err)=>{console.log(err)});
				router.go({name: 'group-management'});
			} else {
				router.go({name: 'group-management'});
			}
		}
	}
}
</script>