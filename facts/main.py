from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstore.chroma import Chroma
from dotenv import load_dotenv
import os

api_eky = os.getenv('OPENAI_API_KEY')

embeddings = OpenAIEmbeddings()
emb = embeddings.embed_query("Hi There")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

print(docs)