'''
Crear embeddings para las palabras más comunes del español, y luego
buscar las palabras similares a una palabra dada.
'''
import chromadb
from chromadb.utils import embedding_functions

palabras = [
    "año",
    "vida",
    "mundo",
    "trabajo",
    "manera",
    "alguien",
    "familia",
    "noche",
    "forma",
    "problema",
    "agua",
    "gobierno",
    "hombre",
    "ciudad",
    "lugar",
    "amor",
    "día",
    "persona",
    "tiempo",
    "noche",
    "mujer",
    "madre",
    "padre",
    "hijo",
    "hermano",
    "amigo",
    "trabajo",
    "casa",
    "país",
    "ciudad",
    "guerra",
    "paz",
    "mente",
    "razón",
    "voz",
    "mente",
    "luz",
    "camino",
    "mundo",
    "corazón",
    "mano",
    "pie",
    "ojo",
    "boca",
    "mente",
    "cabeza",
    "cuerpo",
    "mente",
    "dinero",
    "negocio",
    "familia",
    "niño",
    "educación",
    "música",
    "arte",
    "naturaleza",
    "animal",
    "historia",
    "religión",
    "deporte",
    "trabajo",
    "movimiento",
    "libertad",
    "cambio",
    "desarrollo",
    "forma",
    "causa",
    "resultado",
    "proceso",
    "hecho",
    "sociedad",
    "cultura",
    "ley",
    "justicia",
    "política",
    "poder",
    "gobierno",
    "influencia",
    "futuro",
    "sentido",
    "educación",
    "conocimiento",
    "comunicación",
    "publicidad",
    "información",
    "importancia",
    "posibilidad",
    "problema",
    "solución",
    "encuentro",
    "experiencia",
    "viaje",
    "momento",
    "belleza",
    "peligro",
    "oportunidad",
    "sueño",
    "amor"
]

ids = []
for index in range(len(palabras)):
    ids.append(str(index + 1))

chroma_client = chromadb.Client()
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="TU_API_KEY",
    model_name="text-embedding-ada-002")


words_collection = chroma_client.create_collection(name="palabras", embedding_function=openai_ef)
words_collection.add(documents=palabras, ids=ids,)

result = words_collection.query(query_texts="el mejor amigo del hombre", n_results=5)
print(type(result['documents'][0]))
print(result['documents'][0])