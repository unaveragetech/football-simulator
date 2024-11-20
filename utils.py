import random

def flip_coin():
    """Randomly return an operation."""
    return random.choice(["add", "subtract", "multiply", "divide"])

def calculate_score(player):
    """Weighted score calculation."""
    return round(
        (player["skill"] * 0.5)
        + (player["agility"] * 0.3)
        + (player["stamina"] * 0.2),
        2,
    )
