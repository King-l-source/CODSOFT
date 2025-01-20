import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        result_label.config(text="It's a tie!", fg="blue")
    elif result == "user":
        result_label.config(text="You win this round!", fg="green")
        user_score += 1
    else:
        result_label.config(text="Computer wins this round!", fg="red")
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="Let's play!", fg="black")
    computer_choice_label.config(text="")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 14))
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14))
computer_score_label.pack()

computer_choice_label = tk.Label(root, text="", font=("Arial", 14), fg="gray")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Let's play!", font=("Arial", 16), fg="black")
result_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), bg="orange", fg="white", command=reset_game)
reset_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg="red", fg="white", command=root.quit)
exit_button.pack()

root.mainloop()
