import random
from string import ascii_lowercase

# Function to display the question and handle input
def ask_question(question, choices):
    labeled_alts = dict(zip(ascii_lowercase, random.sample(choices, k=len(choices))))
    
    print(f"{question}?")
    for label, alt in labeled_alts.items():
        print(f"  {label}) {alt}")
    
    while True:
        ans_label = input("\nChoice? ").lower()
        if ans_label in labeled_alts:
            return labeled_alts[ans_label]
        else:
            print(f"Invalid choice. Please choose one of {', '.join(labeled_alts)}.")

# Function to run the quiz
def run_quiz(num_qutn_per_quiz=5):
    Q = {
        "When was the first known use of the word 'quiz'": [
            "1781", "1791", "1871", "1881"
        ],
        "Which built-in function can get information from the user": [
            "input", "get", "print", "write"
        ],
        "Which keyword do you use to loop over a given list of elements": [
            "for", "do while", "each", "loop"
        ],
        "What's the purpose of the built-in zip() function": [
            "To iterate over two or more sequences at the same time",
            "To combine several strings into one",
            "To compress several files into one archive",
            "To get information from the user",
        ],
        "What's the name of Python's sorting algorithm": [
            "Timsort", "Quicksort", "Merge sort", "Bubble sort"
        ],
        "What does dict.get(key) return if key isn't found in dict": [
            "None", "key", "True", "False",
        ],
        "How do you iterate over both indices and elements in an iterable": [
            "enumerate(iterable)",
            "enumerate(iterable, start=1)",
            "range(iterable)",
            "range(iterable, start=1)",
        ],
    }
    
    # Randomly choose up to the number of questions requested
    num_qutn = min(num_qutn_per_quiz, len(Q))
    qutns = random.sample(list(Q.items()), k=num_qutn)
    
    num_crrt = 0
    for num, (qutn, alts) in enumerate(qutns, start=1):
        print(f"\nQuestion {num}:")
        correct_ans = alts[0]  # Assuming first option is always the correct one
        ans = ask_question(qutn, alts)

        if ans == correct_ans:
            num_crrt += 1
            print("⭐Correct!⭐")
        else:
            print(f"The answer is {correct_ans!r}, not {ans!r}")
    
    print(f"\nYou got {num_crrt} correct out of {num_qutn} questions")

if __name__ == "__main__":
    try:
        run_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")
