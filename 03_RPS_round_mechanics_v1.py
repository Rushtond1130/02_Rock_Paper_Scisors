# Functions

def round_amount():

    while True:

        response = input("How many rounds would you like to play? :")
        round_error = "input a valid ammount"

        if response != "":

            try:
                response = int(response)

                if response < 1:
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

        heading = "Continuous Mode: round {}".format(rounds_played + 1)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))

        if choose == "xxx":
            break

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds )
        print(heading)
        choose = input(choose_instruction)

        if rounds_played == rounds - 1:
            exit = "yes"

    print("You chose {}".format(choose))

    rounds_played += 1

print("Thanks for playing")
