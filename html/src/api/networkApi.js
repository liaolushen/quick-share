const config = {
/*	url: 'http://45.32.41.145:8888',*/
	url: '',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
/*		'mode': 'no-cors'*/
	},
	interface: {
		login: "/api/manage/login",
		createRoom: '/api/manage/create-room',
		modifyRoom: '/api/manage/modify-room',
		createName: '/api/chat/create-name',
		getName: '/api/chat/get-name',
		getRoom: '/api/chat/get-room-info',
		getMembers: '/api/chat/get-room-members',
		getMessages: '/api/chat/get-room-messages',
		getRoomList: '/api/manage/get-room-list',
		getFiles: '/api/share/get-file-list'
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
				component.setId(res.data.manager_id.toString());
				component.setRole('manager');
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
			console.log(res.data);
			component.receiveMembers(res.data.user_list);
		});
	},
	getMessages: (component, method, room_id) => {
		var message_num = 10;
		var url = config.url + config.interface.getMessages + "?room_id=" + room_id + "&&message_num=" + message_num;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			for(var i = 0 ; i < res.data.message_list.length; i++) {
				if(component.id == res.data.message_list[i].uid) {
					res.data.message_list[i].role = 'self';
				} else {
					res.data.message_list[i].role = 'other';
				}
			}
			component.receiveMessages(res.data.message_list);
			//return Promise.resolve();		
		});
	},
	getName: (component, method, room_id) => {
		var url = config.url + config.interface.getName + "?room_id=" + room_id;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			console.log('getName')
			console.log(res)
			if(res.status_info === "ok") {
				component.setName(res.data.nick_name);
				component.setId(res.data.uid);
				component.setRole('user')
				return Promise.resolve();
			} else {
				return Promise.reject(res.status_info);
			}
		})
	},
	getRoom: (component, method, room_id) => {
		var url = config.url + config.interface.getRoom + "?room_id=" + room_id;
		return fetch(url, {
			credentials: 'include',
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.setCurRoom(res.data);
		})
	},
	createRoom: (component, method, data) => {
		var url = config.url + config.interface.createRoom
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers,
			body: JSON.stringify(data)
		}).then((res) => {
			return res.json();
		}).then((res) => {
			component.createRoom(res.data);
		})
	},
	modifyRoom: (component, method, data) => {
		var url = config.url + config.interface.modifyRoom;
		return fetch(url, {
			credentials: 'include',			
			method: method,
			headers: config.headers,
			body:  JSON.stringify(data)
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
			var room_list = res.data.room_list;
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
			body:  JSON.stringify(data)
		}).then((res) => {
			return res.json();
		}).then((res) => {
			console.log(res);
			component.setId(res.data.uid);
			component.setName(res.data.nick_name);
			component.setRole('user');
		})
	},

	
	//file parts
	getFiles: (component, method, room_id) => {
		var url = config.url + config.interface.getFiles + "?room_id=" + room_id;
		console.log(url)
		return fetch(url, {
			credentials: 'include',
			method: method,
			headers: config.headers
		}).then((res) => {
			console.log('getFiles')
			return res.json();
		}).then((res) => {
			console.log(res)
			component.receiveFiles(res.data.file_list);
		})
	}
}

export { networkApi }