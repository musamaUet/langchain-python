from langchain import LLMChain
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
import os

api_key = os.getenv('OPENAI_API_KEY')

print(f'key Muhammad {api_key}')

load_dotenv()

chat = ChatOpenAI(openai_api_key=api_key)

prompt = ChatPromptTemplate(
    input_variables=['content'],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt
)

while True:
    content = print(">> ")
    
    result = chain({'content': content})
    print(result['text'])