<style scoped>
  .manage-page {
    /* overflow: hidden; */
  }
  #chatbox-part {
    float: left;
    width: 33%;
    height: 600px;
  }
  #management-part {
    float: left;
    width: 67%;
  }
</style>

<template>
  <div class="view-page manage-page">
    <m-header>
      <span slot="left">SHARE</span>
      <span slot="right">{{name}}</span>
    </m-header>
    <div id="group-manage-body">
      <div id="chatbox-part">
        <chat-box width="33%" role="manager"></chat-box>
      </div>
      <div id="management-part">
        <div id="group-info-header">
          <tab :line-width=2 active-color="#A7C8F0">
            <tab-item v-for="item in managerList" :selected="management === item" @click="management = item"> {{item}} </tab-item>
          </tab>
        </div>
        <template v-if="management === '群管理'">
          <m-group></m-group>
        </template>
        <template v-if="management === '投票管理'">
        </template>
        <template v-if="management === '文件管理'">
        </template>
        <template v-if="management === '消息管理'">
        </template>
      </div>
     </div>

  </div>
</template>

<script>

import {Tab, TabItem, Group, Flexbox, FlexboxItem} from 'vux'
import ChatBox from './../ChatBox'
import MHeader from './../MyHeader'
import MGroup from './partials/group-management-partial'
import {setCurRoom} from './../../vuex/actions'
import { getId, getName, getMessages } from './../../vuex/getters'

export default {
  data() {
    return {
      managerList: ['群管理', '投票管理', '文件管理', '消息管理'],
      management: '群管理',
      res: [{title: 'kdlsag'}]
    }
  },
  route: {
/*    activate (transition) {
      !this.auth ? transition.redirect('/'):transition.next();
    }*/
  }, 
  methods: {
  },
  vuex: {
    getters: {
      messages: getMessages,
      auth: getId,
      name: getName
    }
  },
  components: {
    Tab, 
    TabItem,
    Group,
    Flexbox,
    FlexboxItem,
    MHeader,
    MGroup,
    ChatBox
  }
}
</script>