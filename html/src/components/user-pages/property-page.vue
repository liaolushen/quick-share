
<style>
  html {
    background-color: #fafafa;
  }

</style>

<template>
  <div class="view-page">
    <group title="群成员">
      <avatar-cell v-for="member in members" :uid="member.uid" :nick_name="member.nick_name"></avatar-cell>
    </group>
    <group title="群功能">
      <cell title="群二维码" v-link="{name: 'qrcode'}"></cell>
      <cell title="群文件" v-link="{name: 'files'}"></cell>
      <!--
      <cell title="查找聊天记录" v-link="{name: 'history'}"></cell>
      <cell title="向管理员说悄悄话" v-link="{name: 'feedback'}"></cell>
      !-->
    </group>
    <group>
      <cell title="进入聊天" @click="enterRoom"></cell>
      <cell title="退出聊天" @click="leaveRoom"></cell>
    </group>

  </div>
</template>

<script>
import { Group, Cell } from "vux";
import { setCurRoom,receiveMessage,addMember,delMember, reset } from './../../vuex/actions'
import { getCurRoom, getMembers } from './../../vuex/getters'
import AvatarCell from './../AvatarCell'

export default {
  components: {
    Group,
    Cell,
    AvatarCell
  },
  data() {
    return {
    }
  },
  vuex: {
    getters: {
      room: getCurRoom,
      members: getMembers
    },
    actions: {
      setCurRoom,
      addMember,
      delMember,
      receiveMessage,
      reset
    }
  },
  methods: {
    enterRoom: function() {
      router.go({name: 'room', params: {room_id: this.room.room_id}});
    },
    leaveRoom: function() {
      var id = this.room.room_id
      socket.emit('leave room', {room_id: id})
      this.reset();
      socket = null;
      router.go({name: 'thanks'})
    }
  },
  ready() {
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
  }
}
</script>