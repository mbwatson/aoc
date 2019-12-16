import time
import re

###

def ingest(filename):
    input = []
    with open(filename) as f:
        return(f.read())

def trigger(polymer, counts):
    remove = set().union(*counts)
    print('remove', remove)
    return [polymer[i] for i in range(len(polymer)) if i not in remove]

def same_letters(x, y):
    return abs(ord(x) - ord(y)) == 32

def reduce(polymer):
    length = len(polymer)
    if len(polymer) == 2 and same_letters(polymer[0], polymer[1]):
        return ''
    for i in range(len(polymer) - 1):
        n = length - i - 2
        if n < len(polymer) - 2:
            if same_letters(polymer[n], polymer[n + 1]):
                polymer = polymer[:n] + polymer[n + 2:]
    return polymer

def get_units(polymer):
    return set([letter.lower() for letter in list(polymer)])

assert get_units('dabAcCaCBAcCcaDA') == {'a', 'b', 'c', 'd'}

def part1(polymer):
    reducing = True
    while reducing:
        print(polymer)
        reduced_polymer = reduce(polymer)
        if reduced_polymer == polymer:
            reducing = False
        polymer = reduced_polymer
    return(len(polymer))

assert part1('dabAcCaCBAcCcaDA') == 10
assert part1('aA') == 0
assert part1('abBA') == 0
assert part1('abAB') == 4
assert part1('aabAAB') == 6

def collapse(polymer, unit):
    upper_unit = unit.upper()
    return ''.join([letter for letter in polymer if letter != unit and letter != upper_unit])

def part2(polymer):
    units = get_units(polymer)
    tests = {}
    for unit in units:
        collapsed_polymer = collapse(polymer, unit)
        tests[unit] = reduce(collapsed_polymer)
    min_polymer = min(tests.items(), key=lambda k: len(k[1]))
    return len(min_polymer[1])

assert part2('dabAcCaCBAcCcaDA') == 4

###

input = 'dabAcCaCBAcCcaDA'
input = ingest('input.txt')

start_time = time.time()

print('\nPart 1')
print(f'Polymer reduces to size { part1(input) }.')

print('\nPart 2')
print(f'Shorter polymer has length { part2(input) }.')

print(f'\n >> Completed in { time.time() - start_time } seconds.')
