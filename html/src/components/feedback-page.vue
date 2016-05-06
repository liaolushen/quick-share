<style scoped>
  .seperate {
    height: 20px;
  }
</style>

<template>
  <group title="用户反馈">
    <x-textarea :max="max" placeholder="向管理员说些什么"></x-textarea>
  </group>
  <div class="seperate"></div>
  <div style="margin: 10px">
    <x-button text="提交" type="primary"></x-button>
  </div>
  
</template>

<script>

import { Group, XButton, GroupTitle } from 'vux';
import { Textarea as XTextarea } from 'vux';

export default {
  data() {
    return {
      max: 400
    }
  },
  components: {
    XTextarea,
    Group,
    XButton
  }
}
</script>