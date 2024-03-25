import random
choice='y'
while choice=='y':
   user_choice = input("Enter your choice(rock,paper,scissors):");
   possible_choice=["rock","paper","scissors"];
   computer_choice=random.choice(possible_choice);
   print(f"Your choice is {user_choice} \ncomputer choice is {computer_choice}")
   if user_choice == computer_choice:
      print("It's a tie!")
   elif user_choice == "rock" and computer_choice == "scissors":
      print("you win!")
   elif user_choice=="paper" and computer_choice=="rock":
      print("you win!")
   elif user_choice=="scissors" and computer_choice=="paper":
      print("you win!")
   else:
      print("computer win!")
   choice=input("Do you want to continue(y/n)?")
