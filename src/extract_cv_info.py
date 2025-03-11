from langchain_community.llms import Ollama
# llm4generator_extractor= Ollama(model="llama2", temperature=0.7,base_url="http://host.docker.internal:11434")
llm4generator_extractor= Ollama(model="llama2", temperature=0.7)
import os

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


    
# prompt4extract_data = f"""

# You are an intelligent assistant designed to extract structured data from a CV. Your task is to **analyze the entire CV** and extract **all relevant information**, ensuring that no key details are missed. If any information is unavailable, mark it as "Not Available." The extracted information should be formatted **clearly and concisely in plain text.**  

# ---

# ### **Data to Extract:**

# 1. **Name**  
#    - Extract the **full name** of the individual.

# 2. **Contact Information**  
#    - Email address  
#    - Phone number  

# 3. **Education History**  
#    - Degree(s) earned (e.g., Bachelor of Science in Computer Science)  
#    - Institution(s) attended (e.g., University of XYZ)  
#    - Year(s) of graduation, if available  

# 4. **Work Experience**  
#    Extract **all job experiences**, even if they are embedded within descriptions, projects, or skills sections. Ensure that each entry includes:  
#    - **Job Title** (e.g., Software Engineer)  
#    - **Company Name** (e.g., ABC Corp)  
#    - **Duration of Employment** (e.g., Jan 2020 – Dec 2022), if available  
#    - **Job Responsibilities & Achievements** (if available)  

#    🔹 **Include all experiences, even if they appear in different formats** (e.g., paragraphs, bullet points, or tables).  
#    🔹 **If a duration is missing, extract at least the job title and company.**  

# 5. **Skills**  
#    Extract **all mentioned skills**, including those found in job descriptions, project details, or other sections. Categorize them as follows:  
#    - **Programming Languages** (e.g., Python, C++, Java)  
#    - **Frameworks & Libraries** (e.g., TensorFlow, Flask, React)  
#    - **Tools & Technologies** (e.g., Docker, AWS, Git)  
#    - **Soft Skills** (e.g., Leadership, Communication, Problem-Solving)  

# ---

# ### **Output Format:**  
# Name: [Full Name]

# Contact Information:
# Email: [Email Address]
# Phone: [Phone Number]

# Education History:

# [Degree], [Institution], [Year of Graduation]
# [Degree], [Institution], [Year of Graduation]
# Work Experience:

# [Job Title], [Company], [Duration]
# Responsibilities:

# [Responsibility 1]
# [Responsibility 2]
# [Job Title], [Company], [Duration]
# Responsibilities:

# [Responsibility 1]
# [Responsibility 2]
# Skills:
# Programming Languages:

# [Skill 1]
# [Skill 2]
# Frameworks & Libraries:

# [Skill 1]
# [Skill 2]
# Tools & Technologies:

# [Skill 1]
# [Skill 2]
# Soft Skills:

# [Skill 1]
# [Skill 2]


# ---

# ### **Additional Instructions:**

# 1. **Ensure Thorough Analysis**  
#    - Examine **all sections**, including headers, bullet points, and paragraphs.  
#    - Extract work experience **even if not explicitly labeled** as "Work Experience."  

# 2. **Handle Multiple Entries**  
#    - Include **all** education and work experience entries.  

# 3. **Extract Implicit Skills**  
#    - Identify **skills hidden in job descriptions** and responsibilities.  

# 4. **Mark Missing Information**  
#    - If any detail (e.g., graduation year) is unavailable, output **"Not Available."**  

# 5. **Ensure Accuracy & Formatting**  
#    - Structure the output **cleanly and consistently.**  

# ---

# ### **Example CV Text**  

# Name: John Smith

# Contact Information:
# Email: john.smith@example.com
# Phone: +1 555 123 4567

# Education History:

# Master of Science in Computer Science, Stanford University, 2021
# Bachelor of Science in Electrical Engineering, MIT, 2019
# Work Experience:

# Senior Software Engineer, Tech Innovators Inc., Jan 2022 – Present
# Responsibilities:

# Led backend development for AI-driven products
# Improved system scalability by 40% using cloud technologies
# Software Engineer, CodeCraft LLC, Jun 2019 – Dec 2021
# Responsibilities:

# Developed web applications using React and Flask
# Optimized database queries to enhance performance
# Skills:
# Programming Languages:

# Python
# Java
# JavaScript
# Frameworks & Libraries:

# Flask
# React
# TensorFlow
# Tools & Technologies:

# Docker
# AWS
# Git
# Soft Skills:

# Leadership
# Team Collaboration
# Problem-Solving


# ---

# ### **Task:**  
# Now, extract the structured information from the following CV:



# """


# function used to run llm prompt to extract the data of the  cv file
def extract_cv_info_with_llm(cv_text,prompt4extract_data):
    # Define a prompt for the LLM to extract structured information
    prompt4extract_data=prompt4extract_data+cv_text
    # extract cv data
    cv_data = llm4generator_extractor(prompt4extract_data)
    return cv_data
    
# with open("cv.txt", "r") as file:
#     cv_text = file.read()

# cv_data = extract_cv_info_with_llm(cv_text,prompt4extract_data)
# print("Extracted CV Data:", cv_data)