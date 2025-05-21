# cpp-course

Interactive C++ Course Streamlit Application

`main.py` launches a Streamlit web app that provides an interactive C++ learning experience tailored for first-year students. Key features include:

* Lesson navigation with videos and reading materials
* Flashcards for active recall and knowledge reinforcement
* Quizzes with instant feedback on multiple-choice questions
* A built-in C++ code editor and compiler interface for hands-on practice
* Spaced repetition schedule to optimize review intervals
* Practice workspace to write and run custom C++ code snippets locally

## Installation (macOS)

### Prerequisites

* macOS 10.13 or later with administrator access
* Homebrew ([https://brew.sh](https://brew.sh)) for package management
* Python 3.7 or higher

### Steps

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install Python 3**:

   ```bash
   brew install python3
   ```
3. **Clone this repository**:

   ```bash
   git clone <repository-url>
   cd cpp-course
   ```
4. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. **Upgrade pip and install Streamlit**:

   ```bash
   pip install --upgrade pip
   pip install streamlit
   ```
6. **(Optional) Install additional dependencies** if a `requirements.txt` file is provided:

   ```bash
   pip install -r requirements.txt
   ```
7. **Ensure a C++ compiler is available** (required for the code editor feature):

   ```bash
   brew install gcc
   ```

## Running the App Locally

With the virtual environment activated, run:

```bash
streamlit run main.py
```

Then, open your browser and navigate to `http://localhost:8501` to access the Interactive C++ Course application.
