import { set } from 'vue'
import * as types from './mutation-types'

export default {
	//string; id = '1'
	[types.SET_ID] (state, id) {
		state.user.id = id;
	},

	//string; username = 'luxi'
	[types.SET_NAME] (state, name) {
		state.user.name = name;
	},

	[types.SET_ROLE] (state, role) {
		state.user.role = role
	},
	//obj; room = {end_time: , room_id: , room_name: , start_time:}
	[types.ADD_ROOM] (state, room) {
		addRoom(state, room);
	},

	// obj: room = {...}
	[types.DEL_ROOM] (state, room) {
		delRoom(state, room);
	},

	[types.LEAVE_ROOM] (state) {
		leaveRoom(state);
	},

	// Array; rooms = [{}, {}] 
	[types.RECEIVE_ROOMS] (state, rooms) {
		rooms.forEach(function (room) {
			addRoom(state, room);
		});
	},

	// obj; room = {end_time: ,}
	[types.SET_CUR_ROOM] (state, room) {
		state.room = room;
	},

	//obj: member = {id: username}
	[types.ADD_MEMBER] (state, member) {
		addMember(state, member);
	},

	//obj: member = {id, username}
	[types.DEL_MEMBER] (state, member) {
		delMember(state, member);
	},

	//Array: members = [{},{}]
	[types.RECEIVE_MEMBERS] (state, members) {
		state.members = [];
		members.forEach(function (member) {
			if(member.uid)
				addMember(state, member);
		});
	},

	//obj: message = {}
	[types.RECEIVE_MESSAGE] (state, message) {
		state.messages.push(message);
	},

	//array: messages = 
	[types.RECEIVE_MESSAGES] (state, messages) {
		state.messages = [];
		messages.forEach(function (message) {
			state.messages.push(message);
		});
	},

	//obj: message = {}
  [types.SEND_MESSAGE] (state, message) {
    state.messages.push(message);
  },

  //array: files = [{file_format: , file_name: , file_size: , file_id:}]
  [types.ADD_FILE] (state, file) {
  	state.files.push(file)
  },

  [types.RECEIVE_FILES] (state, files) {
  	state.files = files
  },

  [types.RESET] (state) {
  	state.user = {
  		name: null,
  		id: null,
  		role: null
  	};
  	state.rooms = [];
  	state.room = null;
  	state.messages = [];
  	state.files = [];
  }
}

function leaveRoom(state) {
	state.room = null;
	state.messages = [];
	state.members = [];
}

function delMember(state, member) {
	console.log('mutaions')
	console.log(state.members)
	for(var i = 0, len = state.members.length; i < len; i++) {
		if(member.uid == state.members[i].uid) {
			state.members.splice(i, 1);
		}
	}
}

function addRoom(state, room) {
	var isExist = false;
	state.rooms.forEach(function (post) {
		if(post.room_id === room.room_id) {
			isExist = true;
		}
	});
	console.log(room)
	if(!isExist) {
		state.rooms.push(room);
	}
}

function delRoom(state, room) {
	var delIndex = -1; 
	state.rooms.forEach(function (post, index) {
		if(post.room_id === room.room_id) {
			delIndex = index;
		}
	});
	if(delIndex !== -1) {
		state.rooms.splice(delindex, 1);
	}
}

function addMember(state, member) {
	console.log(state.members);
	var isExist = false;
	state.members.forEach(function (post) {
		if(post.uid === member.uid) {
			isExist = true;
		}
	});
	if(!isExist) {
		state.members.push(member);
	}
}

function DelMember(state, member) {
	var delIndex = -1;
	state.members.forEach(function (post, index) {
		if(post.uid === member.uid) {
			delindex = index;
		}
	});
	if(delIndex !== -1) {
		state,member.splice(delIndex, 1);
	}
}