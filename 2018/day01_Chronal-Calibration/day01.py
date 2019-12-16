import time
from itertools import cycle

def ingest(filename):
    with open(filename) as f:
        input = [int(val) for val in f.readlines()]
    return(input)

def part1(sequence):
    return sum(sequence)

def part2(sequence):
    frequencies = {0}
    total = 0
    for step in cycle(sequence):
        total += step
        if total in frequencies:
            break
        frequencies.add(total)
    return total

###

start_time = time.time()
input = ingest('input.txt')
print(f'The resulting frequency is { part1(input) }.')
print(f'First repeated frequency is { part2(input) }.')
print(f' >> Completed in { time.time() - start_time } seconds.')
