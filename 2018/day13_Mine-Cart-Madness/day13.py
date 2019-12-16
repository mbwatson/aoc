import time
from typing import NamedTuple
import enum

###

def puzzle_input(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()
    return ''

###

loop = '''/----\
|    |
|    |
\\----/'''

links = '''/-----\
|     |
|  /--+--\
|  |  |  |
\\--+--/  |
   |     |
   \\-----/'''

example = r'''/->-\         
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''

class Loc(NamedTuple):
    x: int
    y: int

class Direction(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Turn(enum.Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

def next_turn(turn):
    if turn == Turn.LEFT:
        return Turn.STRAIGHT
    elif turn == Turn.STRAIGHT:
        return Turn.RIGHT
    else:
        return Turn.LEFT

class Cart:
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction
        self.turn = Turn.LEFT

    def __repr__(self):
        return f'Cart({self.location}, {self.direction})'

    def step(self, track):
        x, y  = self.location
        # Determine new location
        if self.direction == Direction.UP:
            self.location = Loc(x, y - 1)
        elif self.direction == Direction.RIGHT:
            self.location = Loc(x + 1, y)
        elif self.direction == Direction.DOWN:
            self.location = Loc(x, y + 1)
        else: # self.direction == Direction.LEFT
            self.location = Loc(x - 1, y)
        # Determine new direction
        rail = track[self.location]
        if rail in ['|', '-']:
            return
        elif rail == '/':
            if self.direction == Direction.UP: self.direction = Direction.RIGHT
            elif self.direction == Direction.RIGHT: self.direction = Direction.UP
            elif self.direction == Direction.DOWN: self.direction = Direction.LEFT
            else: # self.direction == Direction.LEFT
                self.direction = Direction.DOWN
        elif rail == '\\':
            if self.direction == Direction.UP: self.direction = Direction.LEFT
            elif self.direction == Direction.RIGHT: self.direction = Direction.DOWN
            elif self.direction == Direction.DOWN: self.direction = Direction.RIGHT
            else: # self.direction == Direction.LEFT
                self.direction = Direction.UP
        elif rail == '+':
            direction_value = self.direction.value
            if self.turn == Turn.LEFT:
                self.direction = Direction((direction_value - 1) % 4)
            elif self.turn == Turn.RIGHT:
                self.direction = Direction((direction_value + 1) % 4)
            turn_value = self.turn.value
            # self.turn = Turn((turn_value + 4) % 3)
            self.turn = next_turn(self.turn)
        else:
            raise ValueError(f'Bad track {rail} at ({x},{y})')

def parse(input):
    track = {}
    carts = []
    lines = input.split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line.rstrip()):
            location = Loc(x,y)
            if char == ' ':
                continue
            elif char == '^':
                carts.append(Cart(location, Direction.UP))
                track[location] = '|'
            elif char == '>':
                carts.append(Cart(location, Direction.RIGHT))
                track[location] = '-'
            elif char == 'v':
                carts.append(Cart(location, Direction.DOWN))
                track[location] = '|'
            elif char == '<':
                carts.append(Cart(location, Direction.LEFT))
                track[location] = '-'
            else:
                track[location] = char
    return track, carts

def tick_part1(carts, track):
    carts.sort(key=lambda cart: (cart.location.y, cart.location.x))
    cart_locations = { cart.location for cart in carts }
    for cart in carts:
        cart_locations.remove(cart.location)
        cart.step(track)
        if cart.location in cart_locations:
            return cart.location
        cart_locations.add(cart.location)

def part1(input):
    track, carts = parse(input)
    count = 0
    crash = False
    while True:
        crash = tick_part1(carts, track)
        count += 1
        if crash is not None:
            print(f'Crash on tick #{count}.')
            return crash

assert part1(example) == (7,3)

example2 = r'''/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/'''

def part2(input):
    track, carts = parse(input)
    while True:
        print(len(carts))
        carts.sort(key=lambda cart: (cart.location.y, cart.location.x))
        cart_locations = { cart.location: i for i, cart in enumerate(carts) }
        to_be_removed = set()
        for i, cart in enumerate(carts):
            if i in to_be_removed: continue
            del cart_locations[cart.location]
            cart.step(track)
            if cart.location in cart_locations:
                to_be_removed.add(i)
                to_be_removed.add(cart_locations[cart.location])
                del cart_locations[cart.location]
            else:
                cart_locations[cart.location] = i
        carts = [cart for i, cart in enumerate(carts) if i not in to_be_removed]
        if len(carts) == 1:
            return carts[0].location
    return None

###

raw_input = puzzle_input('input.txt')
# raw_input = example
# raw_input = example2
start_time = time.time()

print('\nPart 1')
print('Crash at', part1(raw_input))

print('\nPart 2')
print('Single cart remaining at position', part2(raw_input))

print(f'\n >> Completed in { time.time() - start_time } seconds.')
