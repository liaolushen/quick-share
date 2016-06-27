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
			<div class = "empty">暂无上传任务</div>
		</template>
		<uploading-file-item v-for="item in lists" :file="item"></uploading-file-item>
	</div>
</template>

<script>

import UploadingFileItem from './UploadingFileItem'
import { getCurRoom } from "./../vuex/getters"
import { addFile } from './../vuex/actions'
export default {
	data() {
		return {
			lists: []
		}
	},
	vuex: {
		getters: {
			room: getCurRoom
		},
		actions: {
			addFile
		}
	}, 
	ready() {
		var that = this;
		console.log(this.room.room_id)
		flow = new Flow({
		  target: '/api/share/upload', // target path
		  simultaneousUploads: 1,
		  speedSmoothingFactor: 0.02,
  		query: {
    		'roomId': this.room.room_id
  		}
		});
		flow.on('fileAdded', function(file, event){
    	that.add(file);
		});
		flow.on('filesSubmitted', function(file, event) {
  		flow.upload();
		});
		flow.on('fileSuccess', function(file,message) {
			//将得到的数据
			console.log('success')
			console.log(message);
			var new_file = JSON.parse(message).data;
			console.log(new_file)
			that.addFile(new_file);
			that.remove(file);
		});
		flow.on('fileError', function(file, message) {
			alert(message);
		});
	},
	methods: {
		add: function(file) {
			this.lists.push(file);
		},
		remove: function(file) {
			//根据file.name来删除
			for(var i = 0, len = this.lists.length; i < len; i++) {
				if(file.name === this.lists[i].name) {
					this.lists.splice(i, 1);
				}
			}
		}
	},
	components: {
		UploadingFileItem
	}
}
</script>