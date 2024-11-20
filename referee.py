# referee.py
import random


class Referee:
    def select_operation(self):
        """Randomly selects an operation for the round."""
        operations = ["add", "subtract", "multiply", "divide"]
        return random.choice(operations)

    def apply_operations(self, team1, team2, operation):
        """Applies the selected operation to each player on both teams."""
        for player in team1.players:
            self.apply_operation_to_player(player, operation)

        for player in team2.players:
            self.apply_operation_to_player(player, operation)

    def apply_operation_to_player(self, player, operation):
        """Applies the operation to a player's stats."""
        if operation == "add":
            player["rating"] += random.uniform(0, 5)
        elif operation == "subtract":
            player["rating"] -= random.uniform(0, 5)
        elif operation == "multiply":
            player["rating"] *= random.uniform(1, 2)
        elif operation == "divide":
            player["rating"] /= random.uniform(1.1, 2)

    def handle_injuries(self, team, health_threshold):
        """Randomly injures players and substitutes them if their health is below the threshold."""
        for i, player in enumerate(team.players):
            if player["health"] < health_threshold:
                print(f"Player {i + 1} from {team.name} is injured!")
                team.substitute_player(i)
