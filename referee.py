import random

class Referee:
    def apply_injury(self, player):
        """Randomly injures a player."""
        injury_chance = random.uniform(0, 1)
        if injury_chance <= 0.1:
            injury = random.randint(10, 30)
            player["health"] -= injury
            player["health"] = max(player["health"], 0)
            print(f"Referee: {player['role'].title()} injured! -{injury} Health.")
        return player
