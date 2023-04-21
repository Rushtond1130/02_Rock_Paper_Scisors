rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing
test_results = ["won", "won", "loss", "loss", "tie"]

for item in test_results:
    rounds_played += 1

    # computer choice

    result = item

    if result == "draw":
        result = "It's a draw"
        rounds_drawn += 1

    elif result == "loss":
        rounds_lost += 1

rounds_won = rounds_played - rounds_lost - rounds_drawn


print()
print('*** End Game Summary ***')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")