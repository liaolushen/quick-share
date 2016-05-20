const config = {
	url: 'http://45.32.41.145:8888',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	},
	interface: {
		login: "/api/manage/login",
		createRoom: '/api/manage/create-room',
		createName: '/api/chat/create-name',
		getName: '/api/chat/get-name',
		getMembers: '/api/chat/get-room-members',
		getMessages: '/api/chat/get-room-messages'
	}
}

const networkApi = {
	login: (component, method, data) => {
		var url = config.url + config.interface.login;
		return fetch(url, {
			method: method,
			headers: config.headers,
			body: JSON.stringify(data)
		}).then((res) => {
			return res.json();
		}).then((data) => {
			if(data.status_info != "ok") {
				return Promise.reject(data.status_info);
			} else {
				component.setName(data.manager_name);
				component.setId(data.manage_id);
			}
		})
	},
	getMembers: (component, method, room_id) => {
		var url = config.url + config.interface.getRoomMembers + "?room_id" + room_id;
		return fetch(url, {
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((data) => {
			setMembers(data.user_list);
			//return Promise.resolve();
		});
	},
	getMessages: (component, method, room_id, message_num) => {
		var url = config.url + config.interface.getMessages + "?room_id" + room_id + "&&message_num=" + message_num;
		return fetch(url, {
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((data) => {
			componet.recieveMessages(data.message_list);
			//return Promise.resolve();		
		});
	},
	getName: (component, method, room_id) => {
		var url = config.url + config.interface.getName + "?room_id" + room_id;
		return fetch(url, {
			method: method,
			headers: config.headers
		}).then((res) => {
			return res.json();
		}).then((data) => {
			component.setName(data.data);
		})
	},
	createRoom: (component, method, data) => {
		var url = config.url + config.interface.createRoom
		return fetch(url, {
			method: method,
			headers: config.headers,
			body: data
		}).then((res) => {
			return res.json();
		}).then((data) => {
			component.createRoom(data.data);
			component.setCurRoom(data.data);
		})
	},
	createName: (component, method, data) => {
		var url = config.url + config.interface.createName;
		return fetch(url, {
			method: method,
			headers: config.headers,
			body: data
		}).then((res) => {
			return res.json();
		}).then((data) => {
			component.setId(data.data.uid);
			component.setName(data.data.nick_name);
		})
	}
}

export { networkApi }