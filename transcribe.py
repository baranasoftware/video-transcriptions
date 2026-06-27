import whisper

model = whisper.load_model("turbo")
result = model.transcribe("data/SafeCerebralProtectionDoublePatchTechniqueforAorticandMitralValveReplacement_1080p.mp4")
print(result["text"])
