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
		<m-header></m-header>
		<div id="groups" class="clearfix">
			<header>你所创建的群组</header>
			<group-card v-for="group in groupList"  :room_name="group.room_name"  :start_time ="group.start_time" :date="group.end_time" :room_id="group.room_id"></group-card>
			<group-card room_name="2016 国际体验设计大会" start_time ="6/9 10:00" end_time="6/9 14:00" :room_id="123123"></group-card>
			<group-card></group-card>
		</div>
	</div>
</template>

<script>
import MHeader from './partials/header-partial'
import GroupCard from './../GroupCard'
import { setCurRoom } from './../../vuex/actions'
import { getRooms } from './../../vuex/getters'

export default {
	vuex: {
		getters: {
			groupList: (state) => {
				if(getRooms(state).length === 0) {
					return null;
				} else {
					return getRooms(state)
				}
			}
		},
		actions: {
			setCurRoom
		}
	},
  data() {
  	return {
  		
  	}
  },
  components: {
		MHeader,
		GroupCard, 
  }
}
</script>