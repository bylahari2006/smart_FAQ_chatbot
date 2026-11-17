
import streamlit as st
import ollama

# Page title
st.title("🎓 Smart FAQ Chatbot")
st.write("Ask questions about your course syllabus!")

# Read syllabus file
with open("syllabus.txt", "r", encoding="utf-8") as file:
    syllabus = file.read()

# Function to get AI answer
def get_answer(question):

    prompt = f"""
    You are a college syllabus FAQ chatbot.

    Answer the student's question using
    ONLY the syllabus given below.

    If the answer is not available,
    say: "Sorry, this information is not
    available in the syllabus."

    Syllabus:
    {syllabus}

    Student Question:
    {question}

    Answer:
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


# Chat input
question = st.chat_input("Enter your question")

if question:

    st.write("You:", question)

    with st.spinner("AI is thinking..."):
        try:
            answer = get_answer(question)
            st.write("🤖 Chatbot:", answer)

        except Exception:
            st.error(
                "Please check whether Ollama is running "
                "and Llama 3.2 is installed."
            )
