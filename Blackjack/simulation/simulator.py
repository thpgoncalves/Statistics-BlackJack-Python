from simulation_flow import simulate_game_rounds

if __name__ == "__main__":
    num_games = 1000  # Adjust to the number of games that you want to simulate
    results = simulate_game_rounds(num_games)
    print(f"Overall Win Rate: {results['win_rate']}%")
    print(f"Total Games Played: {results['total_games']}")
    print(f"Total Wins: {results['total_wins']}")
    for strategy in results['strategy_wins']:
        strategy_name = strategy.capitalize() + " hand Strategy win rate"
        print(f"{strategy_name}: {results['strategy_wins'][strategy]}%")