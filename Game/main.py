import random
user_selection=int(input0())
if user_selection==0: 
  print(""" user seklection
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
if user_selection==1:
  print("""
           _______
      ---'    ____)____
                 ______)
                _______)
               _______)
      ---.__________)
      """)
if user_selection==2:
  print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

random_number=random.randint(0,2)
index_number=0
rock=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""]
paper=["""
           _______
      ---'    ____)____
                 ______)
                _______)
               _______)
      ---.__________)
      """]
scissor=["""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """]

rock_paper_scissor=[rock,paper,scissor]
computer_selection=rock_paper_scissor[random_number][index_number]
print(f"computer choose{computer_selection}")