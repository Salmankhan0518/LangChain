from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model="nomic-embed-text", dimensions=32)

documents = [
    "Islamabad is capital of Pakistan",
    "Delhi is the capital of west bangal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))




