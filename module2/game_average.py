
GAMES = 125 # constant
# Your team plays 125 games per season
print('Welcome to the game average program')
print('You played ', GAMES, ' this season')
# Task 1: Prompt the user for the number of wins, draws, and losses
# The sum of wins + draws = losses = GAMES
prompt = 'Out of ' + str(GAMES) + ' how many games did you win?'
wins = int(input(prompt))
games_left = GAMES - wins
prompt = 'Out of ' + str(games_left) + ' how many games did you lose?'
lost = int(input(prompt))
draw = GAMES - wins - lost
print('That means you had ', draw, ' games last season')
# Task 2: Calculate the percentage of wins, draws, and losses

