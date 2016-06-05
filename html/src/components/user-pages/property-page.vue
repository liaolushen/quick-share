<style>
  html {
    background-color: #fafafa;
  }

</style>

<template>
  <div class="view-page">
    <group title="群成员">
      <cell></cell>
    </group>
    <group title="群功能">
      <cell title="群二维码" v-link="{name: 'qrcode'}"></cell>
      <cell title="群文件" v-link="{name: 'files'}"></cell>
      <cell title="查找聊天记录" v-link="{name: 'history'}"></cell>
      <cell title="向管理员说悄悄话" v-link="{name: 'feedback'}"></cell>
    </group>
    <group>
      <cell title="退出聊天"></cell>
    </group>

  </div>
</template>

<script>
import { Group, Cell } from "vux";
import { setCurRoom,recieveMessage,addMember,delMember } from './../../vuex/actions'

export default {
  components: {
    Group,
    Cell
  },
  data() {
    return {
    }
  },
  vuex: {
    getters: {

    },
    actions: {
      setCurRoom,
      addMember,
      delMember,
      recieveMessage
    }
  },
  ready: () => {
    if(socket) {
      socket.on('user update', (message) => {
        console.log('user update');
        console.log(message);
        if(message.flag === 'leave') {
          this.delMember({uid:message.uid, nick_name:message.nick_name})
          alert(message.nick_name, "leave")
        } else {
          this.addMember({uid:message.uid, nick_name: message.nick_name});
          alert(message.nick_name, "join");
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
}
</script>