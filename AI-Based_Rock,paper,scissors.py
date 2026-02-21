import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("Welcome to AI Rock, Paper, Scissors Game!")
print("Type 'exit' to stop playing.\n")

while True:
    user_move = input("Enter rock, paper, or scissors: ").lower()
    
    if user_move == "exit":
        break
    
    if user_move not in choices:
        print("Invalid choice! Try again.\n")
        continue
    
    computer_move = random.choice(choices)
    
    print(f"Computer chose: {computer_move}")
    
    # Winning logic
    if user_move == computer_move:
        print("It's a tie!")
    
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        print("You win!")
        user_score += 1
    
    else:
        print("Computer wins!")
        computer_score += 1
    
    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

print("Final Score:")
print(f"You: {user_score} | Computer: {computer_score}")