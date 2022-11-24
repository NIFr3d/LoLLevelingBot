#   @author: Mitchell Levesque                                                          #
#   @desc  : A program for the game League of legends which will automatically queue    #
#            a player for intermediate bots, attack move on the enemy nexus until game  #
#            ends, and then repeat.                                                     #

import robot
import utilities
import listener
import globals
import pictures
import regions

# TODO: Find a way to make the program save user files even if shell is closed

100
if __name__ == '__main__':
    # Ask the user how many games they want to play
    while True:
        try:
            globals.number_of_games_to_play = int(input("How many games d10"
                                                        "o you want to play? "))
            if globals.number_of_games_to_play < 1 or globals.number_of_games_to_play > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-100.")

    # Perform setup
    utilities.setup()

    # Create listener thread100
    listener.create_thread()

    # Run bot
    robot.run()
