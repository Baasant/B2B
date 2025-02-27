from  src.evaluate_cover_letter import evaluate_cover_letter
from src.extract_cv_info import extract_cv_info_with_llm ,prompt4extract_data
from  src.cover_letter_generate import refined_cover_letter,generate_cover_letter

def feedback_loop(cv_text, job_description, max_iterations=2):
    cv_data=extract_cv_info_with_llm(cv_text,prompt4extract_data)
    current_letter = generate_cover_letter(cv_data, job_description)

    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}: Evaluating the letter...\n")
        # get the feedback 
        feedback = evaluate_cover_letter(cv_data, job_description, current_letter)
        
        
        # Check if the letter is approved
        if "Approved" in feedback:
            print("The letter has been approved")
            return current_letter
    
        else:
            print("Refining the cover letter based on evaluator...\n") 
            print("****************************************************************")
            refined_letter=refined_cover_letter(feedback,cv_data,job_description,current_letter)

    print("Max iterations reached. Returning the latest version of the letter.")
    return refined_letter


