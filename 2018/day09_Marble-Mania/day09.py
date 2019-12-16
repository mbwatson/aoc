import time
from itertools import cycle
from collections import deque

###

def insert_marble(circle, marble, position):
    circle.rotate(-position)
    circle.appendleft(marble)
    circle.rotate(position)

def game(player_count, marble_count):
    print(f'{player_count} player_count, {marble_count} marble_count')
    # setup game
    players = {i + 1: 0 for i in range(player_count)}
    marbles = list(range(1, marble_count+1))
    circle = deque([0])
    current = 0
    last_position = 0
    current_position = 0
    player = 1
    # play
    for i in cycle(range(9)):
        # show game state
        print('= ' * 20)
        print(' Players :', players)
        print(' Marbles :', marbles)
        print('  Circle :', circle)
        next_marble = marbles.pop(0)
        # print('    Next :', next_marble)
        current_position = last_position + 2
        if next_marble % 23 == 0:
            print('           ↳ Multiple of 23')
            circle.rotate(7)
            players[i] += 23 + circle.pop()
            circle.rotate(-1)
        else:
            insert_marble(circle, next_marble, current_position)
            last_position = current_position
        if next_marble == 25:
            break

###

start_time = time.time()

print('\nPart 1')
print(game(player_count=9, marble_count=25))

print(f'\n >> Completed in { time.time() - start_time } seconds.')
