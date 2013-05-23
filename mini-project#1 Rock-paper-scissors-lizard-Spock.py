import random


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

def number_to_name(number):    
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Invalid number"


def name_to_number(name):
    name = name.lower()

    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Invalid name"


def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    
    print "Player chooses " + name.lower()
    print "Computer chooses " + number_to_name(comp_number)
    
    result = (player_number - comp_number) % 5
    if result >= 1 and result <= 2:
        print "Player wins!"
    elif result >= 3 and result <= 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print


# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")