import re
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from pymongo import MongoClient
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain.prompts import PromptTemplate
from langchain_community.llms import ollama
from langchain.chains import RetrievalQA

# Create client and collection for mongo connection
client = MongoClient(st.secrets["mongo"]["URI"])
db = client["vector-store"]
collection = client["vector-store"]["embeddings"]

# Create embeddings with FastEmbed
embeddings = FastEmbedEmbeddings()

# Load iff collection is empty
if collection.count_documents({}) == 0:
    # Load PDF file 
    loader = PyPDFLoader("Food_Sus.pdf")
    pages = loader.load()

    # Split docs into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(pages)

    # Clean up text: Remove punc and #s
    for text in texts:
        text.page_content = re.sub(r'[^\w %]|_', '', text.page_content, flags=re.UNICODE)
        print(text.page_content)

    # Store docs in mongo
    docsearch = MongoDBAtlasVectorSearch.from_documents(texts, embeddings, collection=collection)

else:
    # Load existing data
    docsearch = MongoDBAtlasVectorSearch(embedding=embeddings, collection=collection)

# Custom prompt template for LLM to know how to approach a question
custom_prompt_template = '''Consider the following article:

{context}

Now, based on the article, answer the following question:

{question}

Provide a concise and accurate response below. If you cannot answer the question based on the article, say "I'm not sure I can answer this. I'd happy to answer question about promoting food sustainability though!".

'''

prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

llm = ollama.Ollama(model="llama2", temperature=0.6)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 1}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

def get_answer(question):
    return qa.invoke(question)["result"]


# Article Citation: https://www.fourth.com/article/how-much-food-restaurants-waste