import random

pickables = ['Rock', 'Paper', 'Scissor']

while True:
    user_count=0
    comp_count=0
    user_choice=int(input('''
 --- Game Started ---
     1 Yes
     2 No
     '''))

    if user_choice==1:
        for a in range(1,5):
            userInput = int(input('''

            1 Rock
            2 Paper
            3 Scissor
                        '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Paper"
            elif userInput==3:
                uchoice="Scissor"

            Comp_choice=random.choice(pickables)

            if Comp_choice==uchoice:
                print("User choice", uchoice)
                print("Computer choice", Comp_choice)
                print("It's a tie")
                user_count=user_count+1
                comp_count=comp_count+1

            elif (uchoice=="Rock" and Comp_choice=="Scissor") or (uchoice=="Paper" and Comp_choice=="Rock") or (uchoice=="Scissor" and Comp_choice=="Paper"):
                print("User choice", uchoice)
                print("Computer choice", Comp_choice)
                print("You win")
                user_count=user_count+1

            else:
                print("User choice", uchoice)
                print("Computer choice", Comp_choice)
                print("Computer win")
                comp_count=comp_count+1

        if user_count==comp_count:
            print("Final game draw")
            print("User score is :",user_count)
            print("Computer score is :",comp_count)

        elif user_count>comp_count:
            print("Final game won by you")
            print("User score is :",user_count)
            print("Computer score is :",comp_count)

        else:
            print("Final game won by computer")
            print("User score is :",user_count)
            print("Computer score is :",comp_count)

       
    else:
        print("Exiting from the game")
        break
        
              




