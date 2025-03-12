# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# model = SentenceTransformer('all-MiniLM-L6-v2')
# def compute_bert_recall_confidence_score(cv, job_desc, cover_letter):
    
#     # get embeding of cv ,description and cover letter 
#     cv_embedding = model.encode(cv)
#     jd_embedding = model.encode(job_desc)
#     cl_embedding = model.encode(cover_letter)

#     combined_cv_jd = np.mean([cv_embedding, jd_embedding], axis=0)

#     # calculate the cos similarity 
#     similarity = cosine_similarity([combined_cv_jd], [cl_embedding])[0][0]
#     # return the similarity which is a confidence score about how accurate the generated cover letter
#     return similarity*100

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
# from src.llm_instance import SentenceTransformer_model
# Load BERT-based model
model = SentenceTransformer("all-MiniLM-L6-v2")

def read_text_file(file_path):
    """Reads a text file and returns its content as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def compute_bert_recall_confidence_score(cv_path, job_desc_path, cover_letter_path):
    """Computes the confidence score based on BERT embeddings."""
    
    # Read the text files
    cv = read_text_file(cv_path)
    job_desc = read_text_file(job_desc_path)
    cover_letter = read_text_file(cover_letter_path)
    
    # Get embeddings of CV, job description, and cover letter
    cv_embedding = model.encode(cv)
    jd_embedding = model.encode(job_desc)
    cl_embedding = model.encode(cover_letter)

    # Compute combined embedding of CV and job description
    combined_cv_jd = np.mean([cv_embedding, jd_embedding], axis=0)

    # Calculate cosine similarity
    similarity = cosine_similarity([combined_cv_jd], [cl_embedding])[0][0]

    # Return the similarity score as a percentage
    return int(similarity * 100)


