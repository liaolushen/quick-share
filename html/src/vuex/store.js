import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/logger';
import mutations from './mutations';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    test: 0,
    messages: [
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'other', name: '牠们', content: '就快乐撒价格快乐的是就快乐，进口关税了几个'},
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'other', name: '简单快乐', content: 'he就快乐就离开过设计健康管理撒llo'},
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'other', name: '牠们', content: '就快乐撒价格快乐的是就快乐，进口关税了几个'},
      {role: 'self', name: '我自己', content: 'hello'},
      {role: 'other', name: '简单快乐', content: 'he就快乐就离开过设计健康管理撒llo'}
    ]
  },
  mutations,
  middlewares: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : []
})