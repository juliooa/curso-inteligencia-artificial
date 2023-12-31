import os
import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.llms.openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import streamlit as st

def process_pdf(path):
    pdf_loader = PyPDFLoader(path)
    documents = pdf_loader.load_and_split()
    vectordb = Chroma.from_documents(documents, SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"))
    return vectordb

def main():
    st.title("The Book Reader 📖")
    pdf = st.file_uploader("Sube tu libro en formato PDF", type=["pdf"])
    if pdf is not None:
        with tempfile.TemporaryDirectory() as tmpdir:
            pdf_path = os.path.join(tmpdir, pdf.name)
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf.read())
            
            vectordb = process_pdf(pdf_path)
            query = st.text_input("Pregúntame algo sobre el libro")
            if query:
                result_docs = vectordb.similarity_search(query, k=3)
                llm = OpenAI(openai_api_key="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")
                chain = load_qa_chain(llm, verbose=True)
                with get_openai_callback() as cost:
                    response = chain.run(input_documents=result_docs, question=query, verbose=True)
                    print(cost)
                    print(response)
                    st.write(response)

if __name__ == "__main__":
    main()

