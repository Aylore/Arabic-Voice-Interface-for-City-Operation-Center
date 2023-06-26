const transcribeButton = document.getElementById('transcribeButton');
const transcriptionForm = document.getElementById('transcriptionForm');
const transcriptionFormRecord = document.getElementById('transcriptionFormRecord');
const transcriptionVideo = document.getElementById('transcriptionVideo');
const h2 = document.querySelector('.animate-flicker');


recordButton.addEventListener('click', (event) => {
  h2.removeAttribute('hidden');
});

transcribeButton.addEventListener('click', (event) => {
  h2.removeAttribute('hidden');
});

// Record Form
transcriptionFormRecord.addEventListener('submit', (event) => {
    recordButton.disabled = true;
    transcribeButton.disabled = true;
});

// Upload Form
transcriptionForm.addEventListener('submit', () => {
    transcribeButton.disabled = true;
    recordButton.disabled = true;

});

transcriptionVideo.addEventListener('ended', () => {
    transcribeButton.disabled = false;
    recordButton.disabled = false;
});