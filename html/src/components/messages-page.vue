<style>
.msg-list {
  height: 100%;
  box-sizing: border-box;
  overflow: auto;
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
</style>

<template>
<div class="view-page">
  <a class="transparent-button" v-link="{path:'/prop'}">...</a>
  <div id="msg-list" class="msg-list" style="padding-bottom: 70px;" v-el:list>

    <message v-for="message in messages" :role="message.role" :name="message.name" :content="message.content"></message>
  </div>
  <my-input></my-input>
</div>
</template>

<script>

import Message from './Message'
import MyInput from './Input'

export default {
  data() {
    return {}
  },
  vuex: {
    getters: {
      messages: state => state.messages
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