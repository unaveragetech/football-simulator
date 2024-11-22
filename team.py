from players import generate_player
from players import PLAYER_NAMES

import random

class Team:
    def __init__(self, name):
        """
        Initializes a team with a given name, an empty list of players, and a score of 0.
        
        Attributes:
            name (str): The name of the team.
            players (list): List of player dictionaries with their stats.
            score (int): The team's total score.
            substitutions (list): A log of all substitutions made during the game.
        """
        self.name = name
        self.players = []
        self.score = 0
        self.substitutions = []
        

    def get_health_status(self):
        """
        Returns the health status of all players.
        
        Returns:
            list: List of strings summarizing player health.
        """
        return [f"{player['name']}: {player['health']}%" for player in self.players]

    def generate_team(self):
        """
        Generates a full team of 53 players with random roles.
        Each player is created with attributes based on their role.
        """
        roles = ["quarterback", "receiver", "lineman", "kicker", "defender"]
        used_names = set()  # Track used player names to ensure uniqueness
        for _ in range(53):
            role = random.choice(roles)
            player = generate_player(role)
            
            # Ensure the name is unique
            while player["name"] in used_names:
                player["name"] = random.choice(PLAYER_NAMES)
            used_names.add(player["name"])

            self.players.append(player)

    def display_team(self):
        """
        Displays the current roster of the team with detailed player stats.
        """
        print(f"\n{self.name} Roster:")
        for i, player in enumerate(self.players, 1):
            print(
                f"{i}. {player['role'].title()} - "
                f"Name: {player['name']} - "
                f"Health: {player['health']}% - "
                f"Rating: {player['rating']:.2f} - "
                f"Stats: Skill {player['skill']}, Agility {player['agility']}, "
                f"Stamina {player['stamina']}, Strength {player['strength']}, "
                f"Luck: {player['luck']}"
            )

    def substitute_player(self, player_index):
        """
        Substitutes a player with a new one of the same role, typically due to low health.
        
        Args:
            player_index (int): The index of the player to substitute.
        """
        old_player = self.players[player_index]
        print(f"Substituting Player {player_index + 1} ({old_player['role']}) due to low health.")
        
        new_player = generate_player(old_player["role"])
        new_player['name'] = f"Player_{random.randint(1, 10000)}"
        self.players[player_index] = new_player
        
        print(f"New Player: {new_player['role']} - Health: {new_player['health']} - Name: {new_player['name']}")
        self.substitutions.append((old_player, new_player))

    def get_active_players(self, health_threshold):
        """
        Returns a list of players whose health is above a certain threshold.
        
        Args:
            health_threshold (int): The minimum health percentage to be considered active.
        
        Returns:
            list: Active players with health above the threshold.
        """
        return [player for player in self.players if player["health"] >= health_threshold]

    def calculate_score(self):
        """
        Calculates the team's score as the sum of all player ratings.
        
        Returns:
            int: The total team score.
        """
        self.score = sum(player['rating'] for player in self.players)
        return self.score

    def apply_player_variance(self):
        """
        Applies a random performance variance to each player's rating.
        Ensures the rating stays between 0 and 100.
        """
        for player in self.players:
            performance_factor = random.uniform(0.8, 1.2)  # Random factor between 80% and 120%
            player['rating'] *= performance_factor
            player['rating'] = max(0, min(player['rating'], 100))  # Clamp rating to range 0-100

    def calculate_performance_grade(self, player):
        """
        Calculates a player's performance grade based on their stats.
        
        Args:
            player (dict): A dictionary of the player's stats.
        
        Returns:
            str: Performance grade ('A', 'B', 'C', 'D', 'F').
        """
        performance_score = (
            0.4 * player['skill'] +
            0.2 * player['stamina'] +
            0.2 * player['agility'] +
            0.1 * player['strength'] +
            0.1 * player['luck']
        )
        if performance_score >= 90:
            return 'A'
        elif performance_score >= 75:
            return 'B'
        elif performance_score >= 60:
            return 'C'
        elif performance_score >= 50:
            return 'D'
        else:
            return 'F'

    def get_team_stats(self):
        """
        Summarizes the team's overall stats.
        
        Returns:
            str: A formatted string of average team stats.
        """
        if not self.players:
            return "No players in the team."
        
        total_skill = sum(player['skill'] for player in self.players)
        total_stamina = sum(player['stamina'] for player in self.players)
        total_agility = sum(player['agility'] for player in self.players)
        total_strength = sum(player['strength'] for player in self.players)
        total_luck = sum(player['luck'] for player in self.players)
        num_players = len(self.players)

        stats_summary = (
            f"Team {self.name} Stats:\n"
            f"Average Skill: {total_skill / num_players:.2f}\n"
            f"Average Stamina: {total_stamina / num_players:.2f}\n"
            f"Average Agility: {total_agility / num_players:.2f}\n"
            f"Average Defense: {total_strength / num_players:.2f}\n"
            f"Average Luck: {total_luck / num_players:.2f}\n"
        )
        return stats_summary

    def get_player_stats(self):
        """
        Summarizes stats for all players in the team.
        
        Returns:
            str: A formatted string of individual player stats.
        """
        player_stats = []
        for player in self.players:
            player_info = (
                f"Player Name: {player['name']}\n"
                f"Role: {player['role']}\n"
                f"Skill Level: {player['skill']} (Scoring and assists impact)\n"
                f"Stamina: {player['stamina']} (Performance over time)\n"
                f"Agility: {player['agility']} (Quick responses)\n"
                f"Defense: {player['strength']} (Blocking ability)\n"
                f"Luck: {player['luck']} (Random chance factor)\n"
                f"Health: {player['health']}%\n"
                f"Performance Grade: {self.calculate_performance_grade(player)}\n"
                f"-----------------------------"
            )
            player_stats.append(player_info)
        return "\n".join(player_stats)

    def get_substitutions(self):
        """
        Returns a summary of all substitutions made during the game.
        
        Returns:
            list: A log of substitutions as tuples (old_player, new_player).
        """
        return [
            f"Substituted {old['name']} (Health: {old['health']}%) with {new['name']} (Health: {new['health']}%)"
            for old, new in self.substitutions
        ]
