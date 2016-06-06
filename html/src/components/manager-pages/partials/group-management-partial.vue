<template>
  <div class="left-part">
    <group>
      <cell title="成员管理" @click="groupFunc = 'mbMang'"></cell>
      <cell title="群组信息" @click="groupFunc = 'gpInfo'"></cell>
      <cell title="群二维码" @click="groupFunc = 'gpQruc'"></cell>
    </group>
    <group>
      <cell title="删除群组" @click="dlGroup"></cell>
    </group>
  </div>
  <div class="breakline"></div>
  <div class="right-part" v-show="groupFunc === 'gpInfo'">
    <m-group-form></m-group-form>
  </div>
  <div class="right-part" v-show="groupFunc==='mbMang'">
    <m-mem-man></m-mem-man>
  </div>
  <div class="right-part" v-show="groupFunc==='gpQruc'">
    <div v-el:qrcode id="qrcode"></div>
  </div>	
</template>

<style scoped>

.breakline {
  display: inline-block;
  height: 600px;
  border-right: 1px solid #ccc;
}

.left-part {
  width: 45%;
}

.right-part {
  width: 45%;
  margin-right: 3%;
}
.search-wrapper {
  margin-top: 20px;
}

#qrcode {
  width: 100%;
  height: 50%;
  text-align: center;
  margin-top: 50%;
}

</style>

<script>
import MGroupForm from './group-info-form'
import MMemMan from './members-management'
import {Group, Cell} from 'vux'
import MemCell from './../../MemberCell'
import { getCurRoom, getMembers } from './../../../vuex/getters'

export default {
	data() {
		return {
			groupFunc: 'gpInfo'
		}
	},
	methods: {
    dlGroup: () => console.log('delete')
	},
  vuex: {
    getters: {
      room: getCurRoom,
      members: getMembers
    }
  },
	components: {
		MGroupForm,
		Group,
		Cell,
		MemCell	,
    MMemMan
	},
  ready() {
    if(!this.room) {
      console.log('why');
      console.log($('#qrocde'));
      $('#qrcode').append("请先创建房间");
    } else {
      //var url = "http://172.18.41.222:8888/#!" + "/chat-entrance/" + this.room.room_id;
      var url = "http://" + document.domain + ":" + location.port + "/#!" + "/chat-entrance/" + this.room.room_id; 
      console.log(url);
      new QRCode(this.$els.qrcode, url);
    }
  }
}
</script>