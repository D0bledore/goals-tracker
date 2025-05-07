// DOM Elements
const checkboxes = document.querySelectorAll('.completion-checkbox');
const descriptionToggles = document.querySelectorAll('.toggle-description');
const deleteButtons = document.querySelectorAll('.delete-goal-button');


// Event Listeners
checkboxes.forEach(function (checkbox) {
	checkbox.addEventListener('change', handleCheckboxChange);
});
descriptionToggles.forEach(function (button) {
	button.addEventListener('click', handleToggleDescription);
});
deleteButtons.forEach(function (button) {
	button.addEventListener('click', handleDeleteConfirmation);
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

function handleDeleteConfirmation(event) {
	const confirmed = confirm('Are you sure you want to permanently delete this goal?');
	if (confirmed) {
		const form = event.target.closest('form');
		if (form) {
			form.submit();
		}
	}
}
