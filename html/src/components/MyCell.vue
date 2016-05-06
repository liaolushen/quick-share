<style scoped>
  .ui_cell_title {
    font-weight: normal;
  }

  .ui_cell_desc {
    color: #aaa;
    font-size: 13px;
  }
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 20px;
    margin-right: 10px
  }
</style>

<template>
<div class="weui_cell">
  <div class="weui_cell_hd">
    <div class="avatar"></div>
  </div>
  <div class="weui_cell_primary">
    <h4 class="ui_cell_title">{{title}}</h4>
    <p class="ui_cell_desc">{{desc}}</p>
  </div>
</div>
</template>

<script>
export default {
  props: ['title', 'desc']
}
</script>