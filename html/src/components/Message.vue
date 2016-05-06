<style scoped>
.message {
  position: relative;
  overflow: hidden;
  width: 100%;
  box-sizing: border-box;
  
}

.l-msg {
  padding-left: 50px;
}

.r-msg {
  padding-right: 50px;
  text-align: right;
}

.left {
  margin-left: -45px;
  position: absolute;
  bottom: 0;
}

.right {
  margin-right: -45px;
  right: 50px;
  position: absolute;
  bottom: 0;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 20px;
  background-color: #ddd;
}

.main {
  width: 100%;
}

.bubble {
  padding: 10px 12px;
  display: inline-block;
  border-radius: 20px;
  background-color: #eee;
  box-sizing: border-box;
  max-width: 90%;
  font-size: 14px;
  text-align: left;
}

.l-bbl {
  
}

.r-bbl {
  color: #fff;
  background-color: rgb(78, 146, 223);
}

.name {
  padding: 0 15px;
  box-sizing: border-box;
  font-size: 12px;
  color: #aaa;
}

</style>

<template>
  <div class="message"
  :class="{'l-msg': role == 'other', 'r-msg': role == 'self'}">
    <div v-if="role == 'other'" class="left">
      <div class="avatar"></div>
    </div>
    <div class="main">
      <div class="name">{{ name }}</div>
      <div class="bubble"
      :class="{'l-bbl': role == 'other', 'r-bbl': role == 'self'}">
        {{ content }}
      </div>
    </div>
    <div v-if="role == 'self'" class="right">
      <div class="avatar"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['role', 'name', 'content'],
  data() {
    return {
      
    }
  }
}

</script>