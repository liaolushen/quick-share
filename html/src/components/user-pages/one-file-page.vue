<style scoped>
.file-info {
  background-color: #EEE;
  height: 100%;
  text-align: center;
  padding-top: 30%;
}
.file-action {
  position: fixed;
  bottom: 0;
  background-color: white;
  height: 50px;
  width: 100%;
}
.file-action a {
  text-align: center;
  display: inline-block;
  background-color: #4486F6;
  color: white;
  height: 50px;
  line-height: 50px;
  font-size: 20px;
}
</style>

<template>
  <div class="view-page">
    <div class="file-info">
      <div class="avatar">
        <img :src="format" alt="">
      </div>
      <div class="name">{{file.file_name}}</div>
    </div>
    <div class="file-action">
      <a class="file-action" :href="downloadUrl" :download="file.file_name">下载({{file.file_size | trans}})</a>
    </div>
  </div>
</template>

<script>
import { Group, Cell } from "vux";
import { getFiles } from './../../vuex/getters'
import imgSrc from './../imgBase64'

export default {
  components: {
    Group,
    Cell
  },
  data() {
    return {
      file: {
        file_name: '',
        file_id: '',
        file_size: ''
      }
    }
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
  computed: {
    downloadUrl: function() {
      return '/api/share/download?file_id=' + this.file.file_id
    },
    format: function() {
      var pos = this.file.file_name.indexOf('.');
      var str = this.file.file_name.substring(pos+1);
      return imgSrc[str]; 
    },
  },
  vuex: {
    getters: {
      files: getFiles
    },
    actions: {
    }
  },
  ready() {
    for(var i = 0, len = this.files.length; i < len; i++) {
      if(this.files[i].file_id === parseInt(this.$route.params.file_id)) {
        this.file = this.files[i]
        this.file.file_name = this.files[i].file_name
      }
    }
  }
}
</script>