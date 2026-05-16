
"""Rock Paper Scissor - simple, easy-to-understand CLI game.

How to play:
- Run this file with Python.
- At the prompt type one of: rock, paper, scissors (or r, p, s).
- The computer chooses randomly. The result and running score are shown.
- Enter 'q' or 'quit' at the first prompt to exit.

This module exposes `decide_winner(user_choice, comp_choice)` which returns one
of the strings: 'win', 'lose', or 'tie'. Use it for quick, non-interactive checks.
"""

import random

CHOICES = ("rock", "paper", "scissors")
ALIASES = {"r": "rock", "p": "paper", "s": "scissors"}


def normalize_choice(text: str):
	"""Normalize user input to one of 'rock','paper','scissors'.

	Returns normalized string or None if unknown.
	"""
	if not isinstance(text, str):
		return None
	t = text.strip().lower()
	if not t:
		return None
	if t in CHOICES:
		return t
	if t in ALIASES:
		return ALIASES[t]
	# allow first-letter match (e.g., 'r' or user typing 'Rock')
	if t[0] in ALIASES:
		return ALIASES[t[0]]
	return None


def decide_winner(user_choice: str, comp_choice: str) -> str:
	"""Decide winner between user_choice and comp_choice.

	Returns:
	  - 'win'  if user wins
	  - 'lose' if user loses
	  - 'tie'  if same choice
	Both inputs should be normalized (see normalize_choice).
	"""
	u = normalize_choice(user_choice)
	c = normalize_choice(comp_choice)
	if u is None or c is None:
		raise ValueError("Invalid choice provided to decide_winner")
	if u == c:
		return "tie"
	# winning pairs for the user
	wins = {
		("rock", "scissors"),
		("paper", "rock"),
		("scissors", "paper"),
	}
	return "win" if (u, c) in wins else "lose"


def main():
	print("Welcome to Rock Paper Scissors!")
	print("Type 'rock', 'paper', or 'scissors' (or r/p/s). Type 'q' to quit.")
	user_score = 0
	comp_score = 0
	rounds = 0
	try:
		while True:
			txt = input("Your choice (rock/paper/scissors or q to quit): ").strip()
			if txt.lower() in ("q", "quit", "exit"):
				break
			user = normalize_choice(txt)
			if user is None:
				print("I didn't understand that. Please type rock, paper, or scissors (or r/p/s).")
				continue
			comp = random.choice(CHOICES)
			result = decide_winner(user, comp)
			rounds += 1
			if result == "win":
				user_score += 1
				outcome = "You win!"
			elif result == "lose":
				comp_score += 1
				outcome = "You lose."
			else:
				outcome = "It's a tie."

			print(f"You: {user}  |  Computer: {comp}  -> {outcome}")
			print(f"Score after {rounds} round(s): You {user_score} - Computer {comp_score}\n")
	except KeyboardInterrupt:
		print("\nInterrupted by user. Exiting.")
	print("Thanks for playing!")


if __name__ == "__main__":
	main()

