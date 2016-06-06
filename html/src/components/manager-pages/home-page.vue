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
			<room-card v-for="room in roomList"  :room_name="room.room_name"  :start_time ="room.start_time | integer" :end_time="room.end_time | integer" :room_id="room.room_id" :description="room.description"></room-card>
			<room-card></room-card>
		</div>
	</div>
</template>

<script>
import MHeader from './../MyHeader'
import RoomCard from './../RoomCard'
import { setCurRoom,recieveMessage,addMember,delMember } from './../../vuex/actions'
import { getRooms, getId, getName } from './../../vuex/getters'

export default {
	vuex: {
		getters: {
			roomList: getRooms,
			auth: getId,
			name: getName,
			id: getId
		},
		actions: {
			setCurRoom,
			addMember,
			delMember,
			recieveMessage
		}
	},
	filters: {
		integer: (value) => {
			return parseInt(value);
		}
	},
	ready: () => {
		if(socket) {
	    socket.on('user update', (message) => {
	      console.log('user update');
	      console.log(message);
	      if(message.flag === 'leave') {
	        this.delMember({uid:message.uid, nick_name:message.nick_name})
	        console.log(message.nick_name, "leave")
	      } else {
	        this.addMember({uid:message.uid, nick_name: message.nick_name});
	        console.log(message.nick_name, "join");
	      }
	    });
	    socket.on('user message', (message) => {
	      console.log('user message');
	      console.log(message);
	      if(message.uid === this.id) {
	        message.role = "self";
	      } else {
	        message.role = "other";
	      }
	      this.recieveMessage(message);
	    });
		}
	},
	route: {
		activate (transition) {
			console.log("auth:", this.auth);
			!this.auth ? transition.redirect('/'):transition.next();
		}
	},
  components: {
		MHeader,
		RoomCard, 
  }
}
</script>