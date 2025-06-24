from langchain_community.document_loaders import TextLoader
# from langchain_community.document_loaders.chatgpt import ChatGPTLoader
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.document_loaders import TextLoader

