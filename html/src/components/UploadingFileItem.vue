<style scoped>
	.file-item {
		padding: 10px 0px 10px 40px;
		overflow: hidden;
		position: relative;
		border-bottom: 2px solid #EEE;
		height: 60px;
	}
	.item-icon {
		float: left;
	}
	.item-icon img {
		width: 40px;
		height: 50px;
	}
	.item-info {
		position: relative;
		left: 10px;
		top: -10px;
	}
	.item-name {
		padding-top: 10px;
		font-weight: bold;
		font-size: 1.2em;
	}
	.item-size {
		color: #ccc;
	}
	.item-action {
		position: absolute;
		right: 0px;
	}
	.file-action {
		text-align: center;
		display: inline-block;
		position: relative;
		background-color: #35c9e0;
		width: 60px;
		height: 30px;
		line-height: 30px;
		color: black;
		border-radius: 6px;
		font-size: 1.2em;
	}
	button.file-action {
		right: 85px;
		bottom: 50px;
		border: none;
	}
	.file-action:hover {
		color: green;
	}
</style>

<template>
	<div class="file-item">
		<div class="item-icon">
			<img :src="format" alt="">
		</div>
		<div class="item-info">
			<div class="item-name">{{file.name}}</div>
			<div class="ui-active-prog">{{progress}}</div>
		</div>
		<div class="item-action">
			<button class="file-action" v-on:click="toggle">暂停</button>
<!-- 			<button class="file-action" v-on:click="delete">中止</button> -->
		</div>
	</div>
</template>

<script>

import imgSrc from './imgBase64'

export default {
	props: ['file'],
	ready() {
		console.log(this.file);
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
		toggle: function(event) {
			if(this.file.paused === true) {
				this.file.resume();
				event.target.value = '暂停';
			} else {
				this.file.pause();
				event.target.value = '继续';
			}
		},
		removeSelf: function() {
			alert('中止操作吗？还没有实现')
			/*this.$dispatch('remove', this.index);*/
		}
	}
}
</script>