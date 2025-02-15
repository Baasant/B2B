import evaluate_cover_letter
import extract_cv_info

def feedback_loop(cv_data, job_description, max_iterations=2):
    current_letter = generate_cover_letter(cv_data, job_description)

    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}: Evaluating the letter...\n")
        # get the feedback 
        feedback = evaluate_cover_letter(cv_data, job_description, current_letter)
        
        # Display feedback
        # print(f"Feedback from evaluator:\n{feedback}\n")
        
        # Check if the letter is approved
        if "Approved" in feedback:
            print("The letter has been approved")
            return current_letter
    
        else:
            print("Refining the cover letter based on feedback...\n") 
            print("****************************************************************")
            current_letter=refined_cover_letter(feedback,cv_data,job_description,current_letter)

    print("Max iterations reached. Returning the latest version of the letter.")
    return current_letter
