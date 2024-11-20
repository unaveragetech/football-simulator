

### **Football Simulator Overview**

This Football Simulator is a text-based game where two teams compete in a football-like environment. Each team consists of 53 players, and the simulation allows for dynamic gameplay with various interactions like player substitutions based on health, performance variance, and score tracking. The coach has a role in setting up strategies for player health thresholds and stats preferences. 

---

### **Key Concepts and Interactions**

1. **Teams**: Each team consists of 53 players, each with a designated role. Players have stats that influence their performance, including:
   - **Health**: A percentage indicating the player’s current condition.
   - **Rating**: A composite rating based on various player stats, influencing their performance in the game.
   - **Stats**: 
     - **Skill**: Measures a player's overall football skill.
     - **Agility**: Reflects how quick and flexible the player is.
     - **Stamina**: Indicates how well a player can maintain performance over time.
     - **Strength**: Represents physical power for the player.
  
2. **Roles**: Each player is assigned a role (e.g., quarterback, receiver, lineman, kicker, defender) that has specific stat multipliers. The roles determine how the player performs based on the stats.

3. **Substitution**: If a player’s health falls below a set threshold (defined by the coach), that player is substituted with a new one, keeping the same role but with different stats and a new health percentage.

4. **Performance Variance**: Players can perform better or worse in different rounds depending on a random performance factor that adjusts their rating within a certain range (80%-120%).

5. **Game Rounds**: The game runs for several rounds where different operations (e.g., addition, subtraction, multiplication, division) are applied to the teams' scores, and players' stats affect the result of those operations.

6. **Score Calculation**: Each team's score is derived from the sum of all players' ratings. The more skilled and healthy the players, the higher the team's score.

7. **Coach Strategy**: The coach can set a health threshold for substitutions and choose a preferred player stat (like skill, stamina, etc.) that affects the gameplay. For example, the team might focus on skill or stamina depending on the strategy chosen by the coach.

8. **Operations**: Each round, a random operation (addition, subtraction, multiplication, or division) is applied to the team's scores, with the performance of the players factoring into how much they contribute to the team's overall score. 

---

### **Detailed Gameplay Flow**

1. **Initial Setup**:
   - The game starts by asking the user for the names of the two teams.
   - The coach is then asked to set their strategy:
     - Minimum health threshold for players (e.g., 30%).
     - Preferred player stat (e.g., skill, stamina, etc.) for further decision-making.

2. **Team Generation**:
   - Each team generates a roster of 53 players, randomly choosing their roles (quarterback, receiver, lineman, kicker, defender). Each player’s stats are calculated based on their role's multipliers.

3. **Round-by-Round Operations**:
   - For each round (typically 10 rounds in a match):
     - An operation is randomly selected (e.g., add, subtract, multiply, divide).
     - The players’ ratings contribute to the score based on this operation. The team's overall performance is affected by player health and stats.
     - Players may be substituted if their health falls below the set threshold.
     - The score for each team is updated after each round.

4. **Substitutions**:
   - Players whose health drops below the health threshold are substituted. The coach sets this threshold before the game begins.
   - The substituted player is replaced with a new player with the same role, but fresh stats and health.

5. **Performance Variance**:
   - Each player’s performance during a round is influenced by a random variance factor (between 80% and 120%), affecting their overall rating and performance.

6. **Final Score**:
   - After 10 rounds, the final scores for both teams are displayed.
   - The team with the higher score wins. If both teams have equal scores, the result is a tie.

---

### **Code Details**

#### **`team.py`**:

- **Team Class**:
  - `__init__(self, name)`: Initializes the team with a name and an empty roster of players, as well as a score.
  - `generate_team()`: Creates 53 players for the team, each randomly assigned a role.
  - `display_team()`: Displays the current team’s roster with players’ stats, health, and rating.
  - `substitute_player(player_index)`: Substitutes a player whose health is below the threshold with a new player.
  - `get_active_players(health_threshold)`: Returns a list of players whose health is above a given threshold.
  - `calculate_score()`: Calculates the team's total score based on the sum of all players’ ratings.
  - `apply_player_variance()`: Randomly adjusts each player's rating within a variance range (80% to 120%).

#### **`players.py`**:

- **Player Stats**:
  - Defines roles (quarterback, receiver, etc.) with multipliers for different player stats.
  - The `generate_player()` function generates a player with stats influenced by their role and applies random variance to those stats.
  - Each player has a health percentage (starting at 100%) and a rating calculated from their stats.

---

### **Detailed README**

---

# **Football Simulator Game**

Welcome to the **Football Simulator**! This game allows you to simulate a football match between two teams, where you can manage players, set strategies, and see how your team performs based on stats, player health, and random performance variance.

## **Features**
- **Team Generation**: Automatically generate teams with 53 players, each with unique stats based on their role.
- **Substitution Mechanism**: Players can be substituted if their health drops below a specified threshold.
- **Performance Variance**: Players’ performance varies randomly based on a variance factor (80% to 120% of their base stats).
- **Strategy Settings**: The coach can set strategies, including a health threshold for substitutions and a preferred stat (e.g., skill, stamina).
- **Score Calculation**: The score is determined by the sum of player ratings, influenced by health and stats.
- **Operations**: Each round features a randomly selected operation (addition, subtraction, multiplication, division) that affects the team's score.

## **How to Play**
1. **Set Up**:
   - Upon running the game, enter the names for **Team 1** and **Team 2**.
   - As the coach, set your strategy by providing a **minimum health threshold** (the health percentage below which a player will be substituted) and choose a **preferred player stat** (e.g., skill, stamina, etc.).
   
2. **Team Generation**:
   - Each team will automatically generate a roster of 53 players, each assigned a random role (quarterback, receiver, lineman, kicker, defender).
   
3. **Rounds**:
   - The game will run for 10 rounds, with each round featuring a random operation (add, subtract, multiply, divide).
   - The players' ratings contribute to the team score based on the selected operation.

4. **Substitution**:
   - If a player's health falls below the defined threshold, they will be substituted with a new player of the same role.

5. **Performance Variance**:
   - Each player's rating may vary slightly during the rounds, influenced by a random performance factor (between 80% and 120%).

6. **Final Scores**:
   - After 10 rounds, the final scores are calculated. The team with the higher score wins. If the scores are tied, the game ends in a draw.

## **Game Flow Example**

1. **Start the Game**:
   - Team names are set (e.g., apples, grapes).
   - Coach sets the health threshold (e.g., 30%) and chooses the preferred stat (e.g., skill).
   
2. **Rounds**:
   - Each round applies a random operation (e.g., add, subtract, etc.) and updates the teams' scores based on player ratings.
   - Players who fall below the health threshold are substituted.
   - Player performance is affected by random variance, so ratings may change slightly.

3. **End of the Game**:
   - After 10 rounds, the final scores are displayed.
   - The team with the highest score is declared the winner.

---

## **Installation**

To run the Football Simulator on your local machine, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/football-simulator.git
   cd football-simulator
   ```

2. **Install Dependencies**:
   This project does not require any external dependencies, but you may need Python 3.x installed.

3. **Run the Game**:
   ```
   python main.py
   ```

---

### **Contributions**
Feel free to contribute to the project by opening issues or submitting pull requests for additional features, bug fixes, or performance improvements.

