import random
l=['rock','scissor','paper']
'''
rock vs paper-> paper wins
rock vs scissor-> rock wins
paper vs scissor-> scissor wins

'''
while True:
    ccount=0
    ucount=0

    ab=int(input('''
    
Game Start......
1 Yes    
2 Stop | Exit

    '''))
    if ab==1:
        for f in range(1,6):
            userInput=int(input('''
            
                       1 Rock
                       2 Scissor
                       3 Paper            
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer choice",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor")  or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor"
                  and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount=ucount+1

            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                ccount=ccount+1

        if ucount==ccount:
            print("Final Game Draw.....")
            print("user score ",ucount)
            print("Computer Score", ccount)
        elif ucount>ccount:
            print("final you win the game....")
            print("User score",ucount)
            print("computer Score",ucount)
        else:
            print(" Final Computer win the game...")
            print("user score",ucount)
            print("Computer Score", ccount)


        break;
