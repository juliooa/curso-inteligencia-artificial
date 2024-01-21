from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_endpoint = "https://api.elevenlabs.io/v1"
headers = {
    "xi-api-key": api_key,
}
model_id = "eleven_multilingual_v2"
voice_id_rachel = "21m00Tcm4TlvDq8ikWAM"


def get_models():
    url = f"{elevenlabs_endpoint}/models"
    response = requests.request("GET", url, headers=headers)


def get_voices():
    url = f"{elevenlabs_endpoint}/voices"
    response = requests.request("GET", url, headers=headers)
    return response.json()["voices"]


def text_to_speech(text, model_id, voice_id):
    headers["Accept"] = "audio/mpeg"
    url = f"{elevenlabs_endpoint}/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": model_id,
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.status_code)
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
            return f.name
    if response.status_code == 422:  # unprocessible entity
        print(json.dumps(response.json(), indent=4))
        return ""
    return response.status_code


response = text_to_speech(
    "Hola bienvenidos al curso de inteligencia artificial", model_id, voice_id_rachel
)
print(response)
