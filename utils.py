# utils.py
import random

def flip_coin():
    """Randomly returns 'heads' or 'tails'."""
    return random.choice(["heads", "tails"])

def random_operation():
    """Randomly returns one of several mathematical operations."""
    operations = ["add", "subtract", "multiply", "divide", "modulus", "exponentiate", "sqrt", "factorial"]
    return random.choice(operations)

def apply_operation(a, b, operation):
    """Applies a random operation to two numbers."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else 0
    elif operation == "modulus":
        return a % b if b != 0 else 0
    elif operation == "exponentiate":
        return a ** b
    elif operation == "sqrt":
        return a ** 0.5 if a >= 0 else 0
    elif operation == "factorial":
        return factorial(a)
    return 0

def factorial(n):
    """Returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_score(player):
    """Weighted score calculation based on player's attributes."""
    return round(
        (player["skill"] * 0.5)
        + (player["agility"] * 0.3)
        + (player["stamina"] * 0.2),
        2,
    )

def apply_performance_variance(player, variance_range=(0.8, 1.2)):
    """Applies a performance variance to a player's rating within a specified range."""
    performance_factor = random.uniform(*variance_range)  # Random factor between the given range
    player['rating'] *= performance_factor  # Adjust rating based on the variance
    player['rating'] = max(0, min(player['rating'], 100))  # Ensure rating stays between 0 and 100

def generate_random_stat():
    """Generates a random stat value for a player."""
    return random.randint(1, 100)

def random_event():
    """Randomly triggers a game event with a description."""
    events = [
        "A player makes a heroic play!",
        "The crowd goes wild after a big win!",
        "A player is injured and needs substitution.",
        "A controversial call by the referee sparks debate.",
        "A touchdown is scored!",
        "A player receives a penalty for unsportsmanlike conduct."
    ]
    return random.choice(events)

def generate_random_player_stat():
    """Generates random player stats, including skill, agility, stamina, and strength."""
    player_stats = {
        "skill": generate_random_stat(),
        "agility": generate_random_stat(),
        "stamina": generate_random_stat(),
        "strength": generate_random_stat(),
        "health": random.randint(50, 100),  # Health value between 50 and 100
        "rating": random.randint(50, 100)  # Rating value between 50 and 100
    }
    return player_stats

def determine_random_health_change():
    """Determines a random change to a player's health (positive or negative)."""
    change = random.choice([-10, -5, 0, 5, 10])  # Health can increase, decrease, or stay the same
    return change

def get_random_player_role():
    """Randomly selects a role for a player."""
    roles = ["quarterback", "receiver", "lineman", "kicker", "defender"]
    return random.choice(roles)

def get_random_impact_factor():
    """Returns a random factor that can affect gameplay, like weather or crowd noise."""
    factors = ["rain", "snow", "clear skies", "strong winds", "high crowd noise"]
    return random.choice(factors)

def apply_weather_impact():
    """Applies a random weather condition impact to gameplay."""
    weather_impact = get_random_impact_factor()
    if weather_impact == "rain":
        return random.uniform(0.5, 0.8)  # Decreases performance in rain
    elif weather_impact == "snow":
        return random.uniform(0.4, 0.7)  # Further decrease in snow
    elif weather_impact == "clear skies":
        return 1.0  # No impact in clear weather
    elif weather_impact == "strong winds":
        return random.uniform(0.6, 0.9)  # Slight decrease in strong winds
    elif weather_impact == "high crowd noise":
        return random.uniform(0.9, 1.1)  # Crowds can either increase or decrease performance
    return 1.0

def simulate_fatigue(player):
    """Simulates fatigue for a player, lowering their stats over time."""
    fatigue_factor = random.uniform(0.9, 1.0)  # Fatigue ranges from 90% to 100% of current stats
    player['stamina'] *= fatigue_factor
    player['agility'] *= fatigue_factor
    player['strength'] *= fatigue_factor

def adjust_player_stats_for_fatigue(player):
    """Applies fatigue reduction to all player stats."""
    fatigue_factor = random.uniform(0.8, 1.0)  # Fatigue reduces stats between 80% to 100%
    player['skill'] *= fatigue_factor
    player['agility'] *= fatigue_factor
    player['stamina'] *= fatigue_factor
    player['strength'] *= fatigue_factor
    player['rating'] *= fatigue_factor  # Adjust rating as well
    player['health'] -= random.randint(1, 5)  # Small health decrease due to fatigue

def apply_boost_to_stat(player, stat_name, boost_percentage):
    """Boosts a specific stat by a given percentage."""
    if stat_name in player:
        boost_amount = player[stat_name] * (boost_percentage / 100)
        player[stat_name] += boost_amount
        player[stat_name] = min(100, player[stat_name])  # Ensure stat doesn't exceed 100

def get_team_stats(team):
    """
    Returns a string summary of the team's stats.
    
    Args:
        team (Team): The Team object for which stats are to be summarized.

    Returns:
        str: A formatted string containing the team's overall stats.
    """
    # Assuming each team has a list of players, and each player has stats
    total_skill = 0
    total_stamina = 0
    total_agility = 0
    total_defense = 0
    total_luck = 0

    # Loop through all players to accumulate stats
    for player in team.players:
        total_skill += player.skill
        total_stamina += player.stamina
        total_agility += player.agility
        total_defense += player.defense
        total_luck += player.luck

    num_players = len(team.players)

    # Calculate average stats
    avg_skill = total_skill / num_players if num_players > 0 else 0
    avg_stamina = total_stamina / num_players if num_players > 0 else 0
    avg_agility = total_agility / num_players if num_players > 0 else 0
    avg_defense = total_defense / num_players if num_players > 0 else 0
    avg_luck = total_luck / num_players if num_players > 0 else 0

    # Generate the string summary of the team stats
    stats_summary = (f"Team {team.name} Stats:\n"
                     f"Average Skill: {avg_skill:.2f}\n"
                     f"Average Stamina: {avg_stamina:.2f}\n"
                     f"Average Agility: {avg_agility:.2f}\n"
                     f"Average Defense: {avg_defense:.2f}\n"
                     f"Average Luck: {avg_luck:.2f}\n")

    return stats_summary