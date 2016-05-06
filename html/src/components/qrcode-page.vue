<style></style>

<template>
  <div class="view-page">
    <div v-el:qrcode></div>
  </div>
</template>

<script>
export default {
  ready() {
    new QRCode(this.$els.qrcode, "http://jindo.dev.naver.com/collie");
  },
  data() {
    return {}
  }
}
</script>