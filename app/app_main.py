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
#             refined_letter = feedback_loop(cv_text, job_description, max_iterations=2)

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

def main():
    # Set up the Streamlit page layout
    st.set_page_config(page_title="Cover Letter Generator", layout="wide")

    st.title("Cover Letter Generator")
    st.write("Upload your CV and the Job Description to get a customized cover letter.")

    # Upload CV and Job Description as txt files
    cv_file = st.file_uploader("Upload your CV (Text format)", type=["txt"])
    job_file = st.file_uploader("Upload the Job Description (Text format)", type=["txt"])

    if cv_file and job_file:
        # Read the content of the uploaded files
        cv_text = cv_file.getvalue().decode("utf-8")
        job_description = job_file.getvalue().decode("utf-8")
        cv_data=extract_cv_info_with_llm(cv_text,prompt4extract_data)

        # Display the CV and Job Description content (optional)
        st.subheader("Candidate's CV")
        st.text(cv_text)

        st.subheader("Job Description")
        st.text(job_description)

        # Generate the cover letter and give the option to refine it
        if st.button("Generate cover Letter"):
            # Generate the initial cover letter
            refined_letter = feedback_loop(cv_text, job_description, max_iterations=1)

            # Display the generated cover letter
            st.subheader("Generated Cover Letter")
            st.text(refined_letter)

            # Allow users to download the generated cover letter as a .txt file
            st.download_button(
                label="Download Cover Letter",
                data=refined_letter,
                file_name="cover_letter.txt",
                mime="text/plain"
            )

            # Feedback section: let the user provide feedback
            st.subheader("Provide Feedback to Improve the Cover Letter")
            user_feedback = st.text_area("Enter your feedback on the cover letter", "")

            # When user submits feedback
            if st.button("Submit Feedback"):
                if user_feedback:
                    # Call the user_feedback_fun function to process feedback and refine the letter
                    new_refined_letter = user_feedback_fun(user_feedback,cv_data,job_description,refined_letter)
                    

                    # Display the new refined cover letter after feedback
                    st.subheader("Refined Cover Letter After user Feedback")
                    st.text(new_refined_letter)

                    # Allow users to download the refined cover letter
                    st.download_button(
                        label="Download Refined Cover Letter",
                        data=new_refined_letter,
                        file_name="refined_cover_letter.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Please provide your feedback before submitting.")

if __name__ == "__main__":
    main()
