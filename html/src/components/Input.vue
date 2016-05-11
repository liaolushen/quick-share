<style scoped>
.test {
  position: fixed;
  z-index: 999;
  top: 30px;
  background-color: black;
  color: #fff;
}
.bottom-area {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgb(244,244,247);
}

.bottom-area.backdrop-blur {
  backdrop-filter: blur(10px);
  background-color: rgba(244,244,247, .4);
}
.input-wrapper {
  position: relative;
  width: 100%;
  min-height: 50px;
  box-sizing: border-box;
  padding: 0 70px 0 34px;    
}

.input-wrapper:before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 1px;
  display: block;
  overflow: hidden;
  background-color: rgb(223,223,224);
  -webkit-transform: scaleY(0.5);
  transform: scaleY(0.5);
}

.left {
  position: relative;
  box-sizing: border-box;
  height: 100%;
  float: left;
  width: 34px;
  margin-left: -34px;
}

.main {
  position: absolute;
  left: 37px;
  right: 70px;
  box-sizing: border-box;
  padding: 5px 5px 5px 7px;
}

.right {
  position: relative;
  float: right;
  width: 70px;
  margin-right: -70px;
  height: 100%;
  box-sizing: border-box;
  padding: 5px 5px 5px 0;
}

.flex-textarea, .fate-textarea {
  outline: none;
  font-size: 14px;
  display: block;
  border-radius: 5px;
  border: none;
  width: 100%;
  line-height: 1.3;
  height: 40px;
  box-sizing: border-box;
  padding: 10px 8px 10px 8px;
}
.flex-textarea {
  position: relative;
  z-index: 20;
  resize: none;
  box-shadow: 0 0 1px rgb(223,223,224);
}
.textarea-wrapper {
  position: relative;
}

.fate-textarea {
  position: absolute;
  visibility: hidden;
  opacity: 0;
  resize: none;
  top: 0;
  z-index: -10;
}

.comp {
  width: 100%;
  height: 270px;
}


.weui_btn {
  position: absolute;
  font-size: 14px;
  line-height: 40px;
  bottom: 6px;
  right: 5px;
  left: 0;
}

.weui_btn_primary {
  background-color: rgb(78, 146, 223);
}

.ui-emotion {
  position: absolute;
  bottom: 0;
  display: block;
  width: 100%;
  height: 50px;
  background-image: url("../assets/emotion.png");
  background-size: 90%;
  background-repeat: no-repeat;
  background-position: center;
  background-color: transparent;
  border: none;
  box-shadow: none;
  outline: none;
}

.emotion-picker {
  overflow: hidden;
  height: 220px;
  width: 100%;
  background: rgb(246,246,246);
}
</style>

<template>
  <div class="bottom-area">
    <div class="emotion-picker" v-bind:style="{height: emotionAreaHeight + 'px'}">
      <emotion-picker></emotion-picker>
    </div>
    <div class="input-wrapper" v-bind:style="{height: maxHeight + 10 + 'px'}">
      <div class="left">
        <button class="ui-emotion" @click="triggleEmotion"></button>
      </div>
      <div class="right">
        <x-button text="发送" type="primary" @click="send"></x-button>
      </div>
      <div class="main">
        <div class="textarea-wrapper">
          <textarea id="input-text" class="flex-textarea" @focus="focus" @input="updateContent" v-bind:style="{height: maxHeight +'px'}" v-el:realinput>{{content}}</textarea>
        </div>
        <textarea id="fate-text" class="fate-textarea" v-el:fateinput>{{content}}</textarea>
      </div>
    </div>
  </div>
</template>

<script>
import { XButton } from 'vux';

import { sendMessage } from '../vuex/actions';
import EmotionPicker from './EmotionPicker';

export default {
  components: {
    XButton,
    EmotionPicker
  },
  vuex: {
    actions: {
      sendMessage
    }
  },
  data() {
    console.log(XButton);
    return {
      content: '',
      maxHeight: 40,
      isEmotionShow: false
    }
  },
  watch: {
    'content': function(val, oldVal) {
      const flexOne = this.$els.realinput;
      const fateOne = this.$els.fateinput;
      this.maxHeight = fateOne.scrollHeight;
    }
  },
  events: {
    'insert': function(emo) {
      this.content += ` \\${emo} `
    }
  },
  computed: {
    emotionAreaHeight() {
      return this.isEmotionShow ? 220 : 0;
    }
  },
  methods: {
    updateContent(e) {
      this.content = e.target.value;
    },
    triggleEmotion() {
      this.isEmotionShow = !this.isEmotionShow
    },
    send() {
      if (this.content.length <= 0) return;
      this.isEmotionShow = false;
      this.sendMessage({'content': this.content, 'name': 'wo', 'role': 'self'});
      this.content = '';
    },
    focus() {
      this.isEmotionShow = false;
    }
  }
}
</script>