import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
playerschoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if(playerschoice >= 0):
  if(playerschoice < 3):
    game_images =[rock,paper,scissors]
    signals = ["rock","paper","scissors"]

    computerschoice = random.randint(0,2)

    print("Your choice\n")
    print(signals[int(playerschoice)])
    print(game_images[int(playerschoice)])


    print("Computers choice\n")
    print(signals[computerschoice])
    print(game_images[computerschoice])



    if(signals[playerschoice] == "rock" and signals[computerschoice] =="scissors"):
      print("You Win")
    elif(signals[playerschoice] == "scissors" and signals[computerschoice] =="paper"):
      print("You Win")
    elif(signals[playerschoice] == "paper" and signals[computerschoice] =="rock"):
      print("You Win")
    elif(signals[playerschoice] == signals[computerschoice]):
      print("It's a tie")
    else:
      print("Computer Wins")
  else:
    print("Invalid choice, You Lose!")
else:
  print("Invalid choice, You Lose!")

