import random


is_runing = True

items = [
    "R",
    "P",
    "S"
  ]

while is_runing:
  com_choice = random.choice(items)
  print(com_choice)
  
  player_choice = input("Enter a choice R, P, S: ")
  player_choice = player_choice.upper()
  
  if player_choice  in items:
    if player_choice == "R" and com_choice == "S":
      print(f'Player {player_choice} : CPU {com_choice}')
      print("You Win!🏆")
      is_runing = False
    elif player_choice == "P" and com_choice == "R":
      print(f'Player {player_choice} : CPU {com_choice}')
      print("You Win!🏆")
      is_runing = False
    elif player_choice == "S" and com_choice == "P":
      print(f'Player {player_choice} : CPU {com_choice}')
      print("You Win!🏆")
      is_runing = False
    elif com_choice == player_choice:
      print("Tie pick again ...")
    else:
      print("you lost!😟")
      is_runing = False
  else:
    print("wrong choice")