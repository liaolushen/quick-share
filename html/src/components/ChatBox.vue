<style>
.msg-list {
  height: 100%;
  box-sizing: border-box;
  overflow: scroll;
  -webkit-overflow-scrolling: touch;
}
.transparent-button {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 30px;
  height: 30px;
  border-radius: 15px;
  color: #fff;
  z-index: 999;
  text-align: center;
  background-color: rgba(0,0,0,.6);
}

#input-area {
  position: fixed;
  bottom: 0;
  left: 0;
}
</style>

<template>
  <a id="transparent-button" class="transparent-button" v-link="{path:'/prop'}">...</a>
  <div id="msg-list" class="msg-list" style="padding-bottom: 70px;" v-el:list>

    <message v-for="message in messages" :role="message.role" :name="message.nick_name" :content="message.content"></message>
  </div>
  <div id="input-area">
    <my-input></my-input>
  </div>
</template>

<script>
import Message from './Message'
import MyInput from './Input'
import { getMessages, getCurRoom,getId } from "./../vuex/getters"
import { addMember, delMember, recieveMessage } from './../vuex/actions'

export default {
  props: {
    width: {
      type: String,
      default: "100%"
    },
    role: {
      type: String,
      default: 'user'
    }
  },
  data() {
    return {}
  },
  ready() {
    console.log('who,hahahahaha');
    console.log(this)
    $("#input-area").css("width", this.width);
    if(this.role === "manager") {
      $("#transparent-button").css("display", "none");
    }

/*    if(socket === null && this.room) {
      socket = io.connect("http://45.32.41.145.8888/chat");
      socket.on('connect', () => {
        socket.emit('join room', {room_id: room.room_id});
      });
    }
    socket.on('system message', (message) => {
      console.log('system message');
      console.log(message);
      message.role = "system";
    });
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
    });*/
  }, 
  vuex: {
    getters: {
      messages: getMessages,
      room: getCurRoom,
      id: getId
    },
    actions: {
      delMember,
      addMember,
      recieveMessage
    }
  },
  watch: {
    'messages': function(old, val) {
      const msgList = this.$els.list;
      msgList.scrollTop = msgList.scrollHeight;
      console.log(msgList.scrollTop, msgList.scrollHeight);
    }
  },
  components: {
    Message,
    MyInput
  }
}
</script>