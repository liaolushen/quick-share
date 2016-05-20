var validator = {
	login: (data) => {
		if(data.manager_password === "" || data.manager_email === "") {
			return "Please fill the form";
		} else {
			return null;
		}
	},
	group_info: (data) => {
		for(value of room) {
			if(value === "") {
				return "Please fill the form"
			} else {
				return null;
			}
		}
	}
}

export {validator}