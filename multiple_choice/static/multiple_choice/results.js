var form = document.getElementById('form');
form.addEventListener('submit', showMessage);

function showMessage(event) {
  alert("Your response has been recorded.");
  event.preventDefault();
}