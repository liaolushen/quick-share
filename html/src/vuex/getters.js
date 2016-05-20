export const getId = state => {
	return state.id;
}

export const getName = state => {
	return state.name;
}

export const getRooms = state => {
	return state.rooms;
}

export const getCurRoom = state => {
	if(!state.room) {
		return {
  		room_name: '',
  		description: '',
  		start_time: '选择时间',
  		end_time: '选择时间'						
		}
	} else {
		return state.room; 
	}
}

export const getMembers = state => {
	return state.members;
}

export const getMessages = state => {
	return state.messages;
}