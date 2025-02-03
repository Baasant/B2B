# import streamlit as st
# from integrate_module import *
# from user_feedback import *

# def main():
#     # Set up the Streamlit page layout
#     st.set_page_config(page_title="cover Letter Generator", layout="wide")

#     st.title("cover Letter Generator")
#     st.write("Upload your CV and the Job Description to get a customized cover letter.")

#     # Upload CV and Job Description as txt files
#     cv_file = st.file_uploader("Upload your CV (Text format)", type=["txt"])
#     job_file = st.file_uploader("Upload the Job Description (Text format)", type=["txt"])

#     if cv_file and job_file:
#         # Read the content of the uploaded files
#         cv_text = cv_file.getvalue().decode("utf-8")
#         job_description = job_file.getvalue().decode("utf-8")

#         # Display the CV and Job Description content (optional)
#         st.subheader("Candidate's CV")
#         st.text(cv_text)

#         st.subheader("Job Description")
#         st.text(job_description)

#         # Generate the cover letter and give the option to refine it
#         if st.button("Generate cover Letter"):
#             refined_letter = feedback_loop(cv_text, job_description, max_iterations=1)

#             # Display the generated cover letter
#             st.subheader("Generated cover Letter")
#             st.text(refined_letter)

#             # Allow users to download the generated cover letter as a .txt file
#             st.download_button(
#                 label="Download cover Letter",
#                 data=refined_letter,
#                 file_name="cover_letter.txt",
#                 mime="text/plain"
#             )

# if __name__ == "__main__":
#     main()
import streamlit as st
from integrate_module import *
from user_feedback import *
from langchain_community.llms import Ollama

# Initialize LLM
llm4generator_extractor = Ollama(model="llama2", temperature=0.7)

def main():
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
            st.session_state.cover_letter = feedback_loop(cv_text, job_description, max_iterations=1)

        # Display cover letter if available
        if st.session_state.cover_letter:
            st.subheader("Generated Cover Letter")
            st.text(st.session_state.cover_letter)

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



