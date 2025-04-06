from dotenv import load
from dotenv.main import load_dotenv
import os

if __name__ == "__main__":
   load_dotenv()
   print("Hello Langchain")
   print(os.environ['KOOL_API_KEY'])