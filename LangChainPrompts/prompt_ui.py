from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

model = ChatOllama(model="qwen2.5:3b")

st.header('Reasearch Tool')

user_input = st.text_input( "Enter your prompt" )

if st.button('Summerize'):
    st.text('Some random text ')
    result = model.invoke(user_input)
    st.write(result.content)