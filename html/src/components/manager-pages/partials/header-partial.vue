<style scoped>
.brand {
}
</style>

<template>
	<div class="brand">
		<x-header :left-options="{showBack: false}" :right-options="{showMore: true}" style="background-color: #000;"><span slot="left">SHARE</span><span slot="right">{{name}}</span></x-header>
	</div>
</template>

<script>
import { XHeader } from 'vux'
import { getName } from './../../../vuex/getters'
export default {
	components: {
		XHeader
	},
	vuex: {
    getters: {
      name: getName
    }
  },
}
</script>