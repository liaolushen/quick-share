<style scoped>

.emo-wrapper {
  display: inline-block;
  width: 14.28%;
  text-align: center;
  height: 50px;
}

.emo-wrapper .vux-emotion {
  box-sizing: border-box;
  padding-top: 14px;
  transform: scale(1.1);
  transform-origin: 50% 0;
}
</style>

<template>
  <swiper :show_dots="false" height="220px">
    <swiper-item v-for="emoPage in emoList">
      <div v-for="emoLine in emoPage">
        <div class="emo-wrapper" v-for="emo in emoLine" @click="insertEmo(emo)">
          <emotion>{{emo}}</emotion>
        </div>
      </div>
    </swiper-item>
  </swiper>
</template>

<script>

import { Swiper, SwiperItem, WechatEmotion as Emotion } from 'vux'

const emoList = ['微笑', '撇嘴', '色', '发呆', '得意', '流泪', '害羞', '闭嘴', '睡', '大哭', '尴尬', '发怒', '调皮', '呲牙', '惊讶', '难过', '酷', '冷汗', '抓狂', '吐', '偷笑', '可爱', '白眼', '傲慢', '饥饿', '困', '惊恐', '流汗', '憨笑', '大兵', '奋斗', '咒骂', '疑问', '嘘', '晕', '折磨', '衰', '骷髅', '敲打', '再见', '擦汗', '抠鼻', '鼓掌', '糗大了', '坏笑', '左哼哼', '右哼哼', '哈欠', '鄙视', '委屈', '快哭了', '阴险', '亲亲', '吓', '可怜', '菜刀', '西瓜', '啤酒', '篮球', '乒乓', '咖啡', '饭', '猪头', '玫瑰', '凋谢', '示爱', '爱心', '心碎', '蛋糕', '闪电', '炸弹', '刀', '足球', '瓢虫', '便便', '月亮', '太阳', '礼物', '拥抱', '强', '弱', '握手', '胜利', '抱拳', '勾引', '拳头', '差劲', '爱你', 'NO', 'OK', '爱情', '飞吻', '跳跳', '发抖', '怄火', '转圈', '磕头', '回头', '跳绳', '挥手', '激动', '街舞', '献吻', '左太极', '右太极']

var arr, brr, crr = [];
for (var i = 0, len = emoList.length; i < len; i++) {
  if (i === 0) {
    arr = [];
    brr = [];
    arr.push(emoList[i]);
    continue;
  }

  if (i % 7 === 0) {
    brr.push(arr.slice(0));
    arr = [];
  }
  if (i % 28 === 0) {
    crr.push(brr.slice(0));
    brr = [];
  }
  arr.push(emoList[i]);
}

if (arr.length !== 0) {
  brr.push(arr);
  crr.push(brr.slice(0))
}

export default {
  components: {
    Swiper,
    SwiperItem,
    Emotion
  },
  data() {
    return {
      emoList: crr
    }
  },
  methods: {
    insertEmo(emo) {
      console.log(emo);
      this.$dispatch('insert', emo);
    }
  }
}
</script>