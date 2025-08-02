import fitz  # PyMuPDF
from transformers import pipeline

# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]  # summarization models have input limits
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
#quiz questions
# utils.py
from transformers import pipeline

question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def generate_quiz_questions(context, num_questions=3):
    input_text = f"generate question: {context}"
    results = question_generator(
        input_text,
        max_length=64,
        num_return_sequences=num_questions,
        do_sample=True,  # allows variety
        top_k=50,         # controls diversity
    )
    return [r['generated_text'] for r in results]
