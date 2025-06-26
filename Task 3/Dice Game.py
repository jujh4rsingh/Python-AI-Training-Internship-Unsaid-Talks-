import random

def simulate_dice_game():
    players = input("Enter player names separated by commas: ").split(",")
    players = [p.strip() for p in players]

    scores = {player: 0 for player in players}
    last_roll = {player: None for player in players}

    rounds = 0
    min_rounds = 10

    while rounds < min_rounds:
        print(f"\n--- Round {rounds + 1} ---")
        for player in players:
            roll = random.randint(1, 6)
            print(f"{player} rolled a {roll}")

            # Apply main scoring rules
            if roll == 6:
                scores[player] += 10
            elif roll == 1:
                scores[player] -= 5
            else:
                scores[player] += roll

            # Bonus: two 6s in a row
            if last_roll[player] == 6 and roll == 6:
                print(f"{player} rolled two 6s in a row! Bonus +5")
                scores[player] += 5

            # Reset if score goes below 0
            if scores[player] < 0:
                print(f"{player}'s score went below 0! Reset to 0.")
                scores[player] = 0

            last_roll[player] = roll

        rounds += 1

    # Show final scores
    print("\n--- Final Scores ---")
    for player, score in scores.items():
        print(f"{player}: {score}")

    # Use lambda to find highest scorer
    highest = max(scores.items(), key=lambda x: x[1])
    print(f"\n🏆 Winner: {highest[0]} with {highest[1]} points!")

# Run the game
simulate_dice_game()
