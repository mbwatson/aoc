import time
import re
import numpy

with open('input.txt') as f:
    input = []
    for r in f.readlines():
        r = re.split('[^0-9]+', r[1:].strip())
        input.append([int(d) for d in r])

grid = numpy.zeros((1000, 1000))

def part1():
    for n, x, y, dx, dy in input:
        grid[x:x+dx, y:y+dy] += 1
    return numpy.sum(grid > 1)

def part2():
    for n, x, y, dx, dy in input:
        if numpy.all(grid[x:x+dx, y:y+dy] == 1):
            return n

###

start_time = time.time()

print(part1())
print(part2())

print(f'\n >> Completed in { time.time() - start_time } seconds.')