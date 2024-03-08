import os
import uuid
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from embeddings import create_embeddings, get_documents
from llm import query_llm

load_dotenv()

app = Flask(__name__)
CORS(app)

chatbot_status = {}

@app.route('/build_chatbot', methods=['POST'])
def build_chatbot():
    #recibir un pdf
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'}), 400

    file = request.files['file']
    file.save(os.path.join('pdf_files', file.filename))

    chatbot_id = str(uuid.uuid4())
    chatbot_status[chatbot_id] = {'status': 'Creating embeddings'}
    create_embeddings(chatbot_id, file.filename)

    chatbot_status[chatbot_id] = {'status': 'Embeddings ready'}

    return jsonify({'chatbot_id': chatbot_id}), 201

@app.route('/ask_chatbot/<string:chatbot_id>', methods=['POST'])
def ask_chatbot(chatbot_id):
    #recibir chatbot_id y una pregunta
    if chatbot_id not in chatbot_status:
        return jsonify({'error': 'Chatbot not found'}), 404

    data = request.get_json()
    if 'question' not in data:
        return jsonify({'error': 'Missing "question" in the request body'}), 400

    question = data['question']

    #Accedemos a la base de datos de vectores y obtenemos los
    #documentos relevantes a la pregunta
    relevant_documents = get_documents(chatbot_id, question)

    #Preguntamos a openai gpt junto con los documentos relevantes
    answer = query_llm(question, relevant_documents)

    return jsonify({'answer': answer}), 200

if __name__ == '__main__':
    app.run(debug=True)
