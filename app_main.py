from src.confidence_score import compute_bert_recall_confidence_score
import streamlit as st
from src.integrate_module import feedback_loop
from src.user_feedback import user_feedback_fun
# from integrate_module import *
# from user_feedback import *
from langchain_community.llms import Ollama
import os

# Initialize LLM
# llm4generator_extractor = Ollama(model="llama2", temperature=0.7,base_url="http://host.docker.internal:11434")

def main():
#     #read the eva prompt
#     main_directory = os.getcwd()  
#     prompt_dir  = "prompts"  
#     file_name = "evaluate_prompt.txt"  

#     file_path = os.path.join(main_directory, prompt_dir, file_name)

#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as file:
#             evaluation_prompt = file.read()
#    #  print(content)
#     else:
#         print("File does not exist!")

    st.set_page_config(page_title="Cover Letter Generator", layout="wide")
    st.title("Cover Letter Generator")
    st.write("Upload your CV and the Job Description to get a customized cover letter.")

    # Upload CV and Job Description
    cv_file = st.file_uploader("Upload your CV (Text format)", type=["txt"])
    job_file = st.file_uploader("Upload the Job Description (Text format)", type=["txt"])

    # Store generated cover letter in session state
    if "cover_letter" not in st.session_state:
        st.session_state.cover_letter = ""

    if cv_file and job_file:
        cv_text = cv_file.getvalue().decode("utf-8")
        job_description = job_file.getvalue().decode("utf-8")

        st.subheader("Candidate's CV")
        st.text(cv_text)

        st.subheader("Job Description")
        st.text(job_description)

        # Generate cover letter
        if st.button("Generate Cover Letter"):
            st.session_state.cover_letter = feedback_loop(cv_text, job_description, max_iterations=5)
            st.session_state.confidence_score = compute_bert_recall_confidence_score(cv_text, job_description, st.session_state.cover_letter)


        # Display cover letter if available
        if st.session_state.cover_letter:
            st.subheader("Generated Cover Letter")
            st.text(st.session_state.cover_letter)
            with st.container():
                st.markdown("### :chart_with_upwards_trend: The Confidence Level of the Generated Output")
                st.metric(label="Confidence Score", value=f"{st.session_state.confidence_score:.2f}")

            # Allow users to download the cover letter
            st.download_button(
                label="Download Cover Letter",
                data=st.session_state.cover_letter,
                file_name="cover_letter.txt",
                mime="text/plain"
            )
            

            # Feedback input section
            st.subheader("Provide Feedback")
            user_feedback = st.text_area("Enter your feedback to refine the cover letter:")
 
            # Submit feedback and regenerate cover letter
            if st.button("Submit Feedback"):
                if user_feedback.strip():
                    refined_letter = user_feedback_fun(user_feedback, cv_text, job_description, st.session_state.cover_letter)
                    st.session_state.cover_letter = refined_letter  # Update session state

                    # Display the refined cover letter
                    st.subheader("Refined Cover Letter")
                    st.text(refined_letter)
                    st.session_state.confidence_score = compute_bert_recall_confidence_score(cv_text, job_description, refined_letter)

                    with st.container():
                        st.markdown("### :chart_with_upwards_trend: The Confidence Level of the Generated Output")
                        st.metric(label="Confidence Score", value=f"{st.session_state.confidence_score:.2f}")


                    # Allow users to download the refined cover letter
                    st.download_button(
                        label="Download Refined Cover Letter",
                        data=refined_letter,
                        file_name="refined_cover_letter.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Please enter feedback before submitting.")

if __name__ == "__main__":
    main()



