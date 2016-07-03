<style scoped>
.info{
  display: inline-block;
  width: 40px;
  height: 60px;
  margin: 10px 3px 0px 3px;
}
.avatar {
  width: 40px;
  height: 40px;
  background-color: #ddd;
  overflow: hidden;
  margin-bottom: 3px;
}
.name {
  color: gray;
  overflow: hidden;
  text-overflow: ellipsis;
  height: 20px;
}
</style>

<template>
  <div class="info">
    <div class="avatar">
      <canvas width="40" height="40" :id="idHash"></canvas>
    </div> 
    <div class="name">{{nick_name}}</div>
  </div>
   

</template>

<script>

export default {
  props: ['uid', 'nick_name'],
  computed: {
    hash() {
      return md5(this.uid);
    },
    idHash() {
      return 'md5' + this.hash;
    },
  },
  ready() {
    jdenticon.update("#"+this.idHash, this.hash);
  }
}

</script>