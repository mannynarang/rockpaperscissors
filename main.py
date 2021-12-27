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
playerschoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

signals =[rock,paper,scissors]
signals_text = ["rock","paper","scissors"]

computerschoice = random.randint(0,2)

print("Your choice\n")
print(signals_text[int(playerschoice)])
print(signals[int(playerschoice)])


print("Computers choice\n")
print(signals_text[computerschoice])
print(signals[computerschoice])



if(signals_text[int(playerschoice)] == "rock" and signals_text[computerschoice] =="scissors"):
  print("You Win")
elif(signals_text[int(playerschoice)] == "scissors" and signals_text[computerschoice] =="paper"):
  print("You Win")
elif(signals_text[int(playerschoice)] == "paper" and signals_text[computerschoice] =="rock"):
  print("You Win")
elif(signals_text[int(playerschoice)] == signals_text[computerschoice]):
  print("It's a tie")
else:
  print("Computer Wins")


