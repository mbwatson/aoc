def digit_split(val):
    return list(map(int, str(val)))

def part1(init_recipes, elf_count=2, init_recipe_count=9):
    # print(f'init_recipes={init_recipes}, {elf_count} elves, after {init_recipe_count} recipes', end=' -> ')
    
    elves = [i for i in range(elf_count)]
    scoreboard = init_recipes

    while True:
        # print('= ' * 10)
        # for i, pos in enumerate(elves):
            # print(f' - Elf {i}:', pos)
        prod = sum(scoreboard[elf] for elf in elves)
        new_recipes = digit_split(prod)
        
        # print('New recipes:', new_recipes)
        scoreboard += new_recipes
        # print('Scoreboard:', scoreboard)
        
        # print(len(scoreboard))
        for i, pos in enumerate(elves):
            elves[i] += (1 + scoreboard[elves[i]])
            elves[i] %= len(scoreboard)
            # print(f' - elf {i}: {pos} > {elves[i]}')

        if len(scoreboard) > init_recipe_count + 10:
            score_string = ''.join(list(map(str, scoreboard[init_recipe_count:init_recipe_count + 10])))
            # print(score_string)
            return score_string

def part2(init_recipes, elf_count, sequence):
    # print(f'init_recipes={init_recipes}, {elf_count} elves, after {init_recipe_count} recipes', end=' -> ')
    sequence = [int(c) for c in sequence]
    elves = [i for i in range(elf_count)]
    scoreboard = init_recipes
    count = 0
    while True:
        # print('= ' * 10)
        # for i, pos in enumerate(elves):
            # print(f' - Elf {i}:', pos)
        prod = sum(scoreboard[elf] for elf in elves)
        new_recipes = digit_split(prod)
        
        # print('Scoreboard:', scoreboard)
        # print('New recipes:', new_recipes)
        # print('Sequence:', sequence)
        for i, score in enumerate(new_recipes):
            scoreboard.append(score)
            tail = scoreboard[-len(sequence):]
            # print('    Tail:', tail)
            # print('new rec #', i)
            if tail == sequence:
                position = len(scoreboard) - len(sequence)
                # print('position', position)
                return position
        for i, pos in enumerate(elves):
            elves[i] += (1 + scoreboard[elves[i]])
            elves[i] %= len(scoreboard)

        if count % 1000000 == 0:
            print(count, len(scoreboard))
            if count == 50000000:
                break
        count += 1

#

assert part1([3, 7], 2, 5) == '0124515891'
assert part1([3, 7], 2, 9) == '5158916779'
assert part1([3, 7], 2, 18) == '9251071085'
assert part1([3, 7], 2, 2018) == '5941429882'

#

init_recipes = [3, 7]

print('Part 1')
scores = part1(init_recipes, 2, 505961)
print(scores)

#

assert part2([3, 7], 2, '01245') == 5
assert part2([3, 7], 2, '51589') == 9
assert part2([3, 7], 2, '92510') == 18
assert part2([3, 7], 2, '59414') == 2018

#

search_sequence = '505961'

print('Part 2')
index = part2([3,7], 2, search_sequence)
print(index)
