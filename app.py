import streamlit as st
from utils import extract_text_from_pdf,summarize_text

st.set_page_config(page_title="StudyMate", layout="wide")

st.title("📚 StudyMate - Your Smart PDF Study Buddy")

uploaded_file = st.file_uploader("Upload your textbook or notes (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    if st.button("Extract & Summarize"):
        with st.spinner("Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)
            st.subheader("📄 Extracted Text")
            st.text(text[:1000])  # Preview

        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
            st.subheader("🧠 Summary")
            st.write(summary)
#calling from utils file
# app.py
import streamlit as st
from utils import generate_quiz_questions

st.title("Quiz Question Generator")

user_input = st.text_area("Enter study content:", height=500)

num_questions = st.slider("Number of questions", min_value=1, max_value=5, value=3)

if st.button("Generate Quiz Questions"):
    if user_input:
        questions = generate_quiz_questions(user_input, num_questions)
        st.subheader("Quiz Questions:")
        for i, q in enumerate(questions, start=1):
            st.markdown(f"**{i}.** {q}")
    else:
        st.warning("Please enter some study content.")
