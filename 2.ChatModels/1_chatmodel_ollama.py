from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:3b")

result = model.invoke("What is the capital of Pakistan")

print(result.content)


