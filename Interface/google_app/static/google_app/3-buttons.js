let stream, recorder, audioBlob;
const recordBtn = document.getElementById('record-btn');
const stopBtn = document.getElementById('stop-btn');
const playBtn = document.getElementById('play-btn');
const audio = document.getElementById('audio');

recordBtn.addEventListener('click', async () => {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);
    const chunks = [];
    recorder.addEventListener('dataavailable', event => chunks.push(event.data));
    recorder.addEventListener('stop', () => {
        audioBlob = new Blob(chunks, { type: 'audio/wav' });
        audio.src = URL.createObjectURL(audioBlob);
        playBtn.disabled = false;
    });
    recorder.start();
    recordBtn.disabled = true;
    stopBtn.disabled = false;
});

stopBtn.addEventListener('click', () => {
    recorder.stop();
    stream.getTracks().forEach(track => track.stop());
    recordBtn.disabled = false;
    stopBtn.disabled = true;
});

playBtn.addEventListener('click', () => {
    audio.play();
});
