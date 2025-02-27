from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')
def compute_bert_recall_confidence_score(cv, job_desc, cover_letter):
    
    # get embeding of cv ,description and cover letter 
    cv_embedding = model.encode(cv)
    jd_embedding = model.encode(job_desc)
    cl_embedding = model.encode(cover_letter)

    combined_cv_jd = np.mean([cv_embedding, jd_embedding], axis=0)

    # calculate the cos similarity 
    similarity = cosine_similarity([combined_cv_jd], [cl_embedding])[0][0]
    # return the similarity which is a confidence score about how accurate the generated cover letter
    return similarity*100

