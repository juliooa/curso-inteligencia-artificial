import os
import openai

def query_llm(question, relevant_documents):

    information =''
    for document in relevant_documents:
        information+=document.content + '\n'

    pages = ','.join([doc.metadata["page_number"] for doc in relevant_documents])

    prompt = f'''
    Using ONLY the given information, answer the user's question.
    If you can't know the answer with the given information, say that you don't know,
    don't try to guess the answer or invent new information.
    If you find the answer in the documents, include the following text after your answer:
    The information is in pages: {pages}

    Example:
    Assistant: The answer is...
    The information is in pages: 1,2,3
    
    Example:
    Assistant: I can't find the answer in information provided.

    This is the information:
    {information}
    '''

    openai.api_key = os.getenv("OPEN_AI_API_KEY")
    response = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[
            {"role":"system","content":prompt},
            {"role":"user","content":question}
        ]
    )
    return response.choices[0].message.content


