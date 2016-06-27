<style>

</style>

<template>
  <div class="view-page">
    <search placeholder="搜索聊天记录", cancel-text="取消" :results="res" v-ref:search></search>
    
  </div>
</template>

<script>
import { Search,Group } from "vux";

export default {
  components: {
    Search,
    Group
  },
  ready() {
    this.$refs.search.touch();
  },
  data() {
    return {
      res: [{title: 'kdlsag'}]
    };
  }
}
</script>