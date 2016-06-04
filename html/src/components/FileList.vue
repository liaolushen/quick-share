<style scoped>
.empty {
	height: 30px;
	text-align: center;
	font-size: 20px;
}
</style>
<template>
	<div class="ui-list">
		<template v-if="lists.length === 0">
			<div class = "empty">空空如野</div>
		</template>
		<file-item v-for="item in lists" :file="item" :index="$index" v-on:remove="remove"></file-item>
	</div>
</template>

<script>

import FileItem from './FileItem'

export default {
	data() {
		return {
			lists: []
		}
	},
	methods: {
		add: function(file) {
			this.lists.push(file);
		},
		remove: function(index) {
			this.lists.splice(index, 1);
		}
	},
	components: {
		FileItem
	}
}
</script>