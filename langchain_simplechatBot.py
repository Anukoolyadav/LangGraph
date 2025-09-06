# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage , HumanMessage,SystemMessage

import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
model=ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-1.5-flash")

chatHistory=[
    SystemMessage(content='you are a good Ai assistant')
]

while True:
    user_input=input('YOU : ')
    chatHistory.append(HumanMessage(content=user_input))
    if(user_input=='exit'):
        break
    result=model.invoke(chatHistory)
    chatHistory.append(AIMessage(content=result.content))
    print('AI : ',result.content)

print(chatHistory)
