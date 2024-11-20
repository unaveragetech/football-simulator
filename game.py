# game.py
from referee import Referee
from utils import (
    flip_coin,
    calculate_score,
    random_operation,
    apply_operation,
    apply_performance_variance,
    random_event,
    apply_weather_impact,
    simulate_fatigue,
    apply_boost_to_stat,
    get_random_player_role,
    determine_random_health_change,
)
import random  # Added to allow for random choice

class FootballGame:
    def __init__(self, team1, team2, rounds=15):  # Default rounds set to 15, but can be changed
        self.team1 = team1
        self.team2 = team2
        self.referee = Referee()
        self.rounds = rounds  # Use the rounds parameter provided when the game is created
        self.team1_score = 0
        self.team2_score = 0

    def play_game(self):
        """Simulate the game."""
        print(f"Game Start: {self.team1.name} vs {self.team2.name}")
        
        # Randomly determine weather condition at the start
        weather_impact = apply_weather_impact()
        print(f"Weather Impact: {weather_impact * 100}% performance adjustment.")

        for round_num in range(1, self.rounds + 1):  # Loop over the number of rounds set
            print(f"\n=== Round {round_num} ===")
            
            # Coin flip to decide random operation
            operation = flip_coin()
            print(f"Operation: {operation.upper()}")

            # Apply a random operation between team scores
            if operation == "heads":
                operation_type = random_operation()
                self.team1_score = apply_operation(self.team1_score, 10, operation_type)
                self.team2_score = apply_operation(self.team2_score, 10, operation_type)
                print(f"Applied operation: {operation_type} to both teams' scores.")

            # Team decisions and display
            print(f"\n{self.team1.name} selects players.")
            self.team1.display_team()
            print(f"\n{self.team2.name} selects players.")
            self.team2.display_team()

            # Apply referee decisions (injuries)
            self.team1.players = [self.referee.apply_injury(player) for player in self.team1.players]
            self.team2.players = [self.referee.apply_injury(player) for player in self.team2.players]

            # Apply performance variance to players' ratings
            for player in self.team1.players:
                apply_performance_variance(player)
            for player in self.team2.players:
                apply_performance_variance(player)

            # Simulate random events affecting the game
            game_event = random_event()
            print(f"Event: {game_event}")

            # Apply fatigue over time, affecting player performance
            for player in self.team1.players:
                simulate_fatigue(player)
            for player in self.team2.players:
                simulate_fatigue(player)

            # Apply random boost to a player's stats (example: boost skill by 10%)
            player_to_boost = random.choice(self.team1.players)  # Apply to a random player from team1
            apply_boost_to_stat(player_to_boost, "skill", 10)

            # Calculate scores with fatigue and boosted stats
            self.team1_score += sum(calculate_score(player) * weather_impact for player in self.team1.players)
            self.team2_score += sum(calculate_score(player) * weather_impact for player in self.team2.players)

            print(f"\nRound {round_num} Results:")
            print(f"{self.team1.name} Total Score: {self.team1_score}")
            print(f"{self.team2.name} Total Score: {self.team2_score}")

        # Final result
        print("\n=== Final Score ===")
        winner = self.team1.name if self.team1_score > self.team2_score else self.team2.name
        print(f"{self.team1.name}: {self.team1_score} | {self.team2.name}: {self.team2_score}")
        print(f"Winner: {winner}!")
