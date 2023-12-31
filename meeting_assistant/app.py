import os
from meeting_tasks import get_actionable_items, summarize_meeting
from transcriptions import open_transcription, save_transcription, transcribe_audio

#https://www.youtube.com/watch?v=dOXe3Qc5u6w
audio_path = "weekly_meeting_rust.mp4"

if not os.path.exists("transcription.txt"):
    transcription = transcribe_audio(audio_path)
    save_transcription(transcription, "transcription.txt")

transcription = open_transcription("transcription.txt")

# translation = translate_transcription(transcription)
# print("Translation:")
# print(translation)
# print("\n")

summary = summarize_meeting(transcription)
print("Summary:")
print(summary)
print("\n")

actionable_items = get_actionable_items(transcription)
print("Actionable items:")
print(actionable_items)