<style scoped>
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 20px;
    margin-right: 10px;
    background-color: #ddd;
  }
  .ui_cell_name {
    font-size: 20px;
  }
</style>

<template>
<div class="weui_cell">
  <div class="weui_cell_hd">
    <div class="avatar">
      <canvas width="40" height="40" :id="idHash"></canvas>
    </div>
  </div>
  <div class="weui_cell_primary">
    <p class="ui_cell_name">{{name}}</p>
  </div>
</div>
</template>

<script>
export default {
  props: ['name', 'uid'],
  computed: {
    hash() {
      return md5(this.uid);
    },
    idHash() {
      return 'md5' + this.hash;
    }
  },
  ready() {
    jdenticon.update("#"+this.idHash, this.hash);    
  }
}
</script>