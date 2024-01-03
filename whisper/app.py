import openai

openai.api_key = "TU_API_KEY"

audio_file = open("audio.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)