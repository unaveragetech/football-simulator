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
import random

class FootballGame:
    def __init__(self, team1, team2, quarters=4, rounds_per_quarter=5):
        self.team1 = team1
        self.team2 = team2
        self.referee = Referee()
        self.quarters = quarters  # Number of quarters
        self.rounds_per_quarter = rounds_per_quarter  # Rounds per quarter
        self.team1_score = 0
        self.team2_score = 0
        self.weather_impact = apply_weather_impact()  # Initial weather impact
        self.critical_rounds = random.sample(range(1, quarters * rounds_per_quarter + 1), max(1, (quarters * rounds_per_quarter) // 5))  # Mark some rounds as critical
        self.fouls = {self.team1.name: 0, self.team2.name: 0}  # Track fouls

    def display_quarter_start(self, quarter):
        """Display details at the start of each quarter."""
        print(f"\n=== QUARTER {quarter} START ===")
        print(f"Weather Impact: {self.weather_impact * 100:.1f}%")
        print(f"{self.team1.name} Score: {self.team1_score:.1f} | {self.team2.name} Score: {self.team2_score:.1f}")

    def display_quarter_end(self, quarter):
        """Display details at the end of each quarter."""
        print(f"\n=== QUARTER {quarter} END ===")
        print(f"{self.team1.name} Score: {self.team1_score:.1f} | {self.team2.name} Score: {self.team2_score:.1f}")
        print(f"Fouls: {self.team1.name} - {self.fouls[self.team1.name]} | {self.team2.name} - {self.fouls[self.team2.name]}")

    def play_game(self):
        print(f"Game Start: {self.team1.name} vs {self.team2.name}")
        print(f"Initial Weather Impact: {self.weather_impact * 100:.1f}% performance adjustment.")

        # Assign roles to players
        print("\nAssigning roles to players...")
        for player in self.team1.players:
            player.role = get_random_player_role()
        for player in self.team2.players:
            player.role = get_random_player_role()

        # Simulate game by quarters
        for quarter in range(1, self.quarters + 1):
            self.display_quarter_start(quarter)

            for round_num in range(1, self.rounds_per_quarter + 1):
                global_round_num = (quarter - 1) * self.rounds_per_quarter + round_num
                print(f"\n=== Round {global_round_num} ===")

                # Check if this is a critical round
                is_critical = global_round_num in self.critical_rounds
                if is_critical:
                    print("This is a CRITICAL ROUND! Scores will be doubled.")

                # Randomly update weather every quarter
                if global_round_num % self.rounds_per_quarter == 0:
                    self.weather_impact = apply_weather_impact()
                    print(f"Weather changed! New impact: {self.weather_impact * 100:.1f}% performance adjustment.")

                # Coin flip to determine random operation
                operation = flip_coin()
                print(f"Operation: {operation.upper()}")

                # Apply a random operation
                if operation == "heads":
                    operation_type = random_operation()
                    self.team1_score = apply_operation(self.team1_score, 10, operation_type)
                    self.team2_score = apply_operation(self.team2_score, 10, operation_type)
                    print(f"Applied operation: {operation_type} to both teams' scores.")

                # Simulate player performance
                for team, team_name in [(self.team1, self.team1.name), (self.team2, self.team2.name)]:
                    print(f"\n{team_name} Team Performance:")
                    for player in team.players:
                        apply_performance_variance(player)
                        simulate_fatigue(player)
                        player.health += determine_random_health_change()
                        player.health = max(0, min(100, player.health))  # Keep health within 0-100
                        print(f"{player.name} - Role: {player.role}, Health: {player.health}, Performance: {calculate_score(player):.1f}")

                # Random game event
                game_event = random_event()
                print(f"Event: {game_event}")

                # Track fouls (randomly assigned)
                if random.random() < 0.1:  # 10% chance of a foul
                    fouling_team = random.choice([self.team1, self.team2])
                    self.fouls[fouling_team.name] += 1
                    print(f"FOUL! {fouling_team.name} committed a foul!")

                # Apply stat boost to random players
                for team in [self.team1, self.team2]:
                    player_to_boost = random.choice(team.players)
                    stat_to_boost = random.choice(["skill", "stamina", "agility", "defense", "luck"])
                    apply_boost_to_stat(player_to_boost, stat_to_boost, 10)
                    print(f"{player_to_boost.name} from {team.name} received a 10% boost to {stat_to_boost}!")

                # Calculate scores
                round_team1_score = sum(calculate_score(player) * self.weather_impact for player in self.team1.players)
                round_team2_score = sum(calculate_score(player) * self.weather_impact for player in self.team2.players)

                if is_critical:
                    round_team1_score *= 2
                    round_team2_score *= 2

                self.team1_score += round_team1_score
                self.team2_score += round_team2_score

                print(f"\nRound {global_round_num} Results:")
                print(f"{self.team1.name} Round Score: {round_team1_score:.1f} | Total: {self.team1_score:.1f}")
                print(f"{self.team2.name} Round Score: {round_team2_score:.1f} | Total: {self.team2_score:.1f}")

            self.display_quarter_end(quarter)

        # Final result
        print("\n=== Final Score ===")
        print(f"{self.team1.name}: {self.team1_score:.1f} | {self.team2.name}: {self.team2_score:.1f}")
        if self.team1_score > self.team2_score:
            print(f"Winner: {self.team1.name}!")
        elif self.team1_score < self.team2_score:
            print(f"Winner: {self.team2.name}!")
        else:
            print("It's a tie!")
