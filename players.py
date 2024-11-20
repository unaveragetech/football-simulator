import random

# Roles with stat multipliers
ROLES = {
    "quarterback": {"skill": 1.2, "agility": 1.1, "stamina": 0.9, "strength": 1.0},
    "receiver": {"skill": 1.1, "agility": 1.3, "stamina": 1.0, "strength": 0.8},
    "lineman": {"skill": 0.8, "agility": 0.6, "stamina": 1.2, "strength": 1.5},
    "kicker": {"skill": 1.4, "agility": 0.9, "stamina": 0.8, "strength": 0.7},
}

def generate_player(role="quarterback"):
    skill = round(random.uniform(0, 100) * ROLES[role]["skill"], 4)
    adjusted_skill = round(skill - 500, 6)
    agility = int(random.randint(-10, 10) * ROLES[role]["agility"])
    stamina = round(random.uniform(0, 50) * ROLES[role]["stamina"], 2)
    strength = int(random.randint(1, 20) * ROLES[role]["strength"])
    health = 100
    rating = round((skill + agility + stamina + strength) / 4, 2)
    return {
        "role": role,
        "skill": skill,
        "adjusted_skill": adjusted_skill,
        "agility": agility,
        "stamina": stamina,
        "strength": strength,
        "health": health,
        "rating": rating,
    }
