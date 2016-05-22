<style scoped>
	#groups {
		min-height: 100%;
		background-color: #EAEAEA;
	}
	#groups header {
		color: #A4A5A5;
		padding: 25px 0 0 15px;
	}
	.clearfix:after {
		content: '.';
		height: 0;
		visibility: hidden;
		display: block;
		clear: both;
	}
</style>

<template>
	<div class="view-page" id="home-page">
		<m-header>
			<span slot="left">SHARE</span>
			<span slot="right">{{name}}</span>
		</m-header>
		<div id="groups" class="clearfix">
			<header>你所创建的群组</header>
			<room-card v-for="room in roomList"  :room_name="room.room_name"  :start_time ="room.start_time" :end_time="room.end_time" :room_id="room.room_id" :description="room.description"></room-card>
			<room-card></room-card>
		</div>
	</div>
</template>

<script>
import MHeader from './../MyHeader'
import RoomCard from './../RoomCard'
import { setCurRoom } from './../../vuex/actions'
import { getRooms, getId, getName } from './../../vuex/getters'

export default {
	vuex: {
		getters: {
			roomList: getRooms,
			auth: getId,
			name: getName
		},
		actions: {
			setCurRoom
		}
	},
	route: {
		activate (transition) {
			console.log("adfa", this.auth);
			!this.auth ? transition.redirect('/'):transition.next();
		}
	},
  components: {
		MHeader,
		RoomCard, 
  }
}
</script>