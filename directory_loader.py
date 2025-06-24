# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# import os 
# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader


loader=DirectoryLoader(
    path='papers',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
print(len(docs))
print(docs)
