from game import Game

games_results: dict[str, int] = {
    "total_number_of_games": 0,
    "total_number_of_rounds": 0,
    "The General": 0,
    "Heir Apparent": 0,
    "The Princess": 0,
    "The Emperor": 0,
}

for i in range(10000):
    game = Game(number_of_players=4)
    games_results["total_number_of_games"] += 1

    while True:
        if game.winner:
            break
        game.round()

    games_results["total_number_of_rounds"] += game.number_of_rounds
    games_results[game.winner.character_name] += 1

print(f"\nResults: {games_results}")
print(
    f"Average number of rounds: {games_results['total_number_of_rounds'] / games_results['total_number_of_games']}"
)
