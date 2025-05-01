import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number Game")
        self.secret_number = None
        self.max_attempts = None
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="🎯 Welcome to the Guessing Game!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.diff_label = tk.Label(self.root, text="Choose difficulty level:")
        self.diff_label.pack()

        # Difficulty buttons
        self.easy_button = tk.Button(self.root, text="Easy (10 attempts)", command=lambda: self.start_game(10))
        self.easy_button.pack(pady=5)

        self.medium_button = tk.Button(self.root, text="Medium (5 attempts)", command=lambda: self.start_game(5))
        self.medium_button.pack(pady=5)

        self.hard_button = tk.Button(self.root, text="Hard (3 attempts)", command=lambda: self.start_game(3))
        self.hard_button.pack(pady=5)

        # Entry and feedback widgets (hidden until game starts)
        self.guess_label = tk.Label(self.root, text="")
        self.entry = tk.Entry(self.root)
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.cheat_button = tk.Button(self.root, text="Cheat 🤫", command=self.show_cheat)
        self.feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game)

    def start_game(self, attempts):
        self.secret_number = random.randint(1, 20)
        self.max_attempts = attempts
        self.attempts = 0

        # Hide difficulty buttons
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()

        self.diff_label.config(text=f"I've chosen a number between 1 and 20.\nYou have {self.max_attempts} attempts!")

        self.guess_label.config(text="Enter your guess:")
        self.guess_label.pack(pady=5)
        self.entry.pack()
        self.submit_button.pack(pady=5)
        self.cheat_button.pack(pady=5)
        self.feedback.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="⚠️ Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.feedback.config(text=f"📉 Too low! Attempts: {self.attempts}/{self.max_attempts}")
        elif guess > self.secret_number:
            self.feedback.config(text=f"📈 Too high! Attempts: {self.attempts}/{self.max_attempts}")
        else:
            self.feedback.config(text=f"🎉 You guessed it! The number was {self.secret_number}!")
            self.end_game()

        if self.attempts >= self.max_attempts and guess != self.secret_number:
            self.feedback.config(text=f"❌ Game Over! The number was {self.secret_number}.")
            self.end_game()

    def show_cheat(self):
        self.feedback.config(text=f"😈 Cheat Mode: The secret number is {self.secret_number}")

    def end_game(self):
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.cheat_button.pack_forget()
        self.play_again_button.pack(pady=10)

    def reset_game(self):
        self.feedback.config(text="")
        self.play_again_button.pack_forget()
        self.guess_label.pack_forget()
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.cheat_button.pack_forget()

        self.diff_label.config(text="Choose difficulty level:")
        self.easy_button.pack(pady=5)
        self.medium_button.pack(pady=5)
        self.hard_button.pack(pady=5)

# Create the Tkinter window and run the app
root = tk.Tk()
app = GuessingGame(root)
root.mainloop()