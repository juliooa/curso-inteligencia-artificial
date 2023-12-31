from langchain.llms.openai import OpenAI

llm = OpenAI(openai_api_key='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')
result = llm.predict("La mejor forma de empezar el día es ")
print(result)