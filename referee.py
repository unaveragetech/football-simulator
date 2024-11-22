import random
from utils import (
    random_operation,
    apply_operation,
    apply_performance_variance,
    adjust_player_stats_for_fatigue,
    determine_random_health_change,
    random_event,
    apply_boost_to_stat,
    apply_weather_impact,
    generate_random_player_stat,
    calculate_score,
)

class Referee:
    def __init__(self):
        self.weather_condition = apply_weather_impact()
        print(f"Initial weather condition factor: {self.weather_condition:.2f}")

    def select_operation(self):
        """Randomly selects an operation for the round."""
        selected_operation = random_operation()
        print(f"Referee selected operation: {selected_operation}")
        return selected_operation

    def apply_operations(self, team1, team2, operation):
        """Applies the selected operation to each player on both teams."""
        print(f"Applying '{operation}' operation to all players with weather impact.")
        for player in team1.players:
            self.apply_operation_to_player(player, operation)

        for player in team2.players:
            self.apply_operation_to_player(player, operation)

    def apply_operation_to_player(self, player, operation):
        """Applies the operation to a player's stats."""
        original_rating = player["rating"]
        original_health = player["health"]

        # Apply operation dynamically using `apply_operation`
        player["rating"] = apply_operation(player["rating"], self.weather_condition, operation)
        player["health"] += determine_random_health_change()  # Adjust health randomly

        # Ensure logical boundaries for stats
        player["rating"] = max(0, min(player["rating"], 100))
        player["health"] = max(0, min(player["health"], 100))

        print(
            f"Player '{player['name']}' stats adjusted:\n"
            f"  Original Rating: {original_rating:.2f} -> {player['rating']:.2f}\n"
            f"  Original Health: {original_health:.2f} -> {player['health']:.2f}"
        )

    def handle_injuries(self, team, health_threshold=30):
        """Handles injuries and substitutes players below health threshold."""
        for i, player in enumerate(team.players):
            if player["health"] < health_threshold:
                print(f"Player '{player['name']}' from {team.name} is injured with health {player['health']}!")

                substitute_available = team.substitute_player(i)
                if substitute_available:
                    print(f"Player '{player['name']}' was substituted successfully.")
                else:
                    print(f"No substitutes available for '{player['name']}'. Player may recover.")

                    # Allow chance of recovery if substitution fails
                    if random.random() < 0.3:
                        recovery = determine_random_health_change()
                        player["health"] += max(recovery, 0)
                        print(f"Player '{player['name']}' recovered health to {player['health']}!")

    def adjust_performance(self, team):
        """Applies performance variance to each player."""
        print("Adjusting performance for players based on variance.")
        for player in team.players:
            apply_performance_variance(player)
            print(f"Player '{player['name']}' new rating: {player['rating']:.2f}")

    def apply_fatigue(self, team):
        """Applies fatigue adjustments to the team."""
        print("Applying fatigue to players.")
        for player in team.players:
            adjust_player_stats_for_fatigue(player)
            print(
                f"Player '{player['name']}' stamina reduced to {player['stamina']:.2f}."
            )

    def boost_player_stats(self, player, stat_name, boost_percentage=10):
        """Boosts a specific stat for a player."""
        print(f"Boosting '{stat_name}' for player '{player['name']}' by {boost_percentage}%.")
        apply_boost_to_stat(player, stat_name, boost_percentage)
        print(f"Player '{player['name']}' {stat_name} after boost: {player[stat_name]:.2f}")

    def trigger_random_event(self):
        """Triggers a random game event."""
        event = random_event()
        print(f"Random Event: {event}")

    def announce_team_scores(self, team1, team2):
        """Calculates and announces scores for both teams."""
        team1_score = sum(calculate_score(player) for player in team1.players)
        team2_score = sum(calculate_score(player) for player in team2.players)
        print(f"Team {team1.name} Score: {team1_score:.2f}")
        print(f"Team {team2.name} Score: {team2_score:.2f}")

    def start_game_round(self, team1, team2):
        """Starts a game round with a series of dynamic events."""
        print("Starting a new game round!")
        operation = self.select_operation()
        self.apply_operations(team1, team2, operation)

        self.adjust_performance(team1)
        self.adjust_performance(team2)

        self.apply_fatigue(team1)
        self.apply_fatigue(team2)

        self.trigger_random_event()
        self.announce_team_scores(team1, team2)
