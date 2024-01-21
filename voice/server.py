from flask import Flask, request, send_file, jsonify
from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_endpoint = "https://api.elevenlabs.io/v1"
headers = {
    "xi-api-key": api_key,
}

app = Flask(__name__)


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


@app.route("/text2speech", methods=["GET"])
def text2speech():
    model_id = "eleven_multilingual_v1"
    voice_id_rachel = request.args.get(
        "voice_id", default="21m00Tcm4TlvDq8ikWAM", type=str
    )
    # text = request.json["text"]
    text = request.args.get("text", default="", type=str)
    audio_file = text_to_speech(text, model_id, voice_id_rachel)
    return send_file(audio_file, as_attachment=True)


@app.route("/clone_voice", methods=["POST"])
def clone_voice():
    if "file" not in request.files:
        return jsonify({"error": "No file"})

    audio_file = request.files["file"]
    name = request.form["name"]
    description = request.form["description"]

    audio_file_path = f"output_{datetime.now()}.mp3"
    audio_file.save(audio_file_path)

    with open(audio_file_path, "rb") as file:
        files = {"files": (file.name, file)}
        data = {"name": name, "description": description}

        url = f"{elevenlabs_endpoint}/voices/add"
        response = requests.post(url, headers=headers, files=files, data=data)
        print(response.status_code)
        return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
