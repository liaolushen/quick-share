<template>
  <div>
    <template v-if="files.length === 0">
      <div class="no-file-info">
        <div>这里是<em>{{room.name}}</em>的天下</div>
        <div>然而并没有什么文件</div> 
      </div>
    </template>
    <group v-else>
      <file-cell v-for="file in files" :file="file"></file-cell>
    </group>
  </div>
</template>

<style scoped>
  .no-file-info {
    font-size: 20px;    
    text-align: center;
    margin-top: 30%;
  }
</style>

<script>

import FileCell from './../FileCell'
import { Group } from 'vux'
import { setCurRoom,receiveMessage,addMember,delMember,receiveFiles,} from './../../vuex/actions'
import { getCurRoom, getMembers, getFiles } from './../../vuex/getters'
import { networkApi } from './../../api/networkApi'

export default {
  data() {
    return {
    }
  },
  components: {
    FileCell, 
    Group
  },
  vuex: {
    getters: {
      files: getFiles,
      room: getCurRoom
    },
    actions: {
      receiveFiles,
      receiveMessage
    }
  },
  ready() {
    networkApi.getFiles(this, 'GET', this.room.room_id)
      .catch((err) => {
        console.log(err);
      })
  },
}
</script>