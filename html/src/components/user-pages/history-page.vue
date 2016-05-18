<style>

</style>

<template>
  <div class="view-page">
    <search placeholder="搜索聊天记录", cancel-text="取消" :results="res" v-ref:search></search>
    <group title="333">
      <my-cell title="123" desc="333"></my-cell>
      <my-cell title="123" desc="333"></my-cell>
    </group>
    
  </div>
</template>

<script>
import { Search,Group } from "vux";
import MyCell from './../MyCell';

export default {
  components: {
    Search,
    MyCell,
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