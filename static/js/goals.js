// DOM Elements
const checkboxes = document.querySelectorAll('.completion-checkbox');
const descriptionToggles = document.querySelectorAll('.toggle-description');


// Event Listeners
checkboxes.forEach(function (checkbox) {
	checkbox.addEventListener('change', handleCheckboxChange);
});
descriptionToggles.forEach(function (button) {
	button.addEventListener('click', handleToggleDescription);
});


// Event Handlers
function handleCheckboxChange(event) {
	const form = event.target.closest('form');
	form.submit();
}

function handleToggleDescription(event) {
	const goalId = event.target.getAttribute('data-goal-id');
	const description = document.getElementById(`description-${goalId}`);
	description.classList.toggle('show');

	// Update button text
	event.target.textContent = description.classList.contains('show')
		? 'Hide description'
		: 'See description';
}
