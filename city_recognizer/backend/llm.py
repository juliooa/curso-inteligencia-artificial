import os
import base64
from openai import OpenAI


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def identify_city(photo_path):
    base64_image = encode_image(photo_path)

    api_key = os.getenv("OPEN_AI_API_KEY")
    client = OpenAI(api_key=api_key)

    prompt="¿Qué ciudad es la de la foto?"
    
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
        max_tokens=300,
    )

    return response.choices[0].message.content
