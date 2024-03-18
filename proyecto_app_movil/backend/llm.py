import os
import base64
from openai import OpenAI


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def identify_food(photo_path):
    base64_image = encode_image(photo_path)

    api_key = os.getenv("OPEN_AI_API_KEY")
    client = OpenAI(api_key=api_key)

    prompt = """
    Eres un asistente nutricional. El usuario te va a enviar una foto de comida y tu tienes
    que identificar los alimentos en la foto, calcular sus calorias, proteínas, azucares, e
    hidratos de carbono, y comunicarle al usuario estos valores, junto con la descripción de la comida,
    en el siguiente formato:
    Alimentos: La foto contiene arroz y pollo.
    Calorias(kcal): 230
    Proteínas(g): 20
    Azucar(g): 10
    Hidratos de carbono (g): 30
    """

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=1000,
    )

    return response.choices[0].message.content
