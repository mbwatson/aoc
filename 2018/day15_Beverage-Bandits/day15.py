from typing import NamedTuple

def steps(x,y):
    return { (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) }

def readfile(filename):
    with open(filename) as f:
        return f.read()

class Loc(NamedTuple):
    x: int
    y: int
    def __repr__(self):
        return f'({self.x}, {self.y})'

class Elf:
    def __init__(self, x, y):
        self.location = Loc(x,y)
        self.power = 3
        self.hp = 200

    def __repr__(self):
        return f'E{self.location}'

class Goblin:
    def __init__(self, x, y):
        self.location = Loc(x,y)
        self.power = 3
        self.hp = 200

    def __repr__(self):
        return f'G{self.location}'

    def steps(self, map, elves):
        return steps(self.location) & map.empty

class Map:
    def __init__(self, input):
        rows = input.split('\n')
        self.width = len(rows[0])
        self.height = len(rows)
        self.walls = []
        self.elves = []
        self.goblins = []
        self.empty = []
        for y, line in enumerate(rows):
            for x, char in enumerate(line):
                if char == '#':
                    self.walls.append((x,y))
                elif char == 'E':
                    self.elves.append(Elf(x,y))
                elif char == 'G':
                    self.goblins.append(Goblin(x,y))
                else: # char == '.'
                    self.empty.append((x,y))
        print(sorted(self.walls))
        print(self.elves)
        print(self.goblins)
        print(self.empty)
        print(input)

    def __repr__(self):
        for y in range(self.height):
            for x in range(self.width):
                print(x,y)

    def occupant(x,y):
        if (x,y) in self.walls:
            return 'wall'
        elif (x,y) in self.goblin:
            return 'goblin'

def part1(input):
    map = Map(input)
    print(map.elves[0])
    loc = map.elves[0].location
    print(map.steps())

test_input = '''#######
#.G.E.#
#E.G.E#
#.G.E.#
#######'''

input = readfile('input.txt')
input = test_input

print('Part 1')
print('======')
part1(input)