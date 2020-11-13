function main() {
	console.log("Hello")
	var choices = document.querySelectorAll('.choices')
	if (user_profile != "Teacher") {
		choices[0].style.display = 'none';
	};
};

window.addEventListener('load', () => {
	main();
})
