import streamlit as st
from llm import feedback_loop
# Assuming these functions are defined in your script or imported from other modules
# You will need to define these functions or import them:
# - generate_cover_letter
# - evaluate_cover_letter
# - llm4generator_extractor
# - feedback_loop

def main():
    # Set up the Streamlit page layout
    st.set_page_config(page_title="cover Letter Generator", layout="wide")

    st.title("cover Letter Generator")
    st.write("Upload your CV and the Job Description to get a customized cover letter.")

    # Upload CV and Job Description as txt files
    cv_file = st.file_uploader("Upload your CV (Text format)", type=["txt"])
    job_file = st.file_uploader("Upload the Job Description (Text format)", type=["txt"])

    if cv_file and job_file:
        # Read the content of the uploaded files
        cv_data = cv_file.getvalue().decode("utf-8")
        job_description = job_file.getvalue().decode("utf-8")

        # Display the CV and Job Description content (optional)
        st.subheader("Candidate's CV")
        st.text(cv_data)

        st.subheader("Job Description")
        st.text(job_description)

        # Generate the cover letter and give the option to refine it
        if st.button("Generate cover Letter"):
            refined_letter = feedback_loop(cv_data, job_description)

            # Display the generated cover letter
            st.subheader("Generated cover Letter")
            st.text(refined_letter)

            # Allow users to download the generated cover letter as a .txt file
            st.download_button(
                label="Download cover Letter",
                data=refined_letter,
                file_name="cover_letter.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
