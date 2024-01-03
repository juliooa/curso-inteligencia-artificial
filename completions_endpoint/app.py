import json
import openai

def complete(text):
    openai.api_key = "TU_API_KEY"
    completion = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt='''
Eres un chatbot asistente virtual, que ayuda a los usuarios a aprender inglés.
Assistant: Hola soy tu asistente, preguntame lo que quieras.
User: Hola, como se dice hola en inglés?
Assistant: se dice 'Hi'
User: {text}
Assistant: aqui
User: 
'''.format(text=text),
        max_tokens=200,
        temperature=0.5,
        frequency_penalty=1,
        user="julio"
    )

    return completion

response = complete("Cómo se dice 'Donde esta el baño?'")

print(json.dumps(response, indent=4))