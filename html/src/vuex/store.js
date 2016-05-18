import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/logger';
import mutations from './mutations';
import { messages, username, room, id, members } from './../data/mock'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: username,
    id: id,
    rooms: [],
    room: room, //current room
    members: members, //members for the current room
    messages: messages //messages for the current room    
  },
  mutations,
  middlewares: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : []
})