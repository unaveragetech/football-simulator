from referee import Referee
from utils import flip_coin, calculate_score

class FootballGame:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.referee = Referee()
        self.rounds = 10
        self.team1_score = 0
        self.team2_score = 0

    def play_game(self):
        """Simulate the game."""
        print(f"Game Start: {self.team1.name} vs {self.team2.name}")
        for round_num in range(1, self.rounds + 1):
            print(f"\n=== Round {round_num} ===")
            
            # Coin flip
            operation = flip_coin()
            print(f"Operation: {operation.upper()}")

            # Team decisions
            print(f"\n{self.team1.name} selects players.")
            self.team1.display_team()
            print(f"\n{self.team2.name} selects players.")
            self.team2.display_team()

            # Apply referee decisions
            self.team1.players = [self.referee.apply_injury(player) for player in self.team1.players]
            self.team2.players = [self.referee.apply_injury(player) for player in self.team2.players]

            # Calculate scores
            self.team1_score += sum(calculate_score(player) for player in self.team1.players)
            self.team2_score += sum(calculate_score(player) for player in self.team2.players)

            print(f"\nRound {round_num} Results:")
            print(f"{self.team1.name} Total Score: {self.team1_score}")
            print(f"{self.team2.name} Total Score: {self.team2_score}")

        # Final result
        print("\n=== Final Score ===")
        winner = self.team1.name if self.team1_score > self.team2_score else self.team2.name
        print(f"{self.team1.name}: {self.team1_score} | {self.team2.name}: {self.team2_score}")
        print(f"Winner: {winner}!")
