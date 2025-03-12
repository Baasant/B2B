# from langchain_community.llms import Ollama
# llm4eval= Ollama(model="deepseek-r1", temperature=0.7,base_url="http://host.docker.internal:11434")
# llm4eval= Ollama(model="deepseek-r1", temperature=0.7)
# Function to evaluate the cover letter

from src.llm_instance import deepseek_r1_model

def load_prompt_template(file_path="prompts/evaluate_prompt.txt"):
    """Reads the evaluation prompt template from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def evaluate_cover_letter(cv_data, job_description, cover_letter, prompt_file="prompts/evaluate_prompt.txt"):
    # Load the evaluation prompt from the file
    prompt_template = load_prompt_template(prompt_file)
    evaluation_prompt = prompt_template.format(
        cv_data=cv_data,
        job_description=job_description,
        cover_letter=cover_letter
    )
    feedback = deepseek_r1_model(evaluation_prompt)
    return feedback



