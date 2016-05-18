<template>
  <div class="m-search-box">
    <span class="m-icon-search"></span>
    <input class="weui-input" type="text" title="" placeholder="搜索">
  </div>
</template>

<style scoped>
  .m-search-box {
    position: relative;
  }
  .m-icon-search {
    position: absolute;
    left: 1.2em;
    top: 0.7em;
  }
  .m-icon-search::before {
    content: "\EA0E";
    font-family: weui;
    color: #AAA;
  }
  .m-search-box input {
    display: block;
    min-width: 80%;
    border: 1px solid #DADADA ;
    border-radius: 10px;
    font-size: 1.3em;
    padding: 0.5em 2em;
  }
</style>

<script>
export default {

}
</script>