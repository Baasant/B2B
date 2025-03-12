# 📌 Overview

The Cover Letter Generator is a Streamlit-based web application that helps users generate customized cover letters by uploading their CV and job description. It utilizes a language model to create a tailored cover letter and allows users to provide feedback for refinement. The app also calculates a confidence score using BERT-based recall confidence scoring.

#🚀 Features

- **Upload your CV and Job Description in text format.

- **Generate a customized cover letter using an AI model.

- **View and download the generated cover letter.

- **Provide feedback to refine the cover letter further.

- **Calculate and display the confidence score of the generated output.

- **Download the refined cover letter after improvements.



# 🧠 Used Models 
- **llama 2 for 
    - Extracting data from the CV.
    - Generating the cover letter.
    - Taking feedback from the evaluator model and regenerating the cover letter based on the feedback.
- **deepseek-r1 a evalualtor 

# 🛠️ Installation & Setup

# Prerequisites
Ensure you have Python installed (preferably Python 3.9+). Also, install the required dependencies.

- Clone the Repository
- Create a Virtual Environment (Optional but Recommended)
```
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate    # On Windows
```
- Install Dependencies
```
pip install -r requirements.txt
```
- Running the App
```
python -m streamlit run app_main.py
```

# Run using Docker container
1. Build the Docker Image
```
docker build -t streamlit-app .
```
2. Run the Docker Container
```
docker run -p 8501:8501 streamlit-app
```
This maps port 8501 inside the container to port 8501 on your local machine, allowing you to access your Streamlit app at

🔗 http://localhost:8501