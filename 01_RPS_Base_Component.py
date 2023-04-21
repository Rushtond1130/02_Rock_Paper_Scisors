import random

# Functions
def round_amount():


    while True:

        response = input("\nHow many rounds would you like to play? :")
        round_error = "Please type an integer more than 0\nOr <enter> for infinite mode."

        if response != "":      # Check that the response is an integer more than zero if infinite mode is not chosen

            try:
                response = int(response)

                if response < 1:        # Give an error if the response is less than 1 and start the loop again
                    print(round_error)
                    continue
            
            except ValueError:
                print(round_error)
                continue
            
        return response

def choice_checker(question, valid_list, error):


    valid = False
    while not valid:

        response = input(question).lower() # Ask the user for their choice

        for item in valid_list:

            if response == item[0] or response == item:
                return item

        print(error) # An error will show if the item is not in the list
        print()
      
# Main routine

# Valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Show instructions if user has not played before

# Ask for number of rounds

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0
game_summary = []


rounds = round_amount()
exit = "no"

while exit == "no":

    print()

    if rounds == "":

        heading = "Continuous Mode: Round {}".format(rounds_played + 1)     # Continuous

    else:
        
        heading = "Round {} of {}".format(rounds_played + 1, rounds)        # Custom ammount

        if rounds_played == rounds - 1:
            exit = "yes"

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p), or scissors (s)."
    choose_error = "\nPlease choose from rock / paper / scissors (or xxx to quit)"

# Get R P S user choice

    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

# Exit 

    if user_choice == "xxx":     # Exit
        break

# Get computer R P S choice

    comp_choice = random.choice(rps_list[:-1])

# Compare computer and user choices

    if comp_choice == user_choice:
       result = "draw"
       rounds_drawn += 1

    elif user_choice == "rock" and comp_choice == "scissors" or user_choice == "paper" and comp_choice == "rock" or user_choice == "scissors" and comp_choice == "paper":
        result = "won"

    else:
        result = "lost"
        rounds_lost += 1

# Tell the user both the computer choice and the user choice, then show the outcome

    if result == "draw":
        feedback = "It's a draw"

    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

    print(feedback)
    rounds_played += 1




    for item in range(rounds_played, rounds_played + 1):

        outcome = "Round {}: {}".format(item, result)
        
        game_summary.append(outcome)

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()


rounds_won = rounds_played - rounds_lost - rounds_drawn

percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_drawn = rounds_drawn / rounds_played * 100

print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost, rounds_drawn, percent_drawn))





# Show user their game stats 


# End of game statement

print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")  

