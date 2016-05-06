import { set } from 'vue';

export default {
  ADD (state) {
    state.test++;
  },
  SEND_MESSAGE (state, message) {
    state.messages.push(message);
  },
  UPDATE_PADDING (state, newVal) {
    state.padding = newVal + 20;
  }
}