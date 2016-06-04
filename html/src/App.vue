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
import { getId, getCurRoom } from './vuex/getters'


module.exports = {
  data() {return {}},
  store: store,
  ready: () => {
    console.log(store.state.id)
    if(socket) {
      $(window).on('beforeunload', function() {
        if(socket) {
          socket.emit('leave room', {room_id: this.room.room_id})
        }
      })
    }
    router.beforeEach((transition) => {
      if (transition.to.auth && !store.state.id) {
        transition.redirect('/');
      } else {
        transition.next();
      }
    });
  }
}
</script>

