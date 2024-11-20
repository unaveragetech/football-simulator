from game import FootballGame
from team import Team

def main():
    print("Welcome to the Football Simulation Game!")
    
    # Create teams
    team1_name = input("Enter the name of Team 1: ")
    team2_name = input("Enter the name of Team 2: ")
    team1 = Team(team1_name)
    team2 = Team(team2_name)

    # Generate players for both teams
    team1.generate_team()
    team2.generate_team()

    # Start the game
    game = FootballGame(team1, team2)
    game.play_game()

if __name__ == "__main__":
    main()
