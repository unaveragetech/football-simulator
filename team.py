from players import generate_player
import random

class Team:
    def __init__(self, name):
        """Initializes a team with a given name, an empty list of players, and a score of 0."""
        self.name = name
        self.players = []  # List to store player data
        self.score = 0  # Initial score
        self.substitutions = []  # List to track substitutions

    def get_health_status(self):
        """Returns a list of player names and their health status."""
        health_status = []
        for player in self.players:
            health_status.append(f"{player['name']}: {player['health']}%")
        return health_status

    def generate_team(self):
        """Generates a full team of 53 players with random roles."""
        roles = ["quarterback", "receiver", "lineman", "kicker", "defender"]
        
        # Generate 53 players with random roles
        for _ in range(53):
            role = random.choice(roles)
            player = generate_player(role)
            # Assign a random name to the player for consistency
            player['name'] = f"Player_{random.randint(1, 10000)}"
            self.players.append(player)

    def display_team(self):
        """Displays the current roster of the team."""
        print(f"\n{self.name} Roster:")
        
        # Print each player's details in a formatted way
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player['role'].title()} - "
                  f"Name: {player['name']} - "
                  f"Health: {player['health']}% - "
                  f"Rating: {player['rating']} - "
                  f"Stats: Skill {player['skill']}, Agility {player['agility']}, "
                  f"Stamina {player['stamina']}, Strength {player['strength']}")

    def substitute_player(self, player_index):
        """Substitutes a player with a new one having the same role, typically due to low health."""
        old_player = self.players[player_index]
        print(f"Substituting Player {player_index + 1} ({old_player['role']}) due to low health.")
        
        # Generate a new player with the same role
        new_player = generate_player(old_player["role"])
        new_player['name'] = f"Player_{random.randint(1, 10000)}"  # Assign new player a random name
        self.players[player_index] = new_player
        
        # Display new player's information
        print(f"New Player: {new_player['role']} - Health: {new_player['health']} - Name: {new_player['name']}")

        # Record the substitution
        self.substitutions.append(new_player)

    def get_active_players(self, health_threshold):
        """Returns a list of players with health above a given threshold."""
        return [player for player in self.players if player["health"] >= health_threshold]

    def calculate_score(self):
        """Calculates and returns the team's score by summing the ratings of all players."""
        self.score = sum(player['rating'] for player in self.players)
        return self.score

    def apply_player_variance(self):
        """Applies a performance variance to each player's rating based on random factors."""
        for player in self.players:
            performance_factor = random.uniform(0.8, 1.2)  # Random factor between 80% and 120%
            player['rating'] *= performance_factor  # Adjust rating based on the variance
            
            # Ensure the rating stays within a reasonable range (0 to 100)
            player['rating'] = max(0, min(player['rating'], 100))

    def get_team_stats(self):
        """
        Returns a string summary of the team's stats.
        
        Returns:
            str: A formatted string containing the team's overall stats.
        """
        total_skill = 0
        total_stamina = 0
        total_agility = 0
        total_defense = 0
        total_luck = 0

        # Loop through all players to accumulate stats
        for player in self.players:
            total_skill += player['skill']
            total_stamina += player['stamina']
            total_agility += player['agility']
            total_defense += player['strength']  # Assuming 'strength' is used for defense
            total_luck += player['luck']  # Using 'luck' stat added in players.py

        num_players = len(self.players)

        # Calculate average stats
        avg_skill = total_skill / num_players if num_players > 0 else 0
        avg_stamina = total_stamina / num_players if num_players > 0 else 0
        avg_agility = total_agility / num_players if num_players > 0 else 0
        avg_defense = total_defense / num_players if num_players > 0 else 0
        avg_luck = total_luck / num_players if num_players > 0 else 0

        # Generate the string summary of the team stats
        stats_summary = (f"Team {self.name} Stats:\n"
                         f"Average Skill: {avg_skill:.2f}\n"
                         f"Average Stamina: {avg_stamina:.2f}\n"
                         f"Average Agility: {avg_agility:.2f}\n"
                         f"Average Defense: {avg_defense:.2f}\n"
                         f"Average Luck: {avg_luck:.2f}\n")

        return stats_summary

    def get_player_stats(self):
        """
        Returns a string summary of each player's stats.
        
        Returns:
            str: A formatted string containing each player's stats.
        """
        player_stats = []
        
        # Loop through each player and add their stats to the list
        for player in self.players:
            player_info = (
                f"Player Name: {player['name']}\n"
                f"Role: {player['role']}\n"
                f"Skill Level: {player['skill']} (Impact on scoring and assists)\n"
                f"Stamina: {player['stamina']} (How long the player can perform effectively)\n"
                f"Agility: {player['agility']} (Quickness in responding to situations)\n"
                f"Defense: {player['strength']} (Ability to block opponents)\n"
                f"Luck: {player['luck']} (Chance-based positive outcomes)\n"
                f"Health Status: {player['health']}%\n"
                f"Substitution Status: {'Available' if player['health'] > 0 else 'Injured'}\n"
                f"Performance Grade: {self.calculate_performance_grade(player)}\n"
                f"-----------------------------"
            )
            player_stats.append(player_info)
        
        # Join all the player stats into one string
        return "\n".join(player_stats)

    def get_substitutions(self):
        """Returns the list of substitutions made for the team."""
        return self.substitutions
