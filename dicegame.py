import random
from sys import exit

print("WELCOME TO  DICE MANIA")
min=1
max=6
NAME=input("Enter NAME: ")
x=0
y=0
score=0
roll_again="yes"
while(roll_again=="yes"):
  if(roll_again=="no"):
    print(score)
    exit(0)
  x=random.randint(min,max)
  y=random.randint(min,max)
  def dice(m):
    if(m==1):
       print(
  '''
    ____________  
   |            |
   |            |
   |      *     |
   |            |
   |____________|
''')
    if(m==2):
       print(
  '''
    ____________  
   |            |
   |       *    |
   |     *      |
   |____________|
''')
    if(m==3):
       print(
  '''
    ____________  
   |            |
   |   *     *  |
   |      *     |
   |____________|
''')
    if(m==4):
      print(
  '''
    ____________  
   |            |
   |    *   *   |
   |    *   *   |
   |____________|
''')
    if(m==5):
      print(
  '''
    ____________  
   |            |
   |    *   *   |
   |      *     |
   |    *   *   |
   |____________|
''')
    if(m==6):
      print(
  '''
    ____________  
   |            |
   |    *   *   |
   |    *   *   |
   |    *   *   |
   |____________|
''')
  print("your turn:")
  dice(x)
  print("computer's turn")
  dice(y)
  if(x==y):
    print("tie!")
  elif(x>y):
    score+=1
    print("you won"+" "+NAME.upper())
  else:
    print("you lost the game"+" "
    +NAME.upper())
  
  roll_again=input("ENTER YES TO ROLL AGAIN: ")

