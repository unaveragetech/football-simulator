from players.py import generate_player

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def generate_team(self):
        """Generates a full team of 53 players."""
        roles = ["quarterback", "receiver", "lineman", "kicker"]
        for _ in range(53):
            role = random.choice(roles)
            player = generate_player(role)
            self.players.append(player)

    def display_team(self):
        """Displays the current team."""
        print(f"\n{self.name} Roster:")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player['role'].title()} - Health: {player['health']}% - Rating: {player['rating']}")
