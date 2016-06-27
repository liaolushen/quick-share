export const getId = state => {
	return state.user.id ? state.user.id : -1;
	//return 1
}

export const getName = state => {
	return state.user.name;
}

export const getRole = state => {
	return state.user.role;
}

export const getRooms = state => {
	return state.rooms.length === 0 ? null : state.rooms;
}

export const getCurRoom = state => {
	if(!state.room) {
		return null;
	} else {
		return state.room; 
	}
}

export const getForm = state => {
	if(!state.room) {
		return {
  		room_name: '',
  		description: '',
  		start_time: '选择时间',
  		end_time: '选择时间'						
		}
	} else {
		return state.room
	}
}

export const getMembers = state => {
	return state.members;
}

export const getMessages = state => {
	return state.messages;
}

export const getFiles = state => {
	return state.files;
}

export const getFileById = (state, id) => {
	for(var i = 0, len = state.files; i < len; i++) {
		if(state.files[i].file_id == id) {
			return state.files[i]
		}
	}
}