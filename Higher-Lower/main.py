from game_data import data
import random
import art
"""Testing"""
print(art.logo)
is_game_over=False
point=0
def random_account(value):
  statement=data[value]
  return statement

def compare(first_value,next_value):
  value=['A','B']
  if first_value>next_value:
    return value[0]
  else:
    return value[1]
compare_A=random.randint(0,49)
result_A=random_account(compare_A)
follower_count_A=result_A['follower_count']
print(f"{result_A['name']}, {result_A['description']}, {result_A['country']}")

while is_game_over!=True:  
  print(art.vs)

  compare_B=random.randint(0,49)
  result_B=random_account(compare_B)
  follower_count_B=result_B['follower_count']
  print(f"{result_B['name']}, {result_B['description']}, {result_B['country']}")



  more_follower=compare(follower_count_A,follower_count_B)

  user_input=input("who has more followers Type A or B\n")
  if user_input==more_follower:
    point=point+1
    if user_input=='A':

      print(f"Correct, {result_A['name']}, has {follower_count_A}M followers.\n")
      print(f"your current score is {point}\n\n")
    else:
      print(f"Correct, {result_B['name']}, has {follower_count_B}M followers.\n")
      print(f"your current score is {point}\n\n")



  else: 
    if user_input=='A':
      print(f"Wrong, {result_B['name']}, has {follower_count_B}M followers compared to {result_A['name']}, who has {follower_count_A}M followers .\n")
    else:
      print(f"Wrong, {result_A['name']}, has {follower_count_A}M followers compared to {result_B['name']}, who has {follower_count_B}M followers .\n")
    is_game_over=True
    print(f"your final score is {point}.\n")

  if is_game_over!=True:
    compare_A=compare_B
    result_A=random_account(compare_A)
    follower_count_A=result_A['follower_count']
    print(f"{result_A['name']}, {result_A['description']}, {result_A['country']}")