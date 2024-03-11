import os
from dotenv import load_dotenv
from flask_cors import CORS
from llm import identify_city
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/query", methods=["POST"])
def query():
    if "photo" not in request.files:
        return jsonify({"error": "No photo provided"}), 400

    photo = request.files["photo"]
    if photo:
        photos_dir = os.path.join("photos")
        os.makedirs(photos_dir, exist_ok=True)
        photo.save(os.path.join(photos_dir, photo.filename))

        answer = identify_city(os.path.join(photos_dir, photo.filename))

        return jsonify({"answer": answer}), 200
    else:
        return jsonify({"error": "No photo provided"}), 400


if __name__ == "__main__":
    app.run(debug=True)
