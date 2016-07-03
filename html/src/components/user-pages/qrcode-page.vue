<style scoped>
.room-info {
	width: 70%;
	margin-left: 30%;
	color: gray;
}
#qrcode {
	width: 70%;
	margin: 20% auto 5% auto;
}
</style>

<template>
  <div class="view-page">
    <div v-el:qrcode id="qrcode"></div>
    <div class="room-info">
  		<div>扫扫上方二维码加入</div>
  		<div>{{room.name}}</div>
  	</div>
  </div>
</template>

<script>
import { getCurRoom, getMembers } from './../../vuex/getters'

export default {
  data() {
    return {}
  },
  vuex: {
  	getters: {
  		room: getCurRoom
  	}
  },
  ready() {
    var url = "http://" + document.domain + ":" + location.port + "/#!" + "/chat-entrance/" + this.room.room_id;
    console.log('二维码呢')
    console.log(url);
    new QRCode(this.$els.qrcode, url);
  },
}
</script>