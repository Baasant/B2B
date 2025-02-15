# %%
import spacy
from langchain_community.llms import Ollama

# %%
llm4generator_extractor= Ollama(model="llama2", temperature=0.7)
llm4eval= Ollama(model="deepseek-r1", temperature=0.7)


# %%
# Read job description from text file
# with open("Job Description1.txt", "r") as file:
#     job_description = file.read()

# with open("cv.txt", "r") as file:
#     cv_text = file.read()

# %%
prompt4extract_data = f"""
You are an intelligent assistant designed to extract structured data from a CV. Your task is to analyze the CV provided and extract the following information. If any information is missing, mark it as "Not Available." Provide the results in a clear and concise plain text format.

---

### Data to Extract:

1. **Name**: Extract the full name of the individual.
2. **Contact Information**:
   - Email address
   - Phone number
3. **Education History**:
   - Degree(s) earned (e.g., Bachelor of Science in Computer Science)
   - Institution(s) attended (e.g., University of XYZ)
   - Year(s) of graduation, if available
4. **Work Experience**:
   - Job title(s) (e.g., Software Engineer)
   - Company name(s) (e.g., ABC Corp)
   - Duration of employment (e.g., Jan 2020 – Dec 2022), if available
   - Include all experiences, even if they are brief or incomplete.
5. **Skills**:
   - List all skills mentioned in the CV, including:
     - Technical skills (e.g., Python, TensorFlow, Docker)
     - Tools and frameworks (e.g., React, Flask)
     - Programming languages (e.g., Java, C++)
     - Soft skills (e.g., teamwork, problem-solving)
   - Identify skills mentioned in any section of the CV, not just under a "Skills" heading.

---

### Output Format:

Return the extracted information in the following plain text format:
Name: [Full Name]

Contact Information:
Email: [Email Address]
Phone: [Phone Number]

Education History:

[Degree], [Institution], [Year of Graduation]

[Degree], [Institution], [Year of Graduation]

Work Experience:

[Job Title], [Company], [Duration]

[Job Title], [Company], [Duration]

Skills:

[Skill 1]

[Skill 2]

[Skill 3]


---

### Additional Instructions:

1. **Thorough Analysis**:
   - Analyze every section of the CV, including headers, bullet points, and paragraphs.
   - Extract information even if it is not explicitly labeled (e.g., skills mentioned in job descriptions).

2. **Multiple Entries**:
   - If the CV contains multiple entries for education or work experience, include all of them in the output.

3. **Skills Extraction**:
   - Extract all skills mentioned in the CV, including those embedded in job descriptions, project details, or other sections.
   - Include both technical and soft skills.

4. **Missing Information**:
   - If a field is missing (e.g., no graduation year for education), mark it as "Not Available."

5. **Be Precise**:
   - Ensure the extracted information is accurate and matches the content of the CV.

---


Example CV Text
Name: John Smith

Contact Information:
Email: john.smith@example.com
Phone: +1 555 123 4567

Education History:
- Master of Science in Computer Science, Stanford University, 2021
- Bachelor of Science in Electrical Engineering, MIT, 2019

Work Experience:
- Senior Software Engineer, Tech Innovators Inc., Jan 2022 – Present
- Software Engineer, CodeCraft LLC, Jun 2019 – Dec 2021

Skills:
- Python
- Java
- JavaScript
- Flask
- React
- TensorFlow
- Docker
- AWS
- Git
- Leadership
- Team Collaboration
- Problem Solving

Expected Output Using the Final Prompt
Name: John Smith

Contact Information:
Email: john.smith@example.com
Phone: +1 555 123 4567

Education History:
- Master of Science in Computer Science, Stanford University, 2021
- Bachelor of Science in Electrical Engineering, MIT, 2019

Work Experience:
- Senior Software Engineer, Tech Innovators Inc., Jan 2022 – Present
- Software Engineer, CodeCraft LLC, Jun 2019 – Dec 2021

Skills:
- Python
- Java
- JavaScript
- Flask
- React
- TensorFlow
- Docker
- AWS
- Git
- Leadership
- Team Collaboration
- Problem Solving

### Task:
For the following CV, extract the information, please:
"""

