from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformers

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "islamabad is the capital of pakistan"

document = [
    "Pakistan is a country in South Asia.",
    "Islamabad is the capital of Pakistan.",
    "The largest city in Pakistan is Karachi."
]

vectors = embeddings.embed_documents(document)

print(str(vectors))