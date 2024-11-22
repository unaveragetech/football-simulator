#players.py
import random

# Roles with stat multipliers
ROLES = {
    "quarterback": {"skill": 1.2, "agility": 1.1, "stamina": 0.9, "strength": 1.0},
    "receiver": {"skill": 1.1, "agility": 1.3, "stamina": 1.0, "strength": 0.8},
    "lineman": {"skill": 0.8, "agility": 0.6, "stamina": 1.2, "strength": 1.5},
    "kicker": {"skill": 1.4, "agility": 0.9, "stamina": 0.8, "strength": 0.7},
    "defender": {"skill": 1.0, "agility": 0.7, "stamina": 1.1, "strength": 1.2},
}

# Example list of player names (you can modify this as needed)
PLAYER_NAMES = [
    "John Doe", "Jane Smith", "Mike Taylor", "Sarah Brown", "Chris Lee",
    "David Wilson", "Emma Clark", "James Johnson", "Olivia Harris", "Daniel Martinez",
    "Sophia Robinson", "William Lewis", "Isabella Walker", "Liam Young", "Ava Hall",
    "Ethan Allen", "Mia King", "Benjamin Scott", "Charlotte Wright", "Lucas Adams",
    "Amelia Nelson", "Alexander Green", "Harper Carter", "Henry Murphy", "Ella Perez",
    "Jackson Coleman", "Grace Simmons", "Sebastian Baker", "Chloe Foster", "Matthew Morris",
    "Zoe Cooper", "Jack King", "Lily Hughes", "Daniel Ward", "Madeline Rivera",
    "Michael Gomez", "Layla Morgan", "Joshua Howard", "Megan Lee", "Samuel Clark",
    "Victoria Perez", "Oliver Brooks", "Hannah Lewis", "Isaiah Harris", "Charlotte Stewart",
    "Mason James", "Lily Walker", "Lucas Wright", "Ella Turner", "Johnnie Walker",
    "Sophia Green", "Jacob Mitchell", "Emily Lewis", "Asher Taylor", "Maya Rogers",
    "Jackson Harris", "Amelia Lee", "Wyatt Thompson", "Lila Evans", "Grace Nelson",
    "Jack Carter", "Sophie Ross", "Leo Carter", "Elena Green", "Mason Bailey",
    "Samantha Murphy", "Nathaniel Peterson", "Aiden Ross", "Penelope Adams", "Dylan Foster",
    "Maya Hughes", "Sebastian Mitchell", "Avery Sullivan", "Hunter Kelly", "Lucas Perez",
    "Chloe Stevens", "Jackson Phillips", "Amos Bennett", "Abigail Cook", "Charlotte Simmons",
    "Aiden Wright", "Ethan Torres", "Emily Barnes", "Isaac Griffin", "Sophie James",
    "Benjamin Rodriguez", "Harper Cook", "Matthew Hughes", "Lily Edwards", "Henry Murphy",
    "Jack Peterson", "Samantha Watson", "Julian Bryant", "Aiden Campbell", "Grace Lee",
    "Evan Carter", "Zoe Henderson", "Maya Fisher", "William Ward", "Abigail Kelly",
    "Lucas Cooper", "Avery Clark", "Sophia Stewart", "Henry Diaz", "Anna Fisher",
    "Eliot White", "Samuel Parker", "Chloe Adams", "Liam Roberts", "Amelia Kelly",
    "Charlotte Bailey", "Benjamin Johnson", "Aiden Green", "Megan Kelly", "Sophie Allen",
    "Ethan Campbell", "Chloe Evans", "Wyatt Murphy", "Liam Collins", "Olivia Henderson",
    "Daniel Baker", "Evan James", "Mason Wright", "Hannah Young", "Henry Gonzalez",
    "Ava Allen", "Jacob Brown", "Olivia Davis", "Isaiah Harris", "Grace Morris"
]


def generate_player(role="quarterback"):
    """Generates a player with stats adjusted for their role."""
    # Select a random name for the player
    name = random.choice(PLAYER_NAMES)
    
    # Generate stats based on the role
    skill = round(random.uniform(0, 100) * ROLES[role]["skill"], 4)
    adjusted_skill = round(skill - 500, 6)
    agility = int(random.randint(-10, 10) * ROLES[role]["agility"])
    stamina = round(random.uniform(0, 50) * ROLES[role]["stamina"], 2)
    strength = int(random.randint(1, 20) * ROLES[role]["strength"])
    luck = round(random.uniform(0, 100), 2)  # Adding luck stat for the player
    health = random.randint(80, 100)  # Players start with a random health level
    rating = round((skill + agility + stamina + strength) / 4, 2)

    return {
        "name": name,  # Add name to the player data
        "role": role,
        "skill": skill,
        "adjusted_skill": adjusted_skill,
        "agility": agility,
        "stamina": stamina,
        "strength": strength,
        "luck": luck,  # Ensure luck is included in the player data
        "health": health,
        "rating": rating,
    }
