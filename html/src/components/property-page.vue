<style>
  html {
    background-color: #fafafa;
  }

</style>

<template>
  <div class="view-page">
    <group title="群成员">
      <cell></cell>
    </group>
    <group title="群功能">
      <cell title="群二维码" link="qrcode"></cell>
      <cell title="群文件" link="files"></cell>
      <cell title="查找聊天记录" link="history"></cell>
      <cell title="向管理员说悄悄话" link="feedback"></cell>
    </group>
    <group>
      <cell title="退出聊天"></cell>
    </group>

  </div>
</template>

<script>
import { Group, Cell } from "vux";

export default {
  components: {
    Group,
    Cell
  },
  data() {
    return {
    }
  }
}
</script>