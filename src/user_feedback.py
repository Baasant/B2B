# from langchain_community.llms import Ollama
# llm4generator_extractor= Ollama(model="llama2", temperature=0.7,base_url="http://host.docker.internal:11434")

from src.llm_instance import lama2_model

def user_feedback_fun(user_feedback,cv_data,job_description,current_letter):
        
        refinement_prompt = f"""
        The evaluator provided the following feedback on your previous cover letter:
        {user_feedback}

        Based on this feedback, refine the cover letter to improve its quality while addressing the issues highlighted.
        Ensure it remains professional and well-aligned with the job description.

        Here are the details for context:

        **Candidate's CV**:
        {cv_data}

        **Job Description**:
        {job_description}

        **Current Cover Letter**:
        {current_letter}

        Generate a new and improved version of the cover letter.
        
        you must only add the new cover letter dont add the feedback or job Description
        the cover letter must End with the candidate’s name as extracted for CV.

        """
        
        # Generate the refined cover letter
        refined_COV = lama2_model(refinement_prompt)
        print("refined_COV")
        # print(refined_COV)
        print("*****************************************************")
        return refined_COV