<template>
  <div>
    <group>
      <cell title="vue" value="cool"></cell>
    </group>
    <div>{{ num }}</div>
    <button @click="addOne">ADD</button>
  </div>
</template>

<script>

import { Group, Cell } from "vux";
import { addOne } from "../vuex/actions";

export default {
  components: {
    Group,
    Cell
  },
  vuex: {
    getters: {
      num: (store) => store.test
    },
    actions: {
      addOne
    }
  }
}
</script>

<style>
@import '~vux/vux.css';
</style>