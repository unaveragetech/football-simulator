import time
import csv
from game import FootballGame
from team import Team
from referee import Referee
import random
from players import PLAYER_NAMES


def main():
    print("========================================")
    print("🏈 WELCOME TO THE ULTIMATE FOOTBALL SIMULATOR! 🏈")
    print("========================================")

    # Team Setup
    print("\n--- 🛠️ Team Setup ---")
    team1_name = input("Enter the name for Team 1: ")
    team2_name = input("Enter the name for Team 2: ")

    team1 = Team(team1_name)
    team2 = Team(team2_name)

    print(f"\nBuilding {team1_name}'s roster...")
    team1.generate_team()
    print(f"Building {team2_name}'s roster...")
    team2.generate_team()

    # Display team rosters
    print("\n========================================")
    print("📋 TEAM ROSTERS")
    print("========================================")
    team1.display_team()
    print("----------------------------------------")
    team2.display_team()

    print("\n========================================")
    print(f"🎮 {team1.name} and {team2.name} are ready to compete!")
    print("========================================")

    # Coach Strategy Setup
    print("\n--- 🧠 Coach Strategy Setup ---")
    min_health_threshold = int(input("Enter the minimum health threshold for players (0-100): "))
    preferred_stat = input("Choose your preferred player stat (skill, stamina, agility, defense, luck): ")
    print(f"\nStrategy Set: Minimum Health Threshold = {min_health_threshold}, Preferred Stat = {preferred_stat}")

    # Referee and Game Setup
    referee = Referee()

    print("\n--- ⚙️ Game Setup ---")
    rounds = int(input("Enter the number of rounds for the game: "))
    print(f"\nGame configured for {rounds} rounds.")

    game_mode = input("\nChoose Game Mode: \n1. Play All at Once\n2. Play Round by Round\n3. Auto-Step with Delay\nEnter choice (1, 2, or 3): ")
    step_duration = 0
    if game_mode == "3":
        step_duration = float(input("Enter the delay duration between each round (in seconds): "))

    # Open CSV file to log the game interactions
    with open(f'{team1.name}_vs_{team2.name}_game_log.csv', 'w', newline='') as csvfile:
        fieldnames = ['Round', 'Operation', 'Team 1 Score', 'Team 2 Score', 'Team 1 Player Stats', 'Team 2 Player Stats', 
                      'Team 1 Player Health', 'Team 2 Player Health', 'Team 1 Substitutions', 'Team 2 Substitutions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        if game_mode == "1":
            print("\n--- 🚀 Playing Full Game ---")
            for round_num in range(1, rounds + 1):
                print(f"\n=== Round {round_num} ===")
                operation = referee.select_operation()
                print(f"🔧 Operation this round: {operation}")
                referee.apply_operations(team1, team2, operation)
                team1.calculate_score()
                team2.calculate_score()
                print(f"⚡ {team1.name} Score: {team1.score} | {team2.name} Score: {team2.score}")
                referee.handle_injuries(team1, min_health_threshold)
                referee.handle_injuries(team2, min_health_threshold)
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
            print("\n--- 🏆 Final Results ---")
            print(f"{team1.name}: {team1.score} | {team2.name}: {team2.score}")
            print(f"{team1.name} wins!" if team1.score > team2.score else f"{team2.name} wins!" if team2.score > team1.score else "It's a tie!")

        elif game_mode == "2":
            print("\n--- 🎯 Playing Round by Round ---")
            for round_num in range(1, rounds + 1):
                print(f"\n=== Round {round_num} ===")
                operation = referee.select_operation()
                print(f"🔧 Operation this round: {operation}")
                referee.apply_operations(team1, team2, operation)
                team1.calculate_score()
                team2.calculate_score()
                print(f"⚡ {team1.name} Score: {team1.score} | {team2.name} Score: {team2.score}")
                referee.handle_injuries(team1, min_health_threshold)
                referee.handle_injuries(team2, min_health_threshold)
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
                if input("Do you want to continue to the next round? (y/n): ").lower() != 'y':
                    break
            print("\n--- 🏆 Final Results ---")
            print(f"{team1.name}: {team1.score} | {team2.name}: {team2.score}")
            print(f"{team1.name} wins!" if team1.score > team2.score else f"{team2.name} wins!" if team2.score > team1.score else "It's a tie!")

        elif game_mode == "3":
            print("\n--- 🔄 Playing Automatically with Step Duration ---")
            for round_num in range(1, rounds + 1):
                print(f"\n=== Round {round_num} ===")
                operation = referee.select_operation()
                print(f"🔧 Operation this round: {operation}")
                referee.apply_operations(team1, team2, operation)
                team1.calculate_score()
                team2.calculate_score()
                print(f"⚡ {team1.name} Score: {team1.score} | {team2.name}: {team2.score}")
                referee.handle_injuries(team1, min_health_threshold)
                referee.handle_injuries(team2, min_health_threshold)
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
                time.sleep(step_duration)
            print("\n--- 🏆 Final Results ---")
            print(f"{team1.name}: {team1.score} | {team2.name}: {team2.score}")
            print(f"{team1.name} wins!" if team1.score > team2.score else f"{team2.name} wins!" if team2.score > team1.score else "It's a tie!")

        else:
            print("❌ Invalid choice! Please restart the game and select 1, 2, or 3.")

if __name__ == "__main__":
    main()
