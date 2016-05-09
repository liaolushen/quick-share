<style>
.msg-list {
  height: 100%;
  box-sizing: border-box;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
}
</style>

<template>
<div class="view-page">
  <div id="msg-list" class="msg-list" style="padding-bottom: 70px;" v-el:list>
    <a v-link="{path:'/prop'}">GO</a>
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