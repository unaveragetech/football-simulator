# utils.py
import random
import math

def flip_coin():
    """Randomly returns 'heads' or 'tails'."""
    return random.choice(["heads", "tails"])

def random_operation():
    """Randomly returns one of several mathematical operations."""
    operations = ["add", "subtract", "multiply", "divide", "modulus", "exponentiate", "sqrt"]
    return random.choice(operations)

def apply_operation(value, weather_condition, operation):
    """
    Applies the specified operation to a value, adjusted by weather condition.

    Args:
        value (float): The value to be operated on.
        weather_condition (float): A factor that modifies the operation.
        operation (str): The operation to perform.

    Returns:
        float: The result of applying the operation.

    Raises:
        ValueError: If the operation or inputs are invalid.
    """
    if operation == "add":
        return value + weather_condition
    elif operation == "subtract":
        return value - weather_condition
    elif operation == "multiply":
        return value * weather_condition
    elif operation == "divide":
        return value / weather_condition if weather_condition != 0 else value
    elif operation == "modulus":
        return value % weather_condition if weather_condition != 0 else value
    elif operation == "exponentiate":
        return value ** weather_condition
    elif operation == "sqrt":
        if value >= 0:
            return math.sqrt(value)
        else:
            raise ValueError("Square root operation requires a non-negative value.")
    elif operation == "factorial":
        if isinstance(value, int) and value >= 0:
            return factorial(value)
        else:
            raise ValueError("Factorial operation requires a non-negative integer.")
    else:
        raise ValueError(f"Unknown operation: {operation}")

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
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
    performance_factor = random.uniform(*variance_range)
    player['rating'] *= performance_factor
    player['rating'] = max(0, min(player['rating'], 100))

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
        "health": random.randint(50, 100),
        "rating": random.randint(50, 100)
    }
    return player_stats

def determine_random_health_change():
    """Determines a random change to a player's health (positive or negative)."""
    return random.choice([-10, -5, 0, 5, 10])

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
        return random.uniform(0.5, 0.8)
    elif weather_impact == "snow":
        return random.uniform(0.4, 0.7)
    elif weather_impact == "clear skies":
        return 1.0
    elif weather_impact == "strong winds":
        return random.uniform(0.6, 0.9)
    elif weather_impact == "high crowd noise":
        return random.uniform(0.9, 1.1)
    return 1.0

def simulate_fatigue(player):
    """Simulates fatigue for a player, lowering their stats over time."""
    fatigue_factor = random.uniform(0.9, 1.0)
    player['stamina'] *= fatigue_factor
    player['agility'] *= fatigue_factor
    player['strength'] *= fatigue_factor

def adjust_player_stats_for_fatigue(player):
    """Applies fatigue reduction to all player stats."""
    fatigue_factor = random.uniform(0.8, 1.0)
    player['skill'] *= fatigue_factor
    player['agility'] *= fatigue_factor
    player['stamina'] *= fatigue_factor
    player['strength'] *= fatigue_factor
    player['rating'] *= fatigue_factor
    player['health'] -= random.randint(1, 5)

def apply_boost_to_stat(player, stat_name, boost_percentage):
    """Boosts a specific stat by a given percentage."""
    if stat_name in player:
        boost_amount = player[stat_name] * (boost_percentage / 100)
        player[stat_name] += boost_amount
        player[stat_name] = min(100, player[stat_name])


def get_team_stats(team):
    """
    Returns a string summary of the team's stats.
    
    Args:
        team (Team): The Team object for which stats are to be summarized.

    Returns:
        str: A formatted string containing the team's overall stats.
    """
    total_skill = 0
    total_stamina = 0
    total_agility = 0
    total_defense = 0
    total_luck = 0

    for player in team.players:
        total_skill += player.skill
        total_stamina += player.stamina
        total_agility += player.agility
        total_defense += player.defense
        total_luck += player.luck

    num_players = len(team.players)

    avg_skill = total_skill / num_players if num_players > 0 else 0
    avg_stamina = total_stamina / num_players if num_players > 0 else 0
    avg_agility = total_agility / num_players if num_players > 0 else 0
    avg_defense = total_defense / num_players if num_players > 0 else 0
    avg_luck = total_luck / num_players if num_players > 0 else 0

    stats_summary = (f"Team {team.name} Stats:\n"
                     f"Average Skill: {avg_skill:.2f}\n"
                     f"Average Stamina: {avg_stamina:.2f}\n"
                     f"Average Agility: {avg_agility:.2f}\n"
                     f"Average Defense: {avg_defense:.2f}\n"
                     f"Average Luck: {avg_luck:.2f}\n")

    return stats_summary
