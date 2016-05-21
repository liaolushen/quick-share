const config = {
	url: 'http://45.32.41.145:8888',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'mode': 'cors'
	},
	interface: {
		login: "/api/manage/login",
		createRoom: '/api/manage/create-room',
		modifyRoom: '/api/manage/modify-room',
		createName: '/api/chat/create-name',
		getName: '/api/chat/get-name',
		getMembers: '/api/chat/get-room-members',
		getMessages: '/api/chat/get-room-messages',
		getRoomList: '/api/manage/get-room-list'
	}
}

const networkApi = {
	login: (component, method, data) => {
		var url = config.url + config.interface.login;
		return fetch(url, {
			credentials: 'include',				
			method: method,	
			headers: config.headers,
			body: JSON.stringify(data)
		}).then((res) => {
			console.log(res);
			return res.json();
		}).then((res) => {
			if(res.status_info != "ok") {
				return Promise.reject(res.status_info);
			} else {
				component.setName(res.data.manager_name);
				component.setId(res.data.manager_id);
			}
		})
	},
	getMembers: (component, method, room_id) => {
		var url = config.url + config.interface.getMembers + "?room_id=" + room_id;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.receiveMembers(res.data.user_list);
		});
	},
	getMessages: (component, method, room_id, message_num) => {
		var url = config.url + config.interface.getMessages + "?room_id=" + room_id + "&&message_num=" + message_num;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.receiveMessages(res.data.message_list);
			//return Promise.resolve();		
		});
	},
	getName: (component, method, room_id) => {
		var url = config.url + config.interface.getName + "?room_id" + room_id;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.setName(res.data.nick_name);
			component.setId(res.data.uid);
		})
	},
	createRoom: (component, method, data) => {
		var url = config.url + config.interface.createRoom
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers,
			body: data
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.createRoom(res.data);
			component.setCurRoom(res.data);
		})
	},
	modifyRoom: (componnent, method, data) => {
		var url = config.url + config.interface.modifyRoom;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: headers,
			body: data
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.setCurRoom(res.data);
		})
	},
	getRoomList: (component, method) => {
		var url = config.url + config.interface.getRoomList;
		return fetch(url,{
			credentials: 'include',					
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			var room_list =res.data.room_list;
			if(room_list) {
				if(room_list.length !== 0) {
					component.setRooms(room_list);
				}
				return Promise.resolve();
			} else {
				return Promise.reject(res.status_info);
			}
		})
	},
	createName: (component, method, data) => {
		var url = config.url + config.interface.createName;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers,
			body: data
		}).then((res) => {
			return res.json();
		}).then((dres) => {
			component.setId(res.data.uid);
			component.setName(res.data.nick_name);
		})
	}
}

export { networkApi }