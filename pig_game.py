import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Please enter player number 2-6: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=6:
            break
        else:
            print("ERROR! Enter a number between 2 and 6.")
    else:
        print("ERROR! Enter a number.")

print(f"There is {players} players.")

max_score = 100
player_score = [0 for i in range(players)]
print(player_score)

while max(player_score) <= max_score:
    
    for i in range(players):
        print("\nPlayer", i+1, "turn just started.\n")
        print(f"Your total score is {player_score[i]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Whould you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
                
            value = roll()
            
            if value == 1:
                print("You rolled 1. Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled {value}.")

            print(f"Your score is {current_score}.")
            print(f"Your total score is: {player_score[i]}")

max_score = max(player_score)
winning_id = player_score.index(max_score)
print(f"Player number {winning_id + 1} won with a score of {max_score}!")
