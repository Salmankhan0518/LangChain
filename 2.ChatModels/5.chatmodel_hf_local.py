from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os

os.environ["HF_HOME"] = 'D:/AI/HuggingFace_textGeneration'

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    task="text-generation",
    pipeline_kwargs= dict(
        temperature=0.7,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke('What is the capital of pakistan')

print(result.content)