import tkinter as tk
import random

class GuessingGame(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Guessing Game")
        self.geometry("1250x700")

        self.level = tk.StringVar()
        self.level.set("easy")

        self.guess = None
        self.attempts = 0
        self.max_attempts = 0

        self.create_GUI()

    def create_GUI(self):
        label = tk.Label(self, text="Guess the Number Game", font=("Algerian", 20), background="yellow")
        label.pack(pady=60)

        frame = tk.LabelFrame(self, text="Select Level", fg="red", borderwidth=10)
        frame.pack(pady=10)

        easy_btn = tk.Radiobutton(frame, text="Easy (No:1-10)", variable=self.level, value="easy")
        easy_btn.pack(anchor="w")

        medium_btn = tk.Radiobutton(frame, text="Medium (No:1-60)", variable=self.level, value="medium")
        medium_btn.pack(anchor="w")

        hard_btn = tk.Radiobutton(frame, text="Hard (No:1-150)", variable=self.level, value="hard")
        hard_btn.pack(anchor="w")

        label0 = tk.Label(self, text="Note:", font=("Helvetica", 9), fg="red")
        label0.pack(padx=0, pady=5)

        label1 = tk.Label(self, text="1. Easy Level maximum 6 attempts\n2. Medium Level maximum 4 attempts\n3. Hard Level maximum 2 attempts", font=("Biome Light", 9), fg="blue")
        label1.pack(pady=5)

        start_btn = tk.Button(self, text="Play", command=self.start_game, background="lightgreen")
        start_btn.pack(pady=20)

        label2 = tk.Label(self, text="Enter your Guessing Number", font=("Helvetica", 12))
        label2.pack(pady=10)
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        submit_btn = tk.Button(self, text="Check Your No", command=self.check_guess, background="pink")
        submit_btn.pack(pady=20)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def start_game(self):
        level = self.level.get()
        if level == "easy":
            self.guess = random.randint(1, 10)
            self.max_attempts = 6
        elif level == "medium":
            self.guess = random.randint(1, 60)
            self.max_attempts = 4
        else:
            self.guess = random.randint(1, 150)
            self.max_attempts = 2

        self.attempts = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.NORMAL)

    def check_guess(self):
        guess = self.guess_entry.get()
        if guess.isdigit():
            guess = int(guess)
            self.attempts += 1

            if guess < self.guess:
                self.result_label.config(text="Your number is too small! Attempts: {}/{}".format(self.attempts, self.max_attempts))
            elif guess > self.guess:
                self.result_label.config(text="Your number is too big! Attempts: {}/{}".format(self.attempts, self.max_attempts))
            else:
                self.result_label.config(text="You win the game Wowww⭐✨\nCongratulations🤩!\nYou guessed it in {} attempts.".format(self.attempts))
                self.guess_entry.config(state=tk.DISABLED)
                return

            if self.attempts >= self.max_attempts:
                self.result_label.config(text="You lost the game! \nYou have reached the maximum number of attempts.\nThe Correct Number was {}.".format(self.guess))
                self.guess_entry.config(state=tk.DISABLED)

        else:
            self.result_label.config(text="Invalid input! Enter a number.")

        self.guess_entry.delete(0, tk.END)

game = GuessingGame()
game.mainloop()
