function reload_page() {
	var delete_confirmation = document.getElementById('delete_confirmation')
	var qns_list= document.getElementById('qns_list')
	console.log("delete triggered");
	qns_list.style.display = "grid";
	delete_confirmation.style.display = "none";
	};


function delete_page() {
	var delete_confirmation = document.getElementById('delete_confirmation')
	var qns_list= document.getElementById('qns_list')
	console.log("delete triggered");
	qns_list.style.display = "none";
	delete_confirmation.style.display = "flex";
};


