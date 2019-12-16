import time

###

def ingest(filename):
    input = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            x, y = line.split(', ')
            input.append((int(x), int(y)))
    return input

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def dist(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)

def closests(points):
    minx = min([p.x for p in points])
    miny = min([p.y for p in points])
    maxx = max([p.x for p in points])
    maxy = max([p.y for p in points])
    grid = {}
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            location = Point(x,y)
            distances = sorted([(p.dist(location),i) for i, p in enumerate(points)])
            print(location, ':', distances)
            if distances[0][0] == distances[1][0]:
                grid[(x,y)] = None
            else:
                grid[(x,y)] = distances[0][1]
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if grid[(x,y)] is not None:
                print(grid[(x,y)], end='')
            else:
                print(' ', end='')
        print()
    return grid

def part1(coords):
    points = [Point(*coord) for coord in coords]
    print(points)
    grid = closests(points)
    areas = {}
    for coord in grid:
        point_number = grid[coord]
        if point_number in areas:
            areas[point_number] += 1
        else:
            areas[point_number] = 1
    areas = sorted(areas.items(), key=lambda kv: kv[1])
    print(areas[-1])

def part2(coords):
    points = [Point(*coord) for coord in coords]
    minx = min([p.x for p in points])
    miny = min([p.y for p in points])
    maxx = max([p.x for p in points])
    maxy = max([p.y for p in points])
    grid = {}
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            location = Point(x,y)
            val = sum([location.dist(point) for point in points])
            grid[(x,y)] = val

    area = 0
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if grid[(x,y)] < 10000:
                print(f'{grid[(x,y)]}\t', end='')
                area += 1
            else:
                print(' \t', end='')
        print()
    print(area)


###

input = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
input = ingest('input.txt')

start_time = time.time()

print('\nPart 1')
# part1(input)

print('\nPart 2')
part2(input)

print(f'\n >> Completed in { time.time() - start_time } seconds.')
