# Video Transcriptions
Demo of using Whisper for video transcriptions.

# Setup 
Follow set up instructions at https://github.com/openai/whisper.

* Install OpenAI Whisper:
```
pip install -U openai-whisper
```

* Install `ffmpeg` into your environment:
```
sudo apt update && sudo apt install ffmpeg
```

* Run using `python3`
```
python3 transcribe.py 
```

```
import whisper
import os

model = whisper.load_model("turbo")
for file in os.listdir("data"):
    if file.endswith((".mp4", ".mkv", ".mov", ".mp3", ".wav")):
        path = os.path.join("data", file)
        result = model.transcribe(path)
        with open(path + ".srt", "w") as f:
            f.write(result["text"])
```


# Demo 
Transcripts were generated for two samples:
* [Free Surgical Care in Sudan: An Interview With Dr. Gina Portella](https://www.ctsnet.org/article-video/free-surgical-care-in-sudan-an-interview-with-dr-gina-portella/) - [Whisper Transcript file](./data/FreeSurgicalCareinSudanAnInterviewWithDrGinaPortella_1080p.mp4.srt).
* [Safe Cerebral Protection: How to Handle Dangerous Sternal Reentry](https://www.ctsnet.org/article-video/safe-cerebral-protection-how-handle-dangerous-sternal-reentry/) - [Whisper Transcript file](./data/SafeCerebralProtectionDoublePatchTechniqueforAorticandMitralValveReplacement_1080p.mp4.srt).


