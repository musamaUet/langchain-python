from langchain import LLMChain
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory
from dotenv import load_dotenv
import os

api_key = os.getenv('OPENAI_API_KEY')

print(f'key Muhammad {api_key}')

load_dotenv()

chat = ChatOpenAI(openai_api_key=api_key)
# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory("messages.json"),
#     memory_key="messages",
#     return_messages=True
#     )
memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat
)
prompt = ChatPromptTemplate(
    input_variables=['content'],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory
)

while True:
    content = input(">> ")
    
    result = chain({'content': content})
    print(result['text'])