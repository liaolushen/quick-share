
export const setId = ({ dispatch }, id) => {
	dispatch('SET_ID', id);
}

export const setName = ({ dispatch }, name) => {
	dispatch('SET_NAME', name);
}
export const setRole = ({ dispatch }, role) => {
	dispatch('SET_ROLE', role)
}

export const createRoom = ({ dispatch }, room) => {
	dispatch('ADD_ROOM', room);
}

export const delRoom = ({ dispatch }, room) => {
	dispatch('DEL_ROOM', room);
}

export const leaveRoom = ({ dispatch }, room) => {
	dispatch("LEAVE_ROOM");
}

//for manager
export const setCurRoom = ({ dispatch }, room) => {
	dispatch('SET_CUR_ROOM', room)
} 

export const setRooms = ({ dispatch }, rooms) => {
	dispatch("RECEIVE_ROOMS", rooms)
}

//for user
export const joinRoom = ({ dispatch }, room) => {
	dispatch('SET_CUR_ROOM', room);
}

export const addMember = ({ dispatch }, member) => {
	dispatch('ADD_MEMBER', member);
}

export const delMember = ({ dispatch }, member) => {
	dispatch('DEL_MEMBER', member);
}

export const receiveMembers = ({ dispatch }, members) => {
	dispatch('RECEIVE_MEMBERS', members);
}

export const receiveMessage = ({ dispatch }, message) => {
	dispatch("RECEIVE_MESSAGE", message)
}

export const receiveMessages = ({ dispatch }, messages) => {
	dispatch("RECEIVE_MESSAGES", messages)
}

export const sendMessage = ({ dispatch }, message) => {
  dispatch('SEND_MESSAGE', message);
}

//file
export const addFile = ({ dispatch }, file) => {
	dispatch('ADD_FILE', file);
}

export const receiveFiles = ({dispatch}, files) => {
	dispatch('RECEIVE_FILES', files);
}

export const reset = ({ dispatch }) => {
	dispatch('RESET');
}