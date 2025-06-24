from langchain_community.document_loaders import TextLoader,WebBaseLoader
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

parser=StrOutputParser()

prompt1=PromptTemplate(template="give the answer of the ask {questions} from the {text}",
                       input_variables=['questions','text'])

url='https://www.daraz.pk/products/-i577223384-s2662294557.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A577223384%253Bsrc%253ALazadaMainSrp%253Brn%253A44bb6548f05b39a2253e2bd4fc163651%253Bregion%253Apk%253Bsku%253A577223384_PK%253Bprice%253A50000%253Bclient%253Adesktop%253Bsupplier_id%253A6005297952492%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7902%253Bitem_id%253A577223384%253Bsku_id%253A2662294557%253Bshop_id%253A1921424%253BtemplateInfo%253A1103_L%2523-1_A3_C%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Punjab&price=5E%204&priceCompare=skuId%3A2662294557%3Bsource%3Alazada-search-voucher%3Bsn%3A44bb6548f05b39a2253e2bd4fc163651%3BoriginPrice%3A5000000%3BdisplayPrice%3A5000000%3BsinglePromotionId%3A-1%3BsingleToolCode%3A-1%3BvoucherPricePlugin%3A0%3Btimestamp%3A1750766040522&ratingscore=&request_id=44bb6548f05b39a2253e2bd4fc163651&review=&sale=0&search=1&source=search&spm=a2a0e.searchlistcategory.list.0&stock=1'

loader=WebBaseLoader(url)

docs=loader.load()
# print(len(docs))

chain=prompt1|model|parser

result=chain.invoke({
    'questions': 'what is the product we are talking about ?',
    'text':docs[0].page_content
})

print(result)


