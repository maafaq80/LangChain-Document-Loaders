from langchain_community.document_loaders import TextLoader
# from langchain_community.document_loaders.chatgpt import ChatGPTLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini" ,
                 openai_api_key=api_key)


prompt=PromptTemplate(template="summarize the text {input}",
                      input_variables=['input'])

parser=StrOutputParser()

loader=TextLoader('cricket.txt' ,encoding='utf-8')
docs=loader.load()

text=RunnableLambda(
    (lambda _:loader.load()[0].page_content)
)

chain=text|prompt|model|parser
result=chain.invoke({
    
})

print(result)

