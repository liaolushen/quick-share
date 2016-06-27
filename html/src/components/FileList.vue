<style scoped>
.empty {
	height: 30px;
	text-align: center;
	font-size: 20px;
}
.ui-list {
	height: 300px;
	overflow: auto;
}
</style>
<template>
	<div class="ui-list">
		<template v-if="lists.length === 0">
			<div class = "empty">暂无文件</div>
		</template>
		<file-item v-for="item in lists" :file="item"></file-item>
	</div>
</template>

<script>

import FileItem from './FileItem'
import { getCurRoom,getFiles } from "./../vuex/getters"
import { addFile } from './../vuex/actions'
export default {
	data() {
		return {
		}
	},
	vuex: {
		getters: {
			room: getCurRoom,
			lists: getFiles
		},
		actions: {
			addFile
		}
	},
	components: {
		FileItem
	}
}
</script>