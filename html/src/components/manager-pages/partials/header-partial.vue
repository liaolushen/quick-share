<style scoped>
.brand {
}
</style>

<template>
	<div class="brand">
		<x-header :left-options="{showBack: false}" :right-options="{showMore: false}" style="background-color: #000;"><span slot="left">SHARE</span><span slot="right">{{username}}</span></x-header>
	</div>
</template>

<script>
import { XHeader } from 'vux'

export default {
	components: {
		XHeader
	},
	vuex: {
    getters: {
      username: state => state.username
    }
  },
}
</script>