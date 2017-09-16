# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(num):
    if num == 0:
        result = "rock"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "paper"
    elif num == 3:
        result = "lizard"
    elif num == 4:
        result = "scissors"
    return result 

    
def name_to_number(name):
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result


def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
   
    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number)
   
    if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""    

    
# test your code
while 1:
	print("Please choose one from below by typing corresponding numbers:\n 1.)rock\n 2.)Spock\n 3.)paper\n 4.)lizard\n 5.)scissors\n 6.)Exit from game")
	player_choice=int(input())
	if(player_choice==1):
			rpsls("rock")
	elif(player_choice==2):
		rpsls("Spock")
	elif(player_choice==3):
		rpsls("paper")
	elif(player_choice==4):
		rpsls("lizard")
	elif(player_choice==5):
		rpsls("scissors")
	elif(player_choice==6):
		break
	else:
		print("please only select from abocve options")

# always remember to check your completed program against the grading rubric