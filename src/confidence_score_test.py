# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
# # from src.llm_instance import SentenceTransformer_model
# # Load BERT-based model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# def read_text_file(file_path):
#     """Reads a text file and returns its content as a string."""
#     with open(file_path, "r", encoding="utf-8") as file:
#         return file.read()

# def compute_bert_recall_confidence_score(cv_path, job_desc_path, cover_letter_path):
#     """Computes the confidence score based on BERT embeddings."""
    
#     # Read the text files
#     cv = read_text_file(cv_path)
#     job_desc = read_text_file(job_desc_path)
#     cover_letter = read_text_file(cover_letter_path)
    
#     # Get embeddings of CV, job description, and cover letter
#     cv_embedding = model.encode(cv)
#     jd_embedding = model.encode(job_desc)
#     cl_embedding = model.encode(cover_letter)

#     # Compute combined embedding of CV and job description
#     combined_cv_jd = np.mean([cv_embedding, jd_embedding], axis=0)

#     # Calculate cosine similarity
#     similarity = cosine_similarity([combined_cv_jd], [cl_embedding])[0][0]

#     # Return the similarity score as a percentage
#     return int(similarity * 100)


import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load BERT-based model
model = SentenceTransformer("all-MiniLM-L6-v2")

def read_text_file(file_path):
    """Reads a text file and returns its content as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        sys.exit(1)

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

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python src/confidence_score_test.py <cv_path> <job_desc_path> <cover_letter_path>")
        sys.exit(1)

    cv_path = sys.argv[1]
    job_desc_path = sys.argv[2]
    cover_letter_path = sys.argv[3]

    score = compute_bert_recall_confidence_score(cv_path, job_desc_path, cover_letter_path)
    print(score)  # Print confidence score
