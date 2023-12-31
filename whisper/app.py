import openai

openai.api_key = "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"

audio_file = open("audio.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)