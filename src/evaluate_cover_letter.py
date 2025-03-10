from langchain_community.llms import Ollama
# llm4eval= Ollama(model="deepseek-r1", temperature=0.7,base_url="http://host.docker.internal:11434")
llm4eval= Ollama(model="deepseek-r1", temperature=0.7)
# Function to evaluate the cover letter
def evaluate_cover_letter(cv_data, job_description, cover_letter):
    # Prepare the evaluation prompt
    evaluation_prompt = f"""
    Please evaluate the following cover letter based on the criteria listed below. For each point, provide a score from 1 (poor) to 5 (excellent), along with a brief explanation or examples supporting your score. Then, provide detailed feedback on the letter, including specific suggestions for improvement where necessary. Finally, include a summary stating whether the letter is **"Approved"** or **"Needs Improvement."**


    **Criteria for Evaluation:**  
    1. **Tailored to the Role/Context:**  
    - Does the letter address the specific job, role, or context clearly?  
    - Is it customized to the recipient (e.g., mentioning the company, university, or field of interest)?  

    2. **Strong Opening:**  
    - Does the letter start with an engaging introduction?  
    - Is the relationship between the writer and the subject of the letter clearly established?  

    3. **Showcases Value:**  
    - Does the letter effectively highlight the subject's key strengths, skills, or achievements?  
    - Are these strengths relevant to the context or role in question?  

    4. **Concrete Examples and Achievements:**  
    - Are specific examples or achievements mentioned to back up claims about the subject?  
    - Are these examples impactful and quantifiable (e.g., using metrics, measurable results)?  

    5. **Well-Structured and Concise:**  
    - Is the letter logically organized and easy to follow?  
    - Is it concise, avoiding unnecessary information while covering all critical points?  

    6. **Professional Tone and Authenticity:**  
    - Does the tone remain professional throughout the letter?  
    - Does the letter feel genuine and sincere in its praise?  

    7. **Strong Closing:**  
    - Does the letter end with a compelling summary and cover?  
    - Is there a clear call to action or offer for further communication?  

    8. **Error-Free and Polished:**  
    - Is the letter free from grammatical, spelling, or formatting errors?  
    - Does the formatting look clean and professional?  

    ---

    **Output Format:**  
    1. **Score for Each Criterion (1–5)**: Provide a score and brief explanation for each criterion.  
    2. **Detailed Feedback**:  
    - Highlight specific strengths of the letter.  
    - Identify areas needing improvement, with actionable suggestions for refinement.  
    3. **Summary**:  
    - Indicate whether the letter is **"Approved"** or **"Needs Improvement."**  
    - If **"Needs Improvement,"** explain what must be addressed to meet approval. 
 

   
    ---
Here are the needed data

        CV:
        {cv_data}
        
        Job Description:
        {job_description}
        
        cover Letter:
        {cover_letter}


        """

    # use the deepseek  model to evaluate the letter
    feedback = llm4eval(evaluation_prompt)
    return feedback


