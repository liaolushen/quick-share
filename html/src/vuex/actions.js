export const setID = ({ dispatch }, id) => {
	dispatch('SET_ID', id);
}

export const setUsername = ({ dispatch}, username) => {
	dispatch('SET_USENAME', username);
}

export const createRoom = ({ dispatch }, room) => {
	dispatch('ADD_ROOM', room);
}

export const delRoom = ({ dispatch }, room) => {
	dispatch('DEL_ROOM', room);
}

//for manager
export const chooseRoom = ({ dispatch }, room) => {
	dispatch('SET_CUR_ROOM', room)
} 

export const getRooms = ({ dispath }, rooms) => {
	dispatch("RECEIVE_ROOMS", rooms)
}

//for user
export const joinRoom = ({ dispatch }, room) => {
	dispatch('SET_CUR_ROOM', room);
}

export const memberJoin = ({ dispatch }, member) => {
	dispatch('ADD_MEMBER', member);
}

export const memberLeave = ({ dispatch }, member) => {
	dispatch('DEL_MEMBER', member);
}

export const getMembers = ({ dispatch }, members) => {
	dispatch('RECEIVE_MEMBERS', members);
}

export const recieveMessage = ({ dispatch }, message) => {
	dispatch("RECEIVE_MESSAGE", message)
}

export const getMessages = ({ dispatch }, messages) => {
	dispatch("RECEIVE_MESSAGES", messages)
}

export const sendMessage = ({ dispatch }, message) => {
  dispatch('SEND_MESSAGE', message);
};
