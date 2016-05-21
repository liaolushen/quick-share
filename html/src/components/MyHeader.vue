<template>
  <div class="header">
    <div class="header-left">
      <slot name="left"></slot>
    </div>
    <div class="header-right">
      <slot name="right"></slot>
      <div class="header-more-wrapper" @click.preventDefault @click="">
        <div class="header-more"></div>
        <ul>
          <li v-link="{name: 'home'}">主页</li>
          <li>注销</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    onClickBack: function () {
      if (this.leftOptions.preventGoBack) {
        this.$emit('on-click-back')
      } else {
        history.back()
      }
    }
  }
}
</script>

<style>
.header{
  position: relative;
  background-color: #000;
  overflow: hidden;
  color: white;
  line-height: 45px;
}
.header-left {
  float: left;
  padding-left: 20px; 
}
.header-right {
  float: right;
  padding-right: 28px;
}
/*增加悬浮的面积*/
.header-more-wrapper {
  position: fixed;
  width: 25px;
  height: 30px;
  right: 8px;
  z-index: 9999;
  top: 15px;
}
.header-more {
  position: fixed;
  right: 10px;
  top: 18px; 
  display: inline-block;
  width: 0;
  height: 0;
  padding-bottom: 40px;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 15px solid white;
}
.header-more-wrapper ul {
  position: fixed;
  visibility: hidden;
  top: 7%;
  right: 5px;
  width: 60px;
  height: 70px;
  padding: 0 5px;
  line-height: 35px;  
  background-color: #00897B;
  color: white;
  text-align: center;
}
.header-more-wrapper li {
  height: 30px;
  border-bottom: 1px solid #ccc;
}
.header-more:hover {
  border-top-color: #3FA156;
} 
.header-more-wrapper:hover ul {
  visibility: visible;
}
li:hover {
  color: yellow;
}

</style>
