<style scoped>
.test {
  position: fixed;
  z-index: 999;
  top: 30px;
  background-color: black;
  color: #fff;
}
.input-wrapper {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50px;
  background-color: rgb(244,244,247);
  box-sizing: border-box;
  padding: 0 70px 0 30px;    
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
  float: left;
  width: 30px;
  margin-left: -30px;
}

.main {
  width: 100%;
  position: relative;
  box-sizing: border-box;
  padding: 5px 5px 5px 7px;
}

.right {
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
  font-size: 14px;
  line-height: 40px;
  
}

.weui_btn_primary {
  background-color: rgb(78, 146, 223);
}

</style>

<template>
  <div class="input-wrapper" v-bind:style="{height: wrapperHeight}">
    <div class="test">{{test}}</div>
    <div class="left">hello</div>
    <div class="right">
      <x-button text="发送" type="primary" @click="send"></x-button>
    </div>
    <div class="main">
    <div class="textarea-wrapper">
      <textarea id="input-text" class="flex-textarea" @focus="triggle" @blur="triggle" @input="updateContent" v-bind:style="{height: maxHeight +'px'}">{{content}}</textarea>
    </div>
    <textarea id="fate-text" class="fate-textarea">{{content}}</textarea>
      
      
    </div>
    <div class="comp" v-show="isShow"></div>
  </div>
</template>

<script>
import { sendMessage } from '../vuex/actions';
import { updatePadding } from '../vuex/actions';
import { XButton } from 'vux'
import { getPadding } from '../vuex/getters';

export default {
  components: {
    XButton
  },
  vuex: {
    getters: {
      getPadding
    },
    actions: {
      updatePadding,
      sendMessage
    }
  },
  data() {
    console.log(XButton);
    return {
      isShow: false,
      test: '',
      content: '',
      maxHeight: 40,
    }
  },
  computed: {
    wrapperHeight() {
      return this.isShow ? 
             this.maxHeight + 280 + 'px':
             this.maxHeight + 10 + 'px';
    }
  },
  watch: {
    'content': function(val, oldVal) {
      const flexOne = this.$el.querySelector('#input-text');
      const fateOne = this.$el.querySelector('#fate-text');
      this.maxHeight = fateOne.scrollHeight;
      this.updatePad();

    }
  },
  methods: {
    updatePad() {
      let pad = this.isShow ? this.maxHeight + 280 : this.maxHeight + 10;
      this.updatePadding(pad);
    },
    updateContent(e) {
      this.content = e.target.value;
      this.test = screen.height;
    },
    send() {
      this.sendMessage({'content': this.content, 'name': 'wo', 'role': 'self'});
      this.content = '';
    },
    triggle() {
      this.isShow = !this.isShow;
      this.updatePad();
    }
  }
}
</script>