# %%
# Function to extract information from CV text using LLM
def extract_cv_info_with_llm(cv_text,prompt4extract_data):
    # Define a prompt for the LLM to extract structured information
    prompt4extract_data=prompt4extract_data+cv_text

    # Use the LLM to generate the structured output
    cv_data = llm4generator_extractor(prompt4extract_data)
    return cv_data
    
# with open("cv.txt", "r") as file:
#     cv_text = file.read()

# Extract information from the CV using LLM
# cv_data = extract_cv_info_with_llm(cv_text,prompt4extract_data)
# print("Extracted CV Data:", cv_data)

# %%
  # Prepare the prompt
prompt4genrator = f"""
I need a cover letter based on their CV and the job description provided. The letter should emphasize the candidate's relevant skills, 
experience, and achievements while tailoring the content to the requirements of the job. Below are the details:

"""

# %%
# Function to generate a cover letter
def generate_cover_letter(cv_data, job_description):
    # Prepare the prompt
    prompt = prompt4genrator+f"""
   
    CV:
    {cv_data}
    
    Job Description:
    {job_description}
    """

    # Generate the cover letter using LLaMA 2
    cover_letter = llm4generator_extractor(prompt)
    return cover_letter

# Generate the cover letter
# cover_letter = generate_cover_letter(cv_data, job_description)
# print("Generated cover Letter:\n", cover_letter)

# %%
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

    # Use the LLaMA model to evaluate the letter
    feedback = llm4eval(evaluation_prompt)
    return feedback


# %%
# Feedback loop to refine the cover letter
def feedback_loop(cv_text, job_description, max_iterations=2):
    cv_data = extract_cv_info_with_llm(cv_text,prompt4extract_data)
# print("Extracted CV Data:", cv_data)
    current_letter = generate_cover_letter(cv_data, job_description)
    
    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}: Evaluating the letter...\n")
        
        # Get feedback from the evaluator
        feedback = evaluate_cover_letter(cv_data, job_description, current_letter)
        
        # Display feedback
        print(f"Feedback from evaluator:\n{feedback}\n")
        
        # Check if the letter is approved
        if "Approved" in feedback:
            print("The letter has been approved!")
            return current_letter
        
        else:
            print("reed modification...................")
            # If not approved, refine the letter based on feedback
            refinement_prompt = f"""
            The evaluator provided the following feedback on your previous letter:
            {feedback}

            Based on this feedback, refine the cover letter to address the issues and improve its quality. 
            Here are the original details for context:

            **Candidate's CV**:
            {cv_data}

            **Job Description**:
            {job_description}

            **Previous cover Letter**:
            {current_letter}

            Refine the letter while maintaining a professional tone and aligning it with the feedback.
            """
            current_letter = llm4generator_extractor(refinement_prompt)

    print("Max iterations reached. Returning the latest version of the letter.")
    return current_letter

# %%
# cover_letter=feedback_loop(cv_data, job_description, max_iterations=2)
# with open("cover_letter4all.txt", "w") as file:
#     file.write(cover_letter)

# %%
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch

# # Load pre-trained GPT-2 model and tokenizer
# model_name = "gpt2"
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# # Calculate perplexity
# def calculate_perplexity(text):
#     inputs = tokenizer(text, return_tensors="pt")
#     with torch.no_grad():
#         outputs = model(**inputs, labels=inputs["input_ids"])
#         loss = outputs.loss
#         perplexity = torch.exp(loss)
#     return perplexity.item()

# # Example generated text
# # Read job description from text file
# with open("cover_letter4all.txt", "r") as file:
#     cover_letter = file.read()

# perplexity = calculate_perplexity(cover_letter)
# print("Perplexity:", perplexity)

# %%
# import textstat

# # Calculate Flesch-Kincaid readability score
# def calculate_readability(text):
#     return textstat.flesch_reading_ease(text)

# # Example generated text
# readability = calculate_readability(cover_letter)
# print("Readability Score:", readability)

# %%



