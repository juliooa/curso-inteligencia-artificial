import os
import tempfile
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, request, jsonify
from llm import identify_food

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/query", methods=["POST"])
def query():
    if "photo" not in request.files:
        return jsonify({"error": "No photo provided"}), 400

    photo = request.files["photo"]
    if photo:
        temp_dir = tempfile.gettempdir()
        temp_file = os.path.join(temp_dir, photo.filename)
        photo.save(temp_file)

        answer = identify_food(temp_file)

        os.remove(temp_file)

        return jsonify({"answer": answer}), 200
    else:
        return jsonify({"error": "No photo provided"}), 400


if __name__ == "__main__":
    app.run()
