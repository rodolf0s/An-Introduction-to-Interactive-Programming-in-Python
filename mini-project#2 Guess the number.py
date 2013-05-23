import simplegui
import random


# initialize global variables
remaining_guess = 7
num_range = 100 

def init():
    '''frame start'''
    f.start()
    range100()

def range100():
    '''button that changes range to range [0,100] and restarts'''
    global num_range, remaining_guess
    remaining_guess = 7
    num_range = random.randrange(0, 101)

    print "New game, range is from 0 to 100"
    print "Number of remaining guesses is ", remaining_guess
    #print "number is", num_range
    print

def range1000():
    '''button that changes range to range [0,1000] and restarts'''
    global num_range, remaining_guess
    remaining_guess = 10
    num_range = random.randrange(0, 1001)

    print "New game, range is from 0 to 1000"
    print "Number of remaining guesses is ", remaining_guess
    #print "number is", num_range
    print

def get_input(guess):
    '''main game logic'''
    global remaining_guess
    guess = int(guess)
    remaining_guess -= 1

    print "Guess was", guess
    print "Number of remaining guesses is ", remaining_guess

    if guess == num_range:
        print "Correct!"
        print
        range100()
    elif guess < num_range:
        print "Hight!"
    else:
        print "Lower!"

    if remaining_guess == 0:
        print "You lose!"
        print
        range100()
    print


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
init()