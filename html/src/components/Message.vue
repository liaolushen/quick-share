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
  overflow: hidden;
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
      <div class="avatar">
        <canvas width="40" height="40" :id="idHash"></canvas>
      </div>
    </div>
    <div class="main">
      <div class="name">{{ name }}</div>
      <div class="bubble"
      :class="{'l-bbl': role == 'other', 'r-bbl': role == 'self'}">
        {{{ formatContent }}}
      </div>
    </div>
    <div v-if="role == 'self'" class="right">
      <div class="avatar">
        <canvas width="40" height="40" :id="idHash"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';

var emoList = ['微笑', '撇嘴', '色', '发呆', '得意', '流泪', '害羞', '闭嘴', '睡', '大哭', '尴尬', '发怒', '调皮', '呲牙', '惊讶', '难过', '酷', '冷汗', '抓狂', '吐', '偷笑', '可爱', '白眼', '傲慢', '饥饿', '困', '惊恐', '流汗', '憨笑', '大兵', '奋斗', '咒骂', '疑问', '嘘', '晕', '折磨', '衰', '骷髅', '敲打', '再见', '擦汗', '抠鼻', '鼓掌', '糗大了', '坏笑', '左哼哼', '右哼哼', '哈欠', '鄙视', '委屈', '快哭了', '阴险', '亲亲', '吓', '可怜', '菜刀', '西瓜', '啤酒', '篮球', '乒乓', '咖啡', '饭', '猪头', '玫瑰', '凋谢', '示爱', '爱心', '心碎', '蛋糕', '闪电', '炸弹', '刀', '足球', '瓢虫', '便便', '月亮', '太阳', '礼物', '拥抱', '强', '弱', '握手', '胜利', '抱拳', '勾引', '拳头', '差劲', '爱你', 'NO', 'OK', '爱情', '飞吻', '跳跳', '发抖', '怄火', '转圈', '磕头', '回头', '跳绳', '挥手', '激动', '街舞', '献吻', '左太极', '右太极']

export default {
  props: ['role', 'name', 'content', 'uid'],
  data() {
    return {
      
    }
  },
  computed: {
    hash() {
      return md5(this.uid);
    },
    idHash() {
      return 'md5' + this.hash;
    },
    formatContent() {
      var rr = /\\(微笑|撇嘴|色|发呆|得意|流泪|害羞|闭嘴|睡|大哭|尴尬|发怒|调皮|呲牙|惊讶|难过|酷|冷汗|抓狂|吐|偷笑|可爱|白眼|傲慢|饥饿|困|惊恐|流汗|憨笑|大兵|奋斗|咒骂|疑问|嘘|晕|折磨|衰|骷髅|敲打|再见|擦汗|抠鼻|鼓掌|糗大了|坏笑|左哼哼|右哼哼|哈欠|鄙视|委屈|快哭了|阴险|亲亲|吓|可怜|菜刀|西瓜|啤酒|篮球|乒乓|咖啡|饭|猪头|玫瑰|凋谢|示爱|爱心|心碎|蛋糕|闪电|炸弹|刀|足球|瓢虫|便便|月亮|太阳|礼物|拥抱|强|弱|握手|胜利|抱拳|勾引|拳头|差劲|爱你|NO|OK|爱情|飞吻|跳跳|发抖|怄火|转圈|磕头|回头|跳绳|挥手|激动|街舞|献吻|左太极|右太极)/g

      var bb = this.content.replace(rr, function(a) {
        var a = a.replace('\\', '');
        var index = _.indexOf(emoList, a);
        return `<img src="https://res.wx.qq.com/mpres/htmledition/images/icon/emotion/${index}.gif">`;
      })
      return bb;
    }
  },
  ready() {
    jdenticon.update("#"+this.idHash, this.hash);
  }
}

</script>