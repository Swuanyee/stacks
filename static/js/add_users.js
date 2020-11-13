function main() {
	console.log("loaded");
	if (user_profile != "Teacher") {
		$('.choices').css("display", "none")
	};
	console.log(user_profile)
	$("input:file").change(() => {
		console.log("file uploaded")
		var filepath= $("#id_excelForm").val();
		console.log(filepath)
		var filename = filepath.substring(filepath.lastIndexOf("\\")+1, filepath.length);
		console.log(filepath);
		$(".fileUpload").css("fill", "#E85D05")
		$("#text").html(filename);
		$("#text").css("color", "#E85D05")
	});
};

$(document).ready(main());
