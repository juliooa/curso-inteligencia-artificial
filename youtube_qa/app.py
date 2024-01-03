''' Conversa con videos de youtube'''
import re
import uuid
import json
from pytube import YouTube
import whisper
import chromadb
import openai

def parse_segment(segment):
    return {
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    }

QUERY = "How to overcome obstacles"

print("Descargando video...")
ytvideo = YouTube("https://www.youtube.com/watch?v=RJsvR_gSEjg")
file_name = re.sub(r'\W+',' ', ytvideo.title) + ".mp4"
ytvideo.streams.first().download("",file_name)

print("Transcribiendo video...")
MODEL = whisper.load_model("tiny.en")
transcription = MODEL.transcribe(file_name)
segments = []
for item in transcription["segments"]:
    segments.append(parse_segment(item))


#Embeddings
print("Creando embeddings...")
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="transcription")
for segment in segments:
    collection.add(
        ids=str(uuid.uuid4()),
        documents=segment["text"],
        metadatas={"start": segment["start"],
                   "end": segment["end"]})

print("Consultando embeddings...")
result = collection.query(query_texts=QUERY, n_results=5)

#Ask question to bot
SEGMENTS_TEXT = "\n".join([document for document in result['documents'][0]])

SYSTEM_PROMPT = f'''
Eres un bot especializado en responder preguntas acerca de videos de youtube.
A continuación te voy a entregar parte de la transcripción de un video titulado
'{ytvideo.title}',que se trata de '{ytvideo.description}', y
tu vas a tener que contestar una pregunta del usuario, sólo basandote en
la información que te estoy entregando.
La información es la siguiente:
{SEGMENTS_TEXT}
'''
print(SYSTEM_PROMPT)

print("Conectando a OpenAI")
openai.api_key = "TU_API_KEY"
result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": SYSTEM_PROMPT},
          {"role":"user", "content": QUERY}
    ]
)
print(result)
print(result['choices'][0]['message']['content'])
