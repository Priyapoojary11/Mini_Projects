# Python Quiz App

This project is a simple Python-based quiz game that asks a set of multiple-choice questions, shuffles their answer choices, and evaluates user input.

## Features
- Randomly selects a configurable number of questions (default: 5).
- Displays multiple-choice options for each question.
- Shuffles the order of answer options for variety.
- Evaluates and displays whether the user's choice is correct or incorrect.
- Displays a score at the end showing how many questions the user answered correctly.
- Handles invalid input and provides feedback to the user.
- Modular code with functions to make the quiz more maintainable.

## How It Works
1. **Questions and Answers**: A dictionary of questions (`Q`) is predefined with possible answers. The correct answer is always the first option in each list.
   
2. **Randomization**: For each quiz, a random selection of questions is made. The answers to each question are shuffled so that they appear in a different order every time.

3. **User Input**: The user is prompted to answer the question by entering the corresponding letter (e.g., `a`, `b`, `c`, etc.). If the input is invalid, the user will be prompted again until a valid response is received.

4. **Evaluation**: The user’s choice is compared to the correct answer, and feedback is given (whether the answer was correct or incorrect).

5. **Scoring**: At the end of the quiz, the user is shown how many answers they got correct out of the total number of questions.

6. **Error Handling**: The program catches any unexpected errors and gives the user a friendly error message.

## Example Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Priyapoojary11/Projects/Quiz-Code.git
