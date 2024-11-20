import csv
from game import FootballGame
from team import Team
from referee import Referee
import random

def main():
    print("Welcome to the Football Simulator!")

    # Team Setup
    team1_name = input("Enter the name for Team 1: ")
    team2_name = input("Enter the name for Team 2: ")

    team1 = Team(team1_name)
    team2 = Team(team2_name)

    team1.generate_team()
    team2.generate_team()

    # Display team rosters
    print("\n--- Team Rosters ---")
    team1.display_team()
    team2.display_team()

    print("\n--- Team Setup Complete ---")
    print(f"{team1.name} and {team2.name} are ready to compete!")

    # Coach Strategy Setup
    min_health_threshold = int(input("Enter the minimum health threshold for players (0-100): "))
    preferred_stat = input("Choose your preferred player stat (skill, stamina, agility, defense, luck): ")

    # Referee and Game Setup
    referee = Referee()

    # Ask the coach to specify the number of rounds
    rounds = int(input("Enter the number of rounds for the game: "))

    # Ask coach if they want to play round by round or all at once
    game_mode = input("\nChoose Game Mode: \n1. Play All at Once\n2. Play Round by Round\nEnter choice (1 or 2): ")

    # Open CSV file to log the game interactions with detailed player stats
    with open(f'{team1.name}_vs_{team2.name}_game_log.csv', 'w', newline='') as csvfile:
        fieldnames = ['Round', 'Operation', 'Team 1 Score', 'Team 2 Score', 'Team 1 Player Stats', 'Team 2 Player Stats', 
                      'Team 1 Player Health', 'Team 2 Player Health', 'Team 1 Substitutions', 'Team 2 Substitutions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        if game_mode == "1":
            print("\n--- Playing Full Game ---")
            # Play the full game at once
            for round_num in range(1, rounds + 1):
                print(f"\n--- Round {round_num} ---")
                operation = referee.select_operation()
                print(f"Operation this round: {operation}")
                
                # Apply operation and update player stats
                referee.apply_operations(team1, team2, operation)

                # Calculate team scores after the operation
                team1.calculate_score()
                team2.calculate_score()

                print(f"Team {team1.name} Score: {team1.score}")
                print(f"Team {team2.name} Score: {team2.score}")

                # Check for any player injuries and substitutions
                referee.handle_injuries(team1, min_health_threshold)
                referee.handle_injuries(team2, min_health_threshold)

                # Log detailed round information into the CSV
                writer.writerow({
                    'Round': round_num,
                    'Operation': operation,
                    'Team 1 Score': team1.score,
                    'Team 2 Score': team2.score,
                    'Team 1 Player Stats': team1.get_player_stats(),
                    'Team 2 Player Stats': team2.get_player_stats(),
                    'Team 1 Player Health': team1.get_health_status(),
                    'Team 2 Player Health': team2.get_health_status(),
                    'Team 1 Substitutions': team1.get_substitutions(),
                    'Team 2 Substitutions': team2.get_substitutions()
                })

            # Final Results
            print("\n--- Final Scores ---")
            print(f"{team1.name}: {team1.score}")
            print(f"{team2.name}: {team2.score}")

            if team1.score > team2.score:
                print(f"{team1.name} wins!")
            elif team2.score > team1.score:
                print(f"{team2.name} wins!")
            else:
                print("It's a tie!")

        elif game_mode == "2":
            print("\n--- Playing Round by Round ---")
            # Play round by round
            for round_num in range(1, rounds + 1):
                print(f"\n--- Round {round_num} ---")
                operation = referee.select_operation()
                print(f"Operation this round: {operation}")
                
                # Apply operation and update player stats
                referee.apply_operations(team1, team2, operation)

                # Calculate team scores after the operation
                team1.calculate_score()
                team2.calculate_score()

                print(f"Team {team1.name} Score: {team1.score}")
                print(f"Team {team2.name} Score: {team2.score}")

                # Check for any player injuries and substitutions
                referee.handle_injuries(team1, min_health_threshold)
                referee.handle_injuries(team2, min_health_threshold)

                # Log detailed round information into the CSV
                writer.writerow({
                    'Round': round_num,
                    'Operation': operation,
                    'Team 1 Score': team1.score,
                    'Team 2 Score': team2.score,
                    'Team 1 Player Stats': team1.get_player_stats(),
                    'Team 2 Player Stats': team2.get_player_stats(),
                    'Team 1 Player Health': team1.get_health_status(),
                    'Team 2 Player Health': team2.get_health_status(),
                    'Team 1 Substitutions': team1.get_substitutions(),
                    'Team 2 Substitutions': team2.get_substitutions()
                })

                # Ask if the coach wants to continue to the next round or end the game
                continue_game = input("Do you want to continue to the next round? (y/n): ")
                if continue_game.lower() != 'y':
                    break

            # Final Results
            print("\n--- Final Scores ---")
            print(f"{team1.name}: {team1.score}")
            print(f"{team2.name}: {team2.score}")

            if team1.score > team2.score:
                print(f"{team1.name} wins!")
            elif team2.score > team1.score:
                print(f"{team2.name} wins!")
            else:
                print("It's a tie!")

        else:
            print("Invalid choice! Please restart the game and select either 1 or 2.")

if __name__ == "__main__":
    main()
