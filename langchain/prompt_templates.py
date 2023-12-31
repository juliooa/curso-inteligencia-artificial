"""Using prompt templates """
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(openai_api_key='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')

SYSTEM_PROMPT = '''
Eres un asistente de servicio al cliente de un banco. 
Sabes muchos idiomas pero siempre respondes en el idioma del cliente.
En esta oportunidad el cliente habla {language}.
La consulta del cliente es:
"{user_question}"
'''
prompt_template = PromptTemplate.from_template(SYSTEM_PROMPT)
prompt = prompt_template.format(language='aleman', user_question='¿Cuánto dinero tengo en mi cuenta?')

result = llm.predict(prompt)
print(result)
