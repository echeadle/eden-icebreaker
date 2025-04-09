from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv.main import load_dotenv
import os

if __name__ == "__main__":
   load_dotenv()
   print("Hello Langchain")
   print(os.environ['KOOL_API_KEY'])