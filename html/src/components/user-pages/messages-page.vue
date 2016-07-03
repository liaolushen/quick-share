<style>

</style>

<template>
<div class="view-page">
  <chat-box></chat-box>
</div>
</template>

<script>

import ChatBox from './../ChatBox'
import {receiveMessages, receiveMembers} from './../../vuex/actions'
import { getId } from './../../vuex/getters'
import { networkApi } from './../../api/networkApi'

export default {
  components: {
    ChatBox
  },
  vuex: {
    getters: {
      id: getId
    },
  	actions: {
  		receiveMessages,
  		receiveMembers
  	}
  },
  ready() {
  	networkApi.getMembers(this, 'GET', this.$route.params.room_id)
  		.then(() => {
  			return networkApi.getMessages(this, 'GET', this.$route.params.room_id);
  		})
  		.catch((err) => {
  			console.log(err);
  		})
  }
}
</script>