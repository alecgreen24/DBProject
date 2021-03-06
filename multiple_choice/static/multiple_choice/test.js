// Global variables
// UI Variables
const quiz = document.getElementById('quiz');
const generateBtn = document.getElementById('generateBtn');
const quizConfig = document.getElementById('quizConfig');
const qTotal = 4;
const total = qTotal.value;
const form = document.getElementById('quizForm');
const submit = document.getElementById('submit');
const submitAnswer = document.getElementById('submitAnswer');

// Position Variables
let pos = 1;
let quizPos = 1;
let position = 0;
let incorrectPos = 0;

// Check box variables
const check1 = document.getElementById("check1");
const check2 = document.getElementById("check2");
const check3 = document.getElementById("check3");

// Quiz data
const questions = [];

// Quiz score
let correct = 0;
let incorrect = 0;

// Generate questions & options for quiz
generateBtn.addEventListener('click', (e) => {
  // Check input fields have value
  storeData();
  clearConfig();
    clearForm();
    displayQuiz();
    renderQuiz();
})

function storeData() {
  // Get values
  for(i = 0; i < qTotal; i++){
  const title = "Test Test";
  const input1 = "Input 1";
  const input2 = "Input 2";
  const input3 = "Input 3";
  const value = "A";
  // Append to array
  questions.push([title, input1, input2, input3, value]);
  }
  // Increase position in form
  pos++;
  console.log(pos);
  console.log(qTotal.value);
  // Reset form
  reset();
  console.log(questions);
}



// JavaScript function to get cookie by name; retrieved from https://docs.djangoproject.com/en/3.1/ref/csrf/
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Start Quiz
submit.addEventListener('click', (e) => {
    storeData();
    clearForm();
    displayQuiz();
    renderQuiz();

})

// Render quiz
function renderQuiz() {
  const qTitle = document.getElementById('qTitle');
  const option1 = document.getElementById('option1');
  const option2 = document.getElementById('option2');
  const option3 = document.getElementById('option3');

  // Question Title
  qTitle.innerHTML = questions[position][0];
  // Correct Answer
  option1.innerHTML = questions[position][1];
  // Incorrect Answers
  option2.innerHTML = questions[position][2];
  option3.innerHTML = questions[position][3];
}

// Check answers
function checkAnswer() {
  // Get group name
  choices = document.getElementsByName('choices');
  // Loop through options to check for selected answer
  for (var i = 0; i < choices.length; i++) {
    // Get the value of selected answer
    if (choices[i].checked) {
      choice = choices[i].value;
    }
  }
  // Check if value = correct answer
  if (choice == questions[position][4]) {
    correct++;
  } else {
    incorrect++;
  }
  position++;
  quizPos++
}

// Sumbit Answer
submitAnswer.addEventListener('click', (e) => {
  if (quizPos >= questions.length) {
    checkAnswer();
    displayResults();
  } else {
    checkAnswer();
    clearQuiz();
    clearCheckbox();
    renderQuiz();
  }
})

// Display results from quiz
function displayResults() {
  quiz.innerHTML = '';
  container.innerHTML = '<h5 id="result" class="center">Results ' + correct + '/ ' + questions.length + '</h5><a href="http://127.0.0.1:8000/multiple_choice/list"><input type="button" class="waves-effect waves-light btn-small" value="Return to Home" /></a>';

}

// Event Listener - Add checked status
check1.addEventListener('click', (e) => {
  check1.checked = true;
})
check2.addEventListener('click', (e) => {
  check2.checked = true;
})
check3.addEventListener('click', (e) => {
  check3.checked = true;
})

// Clear configuration
const clearConfig = () => {
  quizConfig.innerHTML = ' '
};
// Clear form
const clearForm = () => {
  form.classList.add('hide');
}
// Clear quiz
const clearQuiz = () => {
  option1.innerHTML = '';
  option2.innerHTML = '';
  option3.innerHTML = '';
}
// Display Quiz
const displayQuiz = () => {
  quiz.classList.remove('hide');
}
// Clear checkboxs
const clearCheckbox = () => {
  check1.checked = false;
  check2.checked = false;
  check3.checked = false;
}
// Render Form
const renderForm = () => {
  const renderForm = document.getElementById('formContainer');
  formContainer.classList.remove('hide');
}

// Reset form
function reset() {
  form.reset();
  const labels = [...document.querySelectorAll("label")];
  labels.forEach((label) => {
    label.classList.add('active');
  })
}