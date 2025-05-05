// DOM elements
const checkboxes = document.querySelectorAll('.completion-checkbox');


// Event Listeners
checkboxes.forEach(function (checkbox) {
	checkbox.addEventListener('change', handleCheckboxChange);
});


// Define event handler
function handleCheckboxChange(event) {
	const form = event.target.closest('form');
	form.submit();
}
