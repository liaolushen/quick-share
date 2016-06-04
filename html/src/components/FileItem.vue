<style scoped>
	.file-item {
		padding: 10px 0px 10px 40px;
		overflow: hidden;
		position: relative;
		border-bottom: 2px solid #EEE;
	}
	.item-icon {
		float: left;
	}
	.item-icon img {
		width: 75%;
		height: 75%;
	}
	.item-name {
		padding-top: 10px;
		font-weight: bold;
		font-size: 1.5em;
	}
	.item-size {
		color: #ccc;
	}
	.item-delete {
		position: absolute;
		right: 40px;
		top: 40px;
		width: 30px;
		height: 30px;
		border-radius: 50%;
		border: none;
		background-color: #35c9e0;
		color: white;
	}
</style>

<template>
	<div class="file-item">
		<div class="item-icon">
			<img :src="format" alt="">
		</div>
		<div class="item-info">
			<div class="item-name">{{file.name}}</div>
			<div class="item-size">{{size}}</div>
		</div>
		<div class="{'ui-process': true, 'show': isShow}">
			<div class="ui-active-prog"></div>
		</div>
		<button class="item-delete" v-on:click="removeSelf">X</button>
	</div>
</template>

<script>

import imgSrc from './imgBase64'

export default {
	props: ['file', 'index'],
	ready() {
		console.log(this.index);
	},
	computed: {
		isShow: function() {
			return this.file.progress() < 0 && this.file.progress() > 1;
		},
		size: function() {
			return this.trans(this.file.size);
		},
		speed: function() {
			return this.trans(this.file.averageSpeed);
		},
		progress: function() {
			return this.file.progress() * 100 + '%';
		},
		format: function() {
			var pos = this.file.name.indexOf('.');
			var str = this.file.name.substring(pos+1);
			return imgSrc[str];	
		}
	},
	methods: {
		trans: function(size){
			var MB = 1000 * 1000, KB =1000;
			if(+size > MB) {
				return Math.round(+size / MB) + 'MB';
			} else if(+size > KB){
				return Math.round(+size / KB) + 'KB';
			} else {
				return size + 'B';
			}
		},
		removeSelf: function() {
			this.$dispatch('remove', this.index);
		}
	}
}
</script>