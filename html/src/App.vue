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
  height: 100%;
  position: relative;
}

</style>

<template>
  <div>
    <router-view class="ui-view"></router-view>
  </div>
     
</template>

<script>
import store from "./vuex/store";

module.exports = {
  data() {return {}},
  store: store
}

</script>

