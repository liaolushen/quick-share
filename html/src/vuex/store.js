import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/logger';
import mutations from './mutations';
//import { messages, name, room, id, members} from './../data/mock'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      name: null,
      id: null,
      role: null
    },
    rooms: [],
    room: null, //current room
    members: [], //members for the current room
    messages: [], //messages for the current room
    files: []
  },
  mutations,
  middlewares: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : []
})