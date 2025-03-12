# from langchain_community.llms import Ollama
# llm4generator_extractor= Ollama(model="llama2", temperature=0.7,base_url="http://host.docker.internal:11434")
# llm4generator_extractor= Ollama(model="llama2", temperature=0.7)
import os
from src.llm_instance import lama2_model
main_directory = os.getcwd()  
prompt_dir  = "prompts"  
file_name = "data_extract_prompt.txt"  

file_path = os.path.join(main_directory, prompt_dir, file_name)

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        prompt4extract_data = file.read()
   #  print(content)
else:
    print("File does not exist!")



# function used to run llm prompt to extract the data of the  cv file
def extract_cv_info_with_llm(cv_text,prompt4extract_data):
    # Define a prompt for the LLM to extract structured information
    prompt4extract_data=prompt4extract_data+cv_text
    # extract cv data
    cv_data = lama2_model(prompt4extract_data)
    return cv_data
    
# with open("cv.txt", "r") as file:
#     cv_text = file.read()

# cv_data = extract_cv_info_with_llm(cv_text,prompt4extract_data)
# print("Extracted CV Data:", cv_data)