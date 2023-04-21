rps_list = ["rock", "paper", "scissors"]
comp_index = 0

for item in rps_list:
    user_index = 0

    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare

        if comp_choice == user_choice:
            result = "draw"

        elif user_choice == "rock" and comp_choice == "scissors" or user_choice == "paper" and comp_choice == "rock" or user_choice == "scissors" and comp_choice == "paper":
            result = "won"

        else:
            result = "lost"

        print("You chose {}, the computer chose {}.\nResult: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()