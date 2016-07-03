<style scoped>
  .file-item {
    padding: 10px 0px 10px 40px;
    overflow: hidden;
    position: relative;
    border-bottom: 2px solid #EEE;
    height: 60px;
  }
  .item-icon {
    float: left;
  }
  .item-icon img {
    width: 40px;
    height: 50px;
  }
  .item-info {
    position: relative;
    left: 10px;
    top: -10px;
  }
  .item-name {
    padding-top: 10px;
    font-weight: bold;
    font-size: 1.2em;
  }
  .item-size {
    color: #ccc;
  }
  .item-action {
    position: absolute;
    right: 0px;
  }
</style>

<template>
  <div class="file-item" @click="enterFile">
    <div class="item-icon">
      <img :src="format" alt="">
    </div>
    <div class="item-info">
      <div class="item-name">{{file.file_name}}</div>
      <div class="item-size">{{file.file_size | trans}}</div>
    </div>
  </div>
</template>

<script>

import imgSrc from './imgBase64'

export default {
  props: ['file'],
  computed: {
    format: function() {
      var pos = this.file.file_name.indexOf('.');
      var str = this.file.file_name.substring(pos+1);
      return imgSrc[str]; 
    },
  },
  filters: {
    trans: function(size){
      var MB = 1000 * 1000, KB =1000;
      if(+size > MB) {
        return Math.round(+size / MB) + 'MB';
      } else if(+size > KB){
        return Math.round(+size / KB) + 'KB';
      } else {
        return size + 'B';
      }
    },
  },
  methods: {
    enterFile: function() {
      console.log(this.file.file_id)
      router.go({name:'file', params: {file_id: this.file.file_id}});
    }
  }
}
</script>