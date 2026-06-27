import whisper
import os

model = whisper.load_model("turbo")
for file in os.listdir("data"):
    if file.endswith((".mp4", ".mkv", ".mov", ".mp3", ".wav")):
        path = os.path.join("data", file)
        result = model.transcribe(path)
        with open(path + ".srt", "w") as f:
            f.write(result["text"])
