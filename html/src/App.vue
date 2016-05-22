<style>
html {
  height: 100%;
}

body {
  height: 100%;
}

@import '~vux/vux.css';

.view-page {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
}

#app {
  position: relative;
  height: 100%;
}

</style>

<template>
  <div>
    <router-view class="ui-view"></router-view>
  </div>
     
</template>

<script>
import store from "./vuex/store";
import { getId } from './vuex/getters'


module.exports = {
  data() {return {}},
  store: store
}

</script>

