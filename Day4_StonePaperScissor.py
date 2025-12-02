import random
weapons=["stone","paper","scissor"]
limit=int(input("please set a total game score out of which the game will be won: "))
user=0
computer=0
for n in range(limit):
     user_choice=str(input("Your turn: "))
     program_choice=random.choice(weapons)
     print(program_choice)
     if(user_choice==program_choice):
          print("Same choice, no points awarded")
     elif(user_choice=="stone"):
          if(program_choice=="scissor"):
               print("Points awarded to user")
               user+=1
          else:
               print("Points awarded to computer")
               computer+=1
     elif(user_choice=="paper"):
          if(program_choice=="stone"):
               print("Points awarded to user")
               user+=1
          else:
               print("Points awarded to computer")
               computer+=1
     elif(user_choice=="scissor"):
          if(program_choice=="paper"):
               print("Points awarded to user")
               user+=1
          else:
               print("Points awarded to computer")
               computer+=1
print(f"Score of user: {user} ")
print(f"Score of computer: {computer}")
if(user>computer):
     print("User won. Congratulations!!!")
else:
     print("Computer won.Good Job!!!") 



