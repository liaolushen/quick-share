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
  <div id="msg-list" class="msg-list" v-bind:style="{paddingBottom: padding + 'px'}" v-el:list>
    <a v-link="{path:'/prop'}">GO</a>
    <message v-for="message in messages" :role="message.role" :name="message.name" :content="message.content"></message>
  </div>
  <my-input></my-input>
</div>
</template>

<script>

import Message from './Message'
import MyInput from './Input'

import { getPadding } from '../vuex/getters';

export default {
  data() {
    return {}
  },
  vuex: {
    getters: {
      padding: getPadding,
      messages: state => state.messages
    }
  },
  watch: {
    'padding': function(old, val) {
      const msgList = this.$els.list;
      msgList.scrollTop = msgList.scrollHeight;
    },
    'messages': function(old, val) {
      const msgList = this.$els.list;
      msgList.scrollTop = msgList.scrollHeight;
    }
  },
  components: {
    Message,
    MyInput
  }
}
</script>