import random

# Step 1: Define the valid choices
choices = ["stone", "paper", "scissors"]

# Step 2: Get user input and convert to lowercase
player = input("Enter stone, paper, or scissors: ").lower()

# Step 3: Let the computer pick randomly
computer = random.choice(choices)

print("You chose:", player)
print("Computer chose:", computer)

# Step 4: Check for a tie
if player == computer:
    print("It's a tie!")

# Step 5: Check all winning conditions for the player
elif player == "stone" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "stone":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")

# Step 6: If it is not a tie and you didn't win, the computer wins
else:
    print("Computer wins!")
    