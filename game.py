import streamlit as st
import random
import time

# Define the quiz questions, options, and correct answers
questions = (
    "How many elements are there in the periodic table?: ",
    "Which is the most abundant gas in Earth's atmosphere?: ",
    "What is the chemical symbol for gold?: ",
    "What is the process by which water moves through a plant, from the roots to the leaves?: ",
    "Which planet is the hottest?: ",
    "What is the capital of France?: ",
    "Who wrote 'To Kill a Mockingbird'?: ",
    "Which is the largest mammal on Earth?: ",
    "What year did the Titanic sink?: ",
    "Who painted the Mona Lisa?: ",
    "What is the currency of Japan?: ",
    "Which country is known as the Land of the Rising Sun?: ",
    "What is the largest organ in the human body?: ",
    "What is the tallest mountain in the world?: ",
    "Who invented the telephone?: ",
    "Which is the only metal that is liquid at room temperature?: ",
    "What is the smallest planet in our solar system?: ",
    "Which element is diamond composed of?: ",
    "Who discovered penicillin?: ",
    "What is the hardest natural substance on Earth?: "
)

options = (
    ("A. 116", "B. 118", "C. 120", "D. 20"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Argon"),
    ("A. Au", "B. Ag", "C. Fe", "D. Pb"),
    ("A. Transpiration", "B. Photosynthesis", "C. Respiration", "D. Evaporation"),
    ("A. Venus", "B. Mercury", "C. Earth", "D. Mars"),
    ("A. London", "B. Paris", "C. Berlin", "D. Rome"),
    ("A. Harper Lee", "B. J.K. Rowling", "C. Jane Austen", "D. Charles Dickens"),
    ("A. Elephant", "B. Blue whale", "C. Giraffe", "D. Polar bear"),
    ("A. 1912", "B. 1921", "C. 1905", "D. 1933"),
    ("A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"),
    ("A. Yen", "B. Yuan", "C. Won", "D. Rupee"),
    ("A. China", "B. Korea", "C. Japan", "D. Vietnam"),
    ("A. Liver", "B. Brain", "C. Skin", "D. Heart"),
    ("A. Mount Everest", "B. K2", "C. Mount Kilimanjaro", "D. Mount Fuji"),
    ("A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Guglielmo Marconi"),
    ("A. Mercury", "B. Gold", "C. Iron", "D. Lead"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Carbon", "B. Silicon", "C. Oxygen", "D. Nitrogen"),
    ("A. Alexander Fleming", "B. Isaac Newton", "C. Albert Einstein", "D. Thomas Edison"),
    ("A. Gold", "B. Diamond", "C. Titanium", "D. Quartz")
)

answers = (
    "B", "B", "A", "A", "A", "B", "A", "B", "A", "A",
    "A", "C", "C", "A", "A", "B", "B", "A", "A", "B"
)

# Initialize score and guesses
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = ""
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

# Function to start the quiz
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.start_time = time.time()  # Start the timer
    st.session_state.question_num = 0  # Reset question number
    st.session_state.score = 0  # Reset score
    st.session_state.guesses = []  # Reset guesses

# Function to handle user input and timer
def submit_answer():
    elapsed_time = time.time() - st.session_state.start_time
    if elapsed_time > 10:
        st.warning("Time's up! You took too long to answer this question.")
        st.session_state.selected_answer = ""  # Reset selected answer
        return
    
    guess = st.session_state.selected_answer
    st.session_state.guesses.append(guess)
    
    if guess == answers[st.session_state.question_num]:
        st.session_state.score += 1
    
    st.session_state.question_num += 1
    st.session_state.selected_answer = ""
    st.session_state.start_time = time.time()  # Reset start time for next question

# Streamlit app layout
st.title("Quiz Game")

if not st.session_state.quiz_started:
    st.write("Welcome to the Quiz Game!")
    st.button("Start Quiz", on_click=start_quiz)
else:
    if st.session_state.question_num < len(questions):
        question = questions[st.session_state.question_num]
        option = options[st.session_state.question_num]
        
        st.write(f"Question {st.session_state.question_num + 1}: {question}")
        
        # Countdown timer display
        time_left = max(0, 10 - (time.time() - st.session_state.start_time))
        st.markdown(f"Time left: **{int(time_left)}** seconds")
        
        # Radio buttons for options
        st.session_state.selected_answer = st.radio("Options", options=option, key=f"answer_{st.session_state.question_num}")
        
        # Submit button
        if st.session_state.selected_answer:
            st.button("Submit", on_click=submit_answer)
            
        # Restart button if time is up
        if time_left == 0:
            st.button("Restart", on_click=lambda: st.session_state.clear())
    else:
        st.write("Quiz completed!")
        st.write(f"Your final score is: {st.session_state.score} out of {len(questions)}")
        st.write(f"Score percentage: {int((st.session_state.score / len(questions)) * 100)}%")
        
        # Provide feedback based on performance
        if st.session_state.score == len(questions):
            st.write("Excellent! You got all the questions right!")
        elif st.session_state.score >= 4:
            st.write("Great job! You got most of the questions right!")
        elif st.session_state.score >= 2:
            st.write("Good effort! You got some of the questions right.")
        else:
            st.write("Keep trying! Practice makes perfect.")
        
        st.button("Restart", on_click=lambda: st.session_state.clear())
