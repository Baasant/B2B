#initalize llm model that used in the project to avoid reinitalize it each time
from langchain_community.llms import Ollama
from sentence_transformers import SentenceTransformer
#initalize models
deepseek_r1_model= Ollama(model="deepseek-r1", temperature=0.7)
lama2_model= Ollama(model="llama2", temperature=0.7)
SentenceTransformer_model = SentenceTransformer('all-MiniLM-L6-v2')
