import streamlit as st
import subprocess
import tempfile
from datetime import datetime, timedelta

# -------------------- App Title --------------------
st.set_page_config(page_title="Interactive C++ Course", layout="wide")
st.title("📘 Interactive C++ Course for First-Year Students")

# -------------------- Sidebar Navigation --------------------
lesson_titles = [
    "Structure of a C++ Program",
    "Identifiers, Data Types, Operators, Structures",
    "Standard Libraries",
    "Control Structures",
    "Repetition Structures",
    "User Defined Functions",
    "Static and Dynamic Arrays, Vectors, Containers",
    "Inheritance",
    "Operator Overloading",
    "Recursion, Sorting & Searching"
]

lesson = st.sidebar.selectbox("Select a Lesson", lesson_titles)

# -------------------- Flashcard System --------------------
def show_flashcards(cards):
    st.subheader("🧠 Flashcards for Active Recall")
    if "card_index" not in st.session_state:
        st.session_state.card_index = 0

    question, answer = cards[st.session_state.card_index % len(cards)]
    st.markdown(f"**Q: {question}**")
    if st.button("Show Answer"):
        st.info(answer)
        st.session_state.card_index += 1

# -------------------- Quiz System --------------------
def show_quiz(quiz):
    st.subheader("📝 Quiz")
    for i, (question, options, answer) in enumerate(quiz):
        user_ans = st.radio(f"Q{i+1}: {question}", options, key=f"quiz_{i}")
        if user_ans == answer:
            st.success("Correct!")
        elif user_ans:
            st.error(f"Incorrect. Correct answer: {answer}")

# -------------------- Spaced Repetition Scheduling --------------------
def show_spaced_schedule():
    today = datetime.today()
    st.markdown("### ⏰ Spaced Repetition Schedule")
    st.write("Review this lesson on:")
    st.write(f"- Day 1: {today.strftime('%Y-%m-%d')}")
    st.write(f"- Day 3: {(today + timedelta(days=2)).strftime('%Y-%m-%d')}")
    st.write(f"- Day 7: {(today + timedelta(days=6)).strftime('%Y-%m-%d')}")

# -------------------- C++ Compiler --------------------
def run_cpp_code(code):
    with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as tmp_file:
        tmp_file.write(code.encode())
        tmp_file.flush()
        result = subprocess.run(["g++", tmp_file.name, "-o", tmp_file.name + ".out"], capture_output=True, text=True)
        if result.returncode != 0:
            return result.stderr
        run_result = subprocess.run([tmp_file.name + ".out"], capture_output=True, text=True)
        return run_result.stdout if run_result.returncode == 0 else run_result.stderr

# Lesson data loaded from lesson_data.py
from lesson_data import lessons  # Your existing lessons dictionary should be moved to a separate 'lesson_data.py'

lesson_data = lessons.get(lesson)
if lesson_data:
    st.header(f"📚 Lesson: {lesson}")
    st.subheader("📖 Reading")
    st.markdown(f"[Click here to read more]({lesson_data['reading']})")

    st.subheader("🎥 Explainer Video")
    st.video(lesson_data["video"])

    st.subheader("💻 Sample Code")
    st.code(lesson_data["code"], language="cpp")

    show_flashcards(lesson_data["flashcards"])

    if "quiz" in lesson_data:
        show_quiz(lesson_data["quiz"])

# -------------------- Practice Space --------------------
st.markdown("---")
st.subheader("🧪 Try It Yourself")
code_input = st.text_area("Write your C++ code below:", height=200, key="code_input")
if st.button("Run Code"):
    st.subheader("📤 Output")
    output = run_cpp_code(code_input)
    st.code(output)

# -------------------- Spaced Repetition Reminder --------------------
st.markdown("---")
show_spaced_schedule()
