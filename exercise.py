"""
Write a Python program that reads two files player1.txt and player2.txt. These files are organized according to the above rules.
The program should compare both inputs and calculate how many games have been won by player1, by player2 and how many games ended in a draw.
"""
player_one_list = []
player_two_list = []
results = [0, 0, 0]
with open('player1.txt', 'r') as file:
    for line in file:
        line.strip()
        player_one_list += line.strip()

with open('player2.txt', 'r') as file1:
    for line in file1:
        line.strip()
        player_two_list += line.strip()
i = 0
while i < len(player_two_list):
    # Rock, paper, scissors logic
    if player_one_list[i] == 'R' and player_two_list[i] == 'S':
        results[0] += 1
    elif player_one_list[i] == 'S' and player_two_list[i] == 'R':
        results[1] += 1
    elif player_one_list[i] == 'R' and player_two_list[i] == 'R':
        results[2] += 1
    elif player_one_list[i] == 'S' and player_two_list[i] == 'S':
        results[2] += 1
    elif player_one_list[i] == 'P' and player_two_list[i] == 'P':
        results[2] += 1
    elif player_one_list[i] == 'R' and player_two_list[i] == 'P':
        results[1] += 1
    elif player_one_list[i] == 'P' and player_two_list[i] == 'R':
        results[0] += 1
    elif player_one_list[i] == 'P' and player_two_list[i] == 'S':
        results[1] += 1
    elif player_one_list[i] == 'S' and player_two_list[i] == 'P':
        results[0] += 1
    i += 1
print(f"Player1 wins: {results[0]}")
print(f"Player2 wins: {results[1]}")
print(f"Draws: {results[2]}")