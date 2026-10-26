from langchain_ollama import ChatOllama


llm = ChatOllama(model="qwen2.5:3b")

result = llm.invoke("What is the capital of Pakistan")

print(result)


