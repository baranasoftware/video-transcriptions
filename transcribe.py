import whisper
import os

model = whisper.load_model("turbo")
for file in os.listdir("data"):
    if file.endswith((".mp4", ".mkv", ".mov", ".mp3", ".wav")):
        path = os.path.join("data", file)
        result = model.transcribe(path)
        mel = whisper.log_mel_spectrogram(result, n_mels=model.dims.n_mels).to(model.device)
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")
        with open(path + ".srt", "w") as f:
            f.write(result["text"])
