Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock"""
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
Paper"""
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
"""
import random

list=[Rock,Paper,Scissors]
list=random.choice(list)
user=int(input("what do you choose? type 0 for Rock, 1 for papper and 2 for scissors:\n"))


images=[Rock,Paper,Scissors]
# condtion to print the Images
if user==0:
    print(images[user])

elif user==1:
    print(images[user])

elif user==2:
    print(images[user])

else:
    print("You selected Invalid option Please try again")

print(f"Computer Choose:\n{list}")

# Condtions for game
if user==0 and list==Scissors:
    print("You Win")
    if list==Rock:
        print("You win")
elif user==0 and list==Paper:
    print("You lose")

elif user==0 and list==Rock:
    print("it a tie.no one wins")

elif  user==1 and list==Rock:
    print("You win")

elif user==1 and list==Scissors:    
    print("You Lose")

elif user==1 and list==Paper:
    print("it a tie.no one wins")

elif user==2 and list==Paper:
    print("You win")

elif user==2 and list==Scissors:
    print("it a tie.no one wins")
    
elif user==2 and list==Rock:
    print("You Lose")
    
    