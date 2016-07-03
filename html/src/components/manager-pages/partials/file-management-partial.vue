<style scoped>

#file-list{
	padding-top: 10px;
	padding-left: 10px;
	border-top: 10px solid #EEE;
	border-bottom: 10px solid #EEE;
}

#uploading-file-list {
	padding-top: 10px;
	padding-left: 10px;
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
			<h3>文件列表</h3>
			<file-list></file-list>
		</div>
		<div id="uploading-file-list">
			<h3>上传区域</h3>
			<uploading-file-list></uploading-file-list>
		</div>
		<div id="file-btn">
			<button id="browse">选择文件上传</button>
		</div>
	<div>
</template>

<script>

import FileList from './../../FileList'
import UploadingFileList from './../../UploadingFileList'
import { addFile } from "./../../../vuex/actions"
import { getFiles } from "./../../../vuex/getters"

export default {
	data() {
		return {}
	},
	vuex: {
		getters: {
			getFiles
		},
		actions: {
			addFile
		}
	},
	components: {
		FileList,
		UploadingFileList
	},
	ready() {
		flow.assignBrowse(document.getElementById('browse'));
	}
}
</script>