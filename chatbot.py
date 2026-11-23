from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model='qwen2.5:3b')

messages=[
    SystemMessage(content='You are a helpful assistant')
]

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)


print(chat_history)

