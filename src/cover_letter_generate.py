from langchain_community.llms import Ollama
# llm4generator_extractor= Ollama(model="llama2", temperature=0.7,base_url="http://host.docker.internal:11434")
llm4generator_extractor= Ollama(model="llama2", temperature=0.7)
 # Prepare the prompt
phase1_prompt4genrator = f"""
I need a cover letter based on their CV and the job description provided. The letter should emphasize the candidate's relevant skills, 
experience, and achievements while tailoring the content to the requirements of the job. Below are the details:
"""

# Function to generate a cover letter
def generate_cover_letter(cv_data, job_description):
    # concate all the info for the project
    prompt = phase1_prompt4genrator+f"""
   
    CV:
    {cv_data}
    
    Job Description:
    {job_description}

    you must ensure that it concludes with the CV owner's name as extracted from the CV. The name should appear at the very end of the letter.


    """
    # Generate using  llama 2
    cover_letter = llm4generator_extractor(prompt)
    return cover_letter


# # generate the cover letter
# cover_letter = generate_cover_letter(cv_data, job_description)
# print("Generated cover Letter:\n", cover_letter)

# regenerate a cover letter based on feedback from evaluator

def refined_cover_letter(feedback,cv_data,job_description,current_letter):
        refinement_prompt = f"""
        The evaluator provided the following feedback on your previous cover letter:
        {feedback}

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
        you must ensure that it concludes with the CV owner's name as extracted from the CV. The name should appear at the very end of the letter.


        """
        
        # Generate the refined cover letter
        current_letter = llm4generator_extractor(refinement_prompt)
        return current_letter