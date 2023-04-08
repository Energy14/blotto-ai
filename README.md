# Blotto-AI
This is a variation of the Colonel Blotto game with AI opponent.
GUI is built using Flet framework.
AI opponent works by generating a game tree for all possible moves for the next 4 turns.
Then it uses heuristics function to find the most optimal next move.
### Game rules:
Each player has the same amount of troops and three battlefields where they can be distributed.
Players take turns and can move two troops per turn. When both players have no troops left,
game ends and the player who has more troops on two of the three battlefields wins.
If none of the players have more troops on two of the battlefields, it's a draw.