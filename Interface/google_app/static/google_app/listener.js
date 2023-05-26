const recordButton = document.getElementById('record-button');
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recordButton.addEventListener('click', () => {
recognition.start();
});

stopBtn.addEventListener('click', () => {
    recorder.stop();
    stream.getTracks().forEach(track => track.stop());
    recordButton.disabled = false;
    stopBtn.disabled = true;
});

recognition.addEventListener('result', (event) => {
    const audioData = event.results[0][0].transcript;

    // Send the audio data to the server using an AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const transcriptionTextArea = document.getElementById('transcription-textarea');
            transcriptionTextArea.value += response.transcription + '\n';
        }
    };
    xhr.send(JSON.stringify({ audio_data: audioData }));
});


