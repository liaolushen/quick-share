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
			<room-card v-for="room in roomList" :room="room"></room-card>
			<room-card></room-card>
		</div>
	</div>
</template>

<script>
import MHeader from './../MyHeader'
import RoomCard from './../RoomCard'
import { setCurRoom,receiveMessage,addMember,delMember } from './../../vuex/actions'
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
			receiveMessage
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
	      this.receiveMessage(message);
	    });
		}
	},
  components: {
		MHeader,
		RoomCard, 
  }
}
</script>