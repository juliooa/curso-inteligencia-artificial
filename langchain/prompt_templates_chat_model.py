"""Using chat prompt templates """
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(openai_api_key='TU_API_KEY')

SYSTEM_PROMPT = '''
Eres un asistente de servicio al cliente de un banco. 
Sabes muchos idiomas pero siempre respondes en el idioma del cliente.
En esta oportunidad el cliente habla {language}.
El usuario se llama {user_name}
'''

chat_template = ChatPromptTemplate.from_messages([
    ("system",SYSTEM_PROMPT),
    ("user", "{user_question}")
])

messages = chat_template.format_messages(language='español',
                                         user_question="¿Cuánto dinero tengo en mi cuenta?",
                                         user_name="Julio")

response = chat(messages)
print(response)
