'''Learning to use chains'''
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain


llmOpenAI = ChatOpenAI(openai_api_key="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")

prompt1 = ChatPromptTemplate.from_template(
    "Sugiereme un nombre para una empresa \
     que produce {product}?")

chain1 = LLMChain(llm=llmOpenAI, prompt=prompt1, output_key="company_name")


prompt2 = ChatPromptTemplate.from_template(
    "Escribe un tagline para una empresa llamada {company_name}")
chain2 = LLMChain(llm=llmOpenAI, prompt=prompt2)

simple_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

result = simple_chain.run("aceite de oliva")
print(result)
