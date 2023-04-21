# Functions

def choice_checker(question):

    error = "Please choose from rock / paper / " \
        "scissors (or xxx to quit)"

    valid = False
    while not valid:

        response = input(question).lower() # Ask the user for their choice

        if response == "r" or response == "rock":
            return response
        
        elif response == "p" or response == "paper":
            return response
        
        elif response == "s" or response == "scissors":
            return response
        
        elif response == "xxx":
            return response
        
        else:
            print(error)
        

# Main routine

# user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

# Testing loop

user_choice = " "

while user_choice != "xxx":

    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ") #  Ask for user to input choice, then check if valid


    print("You chose {}".format(user_choice)) # Print the choice
