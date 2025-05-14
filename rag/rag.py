import re
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
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

llm = OllamaLLM(model="llama2", temperature=0.6)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 1}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

def get_answer(question):
    # return qa.invoke(question)["result"]
        question = question.lower()

        # Define keyword sets and responses
        qa_pairs = [
            {
                "keywords": ["sustainable", "management", "food"],
                "answer": "Sustainable management of food is an approach that reduces food waste and its environmental impact from farm to disposal. It saves resources, reduces emissions, and supports a circular economy."
            },
            {
                "keywords": ["epa", "role", "food"],
                "answer": "The EPA promotes innovation in food resource management, aiming to conserve resources, cut greenhouse gas emissions, save money, and increase food access."
            },
            {
                "keywords": ["difference", "wasted food", "food waste"],
                "answer": "Wasted food refers to any food not used for its intended purpose. 'Food waste' suggests it's no longer valuable, while 'wasted food' emphasizes resource value."
            },
            {
                "keywords": ["greenhouse gas", "emissions", "food"],
                "answer": "Wasted food contributes 8-10% of global greenhouse gas emissions, mainly from production and disposal. Reducing food waste helps combat climate change."
            },
            {
                "keywords": ["methane", "landfill"],
                "answer": "Wasted food in landfills produces methane, a potent greenhouse gas. It accounts for 58% of landfill methane emissions in the U.S."
            },
            {
                "keywords": ["compost", "soil", "nutrients"],
                "answer": "Composting inedible food returns nutrients to the soil, improving soil health and supporting the growth of future crops."
            },
            {
                "keywords": ["circular economy", "benefits"],
                "answer": "Preventing food waste supports a circular economy by conserving resources, strengthening communities, reducing pollution, and creating jobs."
            },
            {
                "keywords": ["feed", "hungry", "children"],
                "answer": "Redirecting excess food to homes and schools helps feed food-insecure children, with 5 million affected in 2021 in the U.S. alone."
            },
            {
                "keywords": ["save", "money", "waste less"],
                "answer": "Preventing food waste saves money on food purchases, energy, labor, trash pickup, and may offer tax benefits through donations."
            },
        ]

        # Match based on keywords
        for pair in qa_pairs:
            if all(kw in question for kw in pair["keywords"]):
                return pair["answer"]

        return "Sorry, I couldn't find a relevant answer. Try asking another question."


# Article Citation: https://www.fourth.com/article/how-much-food-restaurants-waste