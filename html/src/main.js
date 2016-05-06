import Vue from 'vue'
import App from './App'
import store from './vuex/store'
import VueRouter from 'vue-router'
import { configRouter } from './route-config'

/* eslint-disable no-new */

Vue.config.debug = true
Vue.config.devtools = true

Vue.use(VueRouter);

const router = new VueRouter({
  history: false
});

configRouter(router);


router.start(App, '#app');

window.router = router;


