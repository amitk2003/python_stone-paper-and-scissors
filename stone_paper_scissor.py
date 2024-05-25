# stone, paper,scissor game
import random
l=["rock","paper","scissors"];


# rock vs paper->paper wins
# paper vs scissor->scissor wins
# scissor vs rock->rock wins


while True:
    yourscore=0;
    computerscore=0;

    us=int(input('''Do you want to start game:
      1.yes/start
      2.No/Exit          
                 '''));
    if us==1:
       for a in range(1,6):
        userinput=int(input('''pleas select any one option:
       1.rock
      2.paper
      3.scissor
 '''))
        if userinput==1:
          uschoice="rock"
          computer_choice=random.choice(l)
          if uschoice==computer_choice:
            print("game draws:")
            yourscore=yourscore+1;
            computerscore=computerscore+1;
          elif (uschoice=="paper" and computer_choice=="rock") or  (uschoice=="scissors" and computer_choice=="paper") or      (uschoice=="rock" and computer_choice=="scissors"):
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            print("user wins");
            yourscore=yourscore+1;
          else:
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            print("computer win")
            computerscore=computerscore+1;
          
        elif userinput==2:
          uschoice="paper"
          computer_choice=random.choice(l)
          if uschoice==computer_choice:
            print("game draws:")
            yourscore=yourscore+1;
            computerscore=computerscore+1;
          elif (uschoice=="paper" and computer_choice=="rock") or  (uschoice=="scissors" and computer_choice=="paper") or      (uschoice=="rock" and computer_choice=="scissors"): 
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            print("user wins");
            yourscore=yourscore+1;
          else:
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            print("computer win")
            computerscore=computerscore+1;
         
        elif userinput==3:
          uschoice="scissors"
          computer_choice=random.choice(l)
          if uschoice==computer_choice:
            print("game draws:")
            yourscore=yourscore+1;
            computerscore=computerscore+1;
          elif (uschoice=="paper" and computer_choice=="rock") or  (uschoice=="scissors" and computer_choice=="paper") or      (uschoice=="rock" and computer_choice=="scissors"):
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            yourscore=yourscore+1;
            print("user wins");
          else:
            print("computer value:",computer_choice)
            print("user value:",uschoice)
            print("computer win")
            computerscore=computerscore+1;
       if(yourscore==computerscore):
        print("game draws");
        print("computer score:",computerscore);
        print("user score:",yourscore);
       
       elif (yourscore>computerscore):
         print("you beat computer")
         print("computer score:",computerscore);
         print("user score:",yourscore);
       else:
         print("you lose");
         print("computer score:",computerscore);
         print("user score:",yourscore); 

            
    else:
     break; 
          

# computer_choice=random.choice(l)
# print(computer_choice)
