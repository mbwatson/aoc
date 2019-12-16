import re
import math
from copy import copy

def alive(val):
    if val in state:
        return '#'
    return '.'

raw_input = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''

with open('input.txt') as f:
    raw_input = f.read()

#

input = [line.strip() for line in raw_input.strip().split('\n')]

init_state_regex = 'initial state: (.+)$'
init_state = { i for i, char in
                enumerate(re.match(init_state_regex, input[0]).groups()[0])
                if char == '#' }

note_regex = '([\.\#]{5}) => ([\.\#])'
raw_notes = input[2:]

mutations = {}

for raw_note in raw_notes:
    before, after = re.match(note_regex, raw_note).groups()
    mutations[before] = after

def show(states, minval, maxval):
    print((minval, maxval))
    for state in states:
        for i in range(minval, maxval + 1):
            if i in state:
                print('#', end='')
            else:
                print('.', end='')
        print()

print('Initial State:', init_state)
print('Mutations:')

generation_count = 111
states = []
states.append(init_state)
for i in range(generation_count):
    state = states[i]
    stage = set(copy(state))
    for i in range(min(state) - 2, max(state) + 3):
        group = ''.join(map(alive, (i-2, i-1, i, i+1, i+2)))
        # print(i, group, '=> ', end='')
        if group in mutations:
            # print(mutations[group])
            if mutations[group] == '#':
                stage.add(i)
            else:
                if i in stage:
                    stage.remove(i)
        else:
            # print(group[2])
            if i in state:
                stage.remove(i)
    states.append(sorted(stage))

minval = min(min(state) - 3 for state in states)
maxval = max(max(state) + 2 for state in states)
# show(states, minval, maxval)
print('Minimum value in state:', min(states[-1]))
print(len(states[-1]), 'plants in that final state.')
print('Sum = ', sum(states[-1]), 'after', generation_count, 'generations.')
print('After 50 000 000 000 generations... ', end='')
print(sum(states[-1]) + len(states[-1]) * (50000000000 - generation_count))
