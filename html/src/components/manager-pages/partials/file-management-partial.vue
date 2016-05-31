<style scoped>
#file-list {
	width: 90%;
	background-color: white;
	margin: 10px auto 0 auto;
	border: 1px solid #EEE;
	border-radius: 6px;
}
	
#browse {
	width: 90%;
	display: block;
	margin: 10px auto 0 auto;
	line-height: 3;
	border-radius: 6px;
	border: none;
	background-color: #74CEE0;
}
</style>

<template>
	<div id="file-area">
		<div id="file-list">
			<file-list v-ref:files></file-list>
		</div>
		<div id="file-btn">
			<button id="browse">选择文件上传</button>
		</div>
	<div>
</template>

<script>

import FileList from './../../FileList';

export default {
	data() {
		return {}
	},
	ready() {
		var flow = new Flow({
  		target: '/upload', // target path
  		simultaneousUploads: 1,
  		query: {
    		groupCode: Date.now()
  		}
		});
		var that = this;
		flow.assignBrowse(document.getElementById('browse'));
		flow.assignDrop(document.getElementById('file-area'));
		flow.on('fileAdded', function(file, event){
    	that.$refs.files.add(file);
		});
		flow.on('filesSubmitted', function(file, event) {
  		flow.upload();
		});
		flow.on('fileSuccess', function(file,message){
		});
		flow.on('fileError', function(file, message){
		});
	},
	components: {
		FileList
	}
}
</script>