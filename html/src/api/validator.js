var validator = {
	login: (data) => {
		if(data.manager_password === "" || data.manager_email === "") {
			return "Please fill the form";
		} else {
			return null;
		}
	},
	group_info: (data) => {
		console.log(data);
		for(var item in data) {
			if(data[item] === "") {
				return "Please fill the form"
			}
		}
		return null;
	}
}

export {validator}