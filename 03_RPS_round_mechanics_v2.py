# Functions

def round_amount():

    while True:

        response = input("How many rounds would you like to play? :")
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

# Main

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p), or scissors (s)."
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
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    if choose == "xxx":     # Exit
        break


    rounds_played += 1

print("Thanks for playing")
