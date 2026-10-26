from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model="nomic-embed-text", dimensions=32)

result = embedding.embed_query("Islamabad is capital of Pakistan")

print(str(result))