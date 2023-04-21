# Functions

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

# Lists

rps_list = ["rock", "paper", "scissors", "xxx"]

# Testing loop

user_choice = " "

while user_choice != "xxx":

    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): " , rps_list, "Please choose from rock / paper / scissors (or xxx to quit") #  Ask for user to input choice, then check if valid


    print("You chose {}".format(user_choice)) # Print the choice





