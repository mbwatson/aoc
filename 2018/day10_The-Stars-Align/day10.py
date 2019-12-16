import time
import re
import math

###

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f'Point: ({self.x},{self.y}) <{self.dx},{self.dy}>'

    def move(self, num_seconds=1):
        self.x += num_seconds * self.dx
        self.y += num_seconds * self.dy

def grid(points):
    locations = set()
    for p in points:
        locations.add((p.x, p.y))
    minx = min(p.x for p in points)
    miny = min(p.y for p in points)
    maxx = max(p.x for p in points)
    maxy = max(p.y for p in points)
    grid = [['#' if (x,y) in locations else '.'
            for x in range(minx, maxx + 1)]
            for y in range(miny, maxy + 1)]
    return '\n'.join(''.join(row) for row in grid)

def grid_size(points):
    minx = min(p.x for p in points)
    miny = min(p.y for p in points)
    maxx = max(p.x for p in points)
    maxy = max(p.y for p in points)
    return (maxx - minx) * (maxy - miny)
def part1(input):
    regex = 'position=<(.*)> velocity=<(.*)>'
    points = []
    for line in input.split('\n'):
        pos, vel = re.match(regex, line).groups()
        x, y = [int(n) for n in pos.split(',')]
        dx, dy = [int(n) for n in vel.split(',')]
        points.append(Point(x, y, dx, dy))
    min_size = 9999999999
    min_size_second = 0
    for i in range(10639):
        print('second', i, '-- size:', grid_size(points))
        for p in points:
            p.move()
    print(grid(points))

def part2(input):
    pass

###

input = '''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>'''

with open('input.txt') as f:
    input = f.read()

start_time = time.time()

print('\nPart 1')
part1(input)

print('\nPart 2')
print(part2(data))

print(f'\n >> Completed in { time.time() - start_time } seconds.')
