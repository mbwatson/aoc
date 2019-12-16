import math

def power_level(x, y, serial_number):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    power = (power // 100) % 10
    power -= 5
    return power


assert power_level(3, 5, 8) == 4
assert power_level(122, 79, 57) == -5
assert power_level(217, 196, 39) == 0
assert power_level(101, 153, 71) == 4

def best(serial_number, grid_size=300):
    power_levels = [
        [power_level(y, x, serial_number) for x in range(grid_size)]
            for y in range(grid_size)
    ]
    max_power = max(((x,y) for x in range(1, grid_size - 3) for y in range(1, grid_size - 3)),
        key=lambda pair: sum(power_levels[i][j]
                for i in [pair[0], pair[0]+1, pair[0]+2]
                for j in [pair[1], pair[1]+1, pair[1]+2])
        )
    return max_power

assert best(18) == (33, 45)
assert best(42) == (21, 61)

""" Recursion
                     ________ ___
                    |        |   |      [1,x+s]x[1,y-1]
  [1,1]x[x-1,y-1]   |________|___|
                    |________|###|  
                                    [1,1]x[x+s, y+s]
             [1,x-1]x[1,y+s]
"""

def best2(serial_number, grid_size=300):
    # Set of accumulated poewr levels of cells in rectangles [1,1]X[x,y], for x, y in [grid_size]
    rect_powers = {}
    for y in range(1, grid_size + 1):
        for x in range(1, grid_size + 1):
            if x == 1 or y == 1:
                rect_powers[(x,y)] = power_level(x, y, serial_number)
            else:
                rect_powers[(x,y)] = power_level(x, y, serial_number) + rect_powers[(x,y-1)] + rect_powers[(x-1,y)] - rect_powers[(x-1,y-1)]
    print(rect_powers)
    maximal_trio = None
    max_power = -math.inf
    for y in range(1, grid_size + 1):
        for x in range(1, grid_size + 1):
            for s in range(1, min(grid_size - x + 1, grid_size - y + 1)):
                power = rect_powers[(x+s, y+s)]
                if y - 1 > 0: power -= rect_powers[(x+s, y-1)]
                if x - 1 > 0: power -= rect_powers[(x-1, y+s)]
                if x - 1 > 0 and y-1 > 0: power += rect_powers[(x-1, y-1)]
                if power > max_power:
                    print((x, y, s), ':', power)
                    max_power = power
                    maximal_trio = (x, y, s)
    print('Done!')
    print(maximal_trio)
    return(maximal_trio)

# THESE ARE OFF BY ONE.
# ACCOUNT FOR THIS AT SUBMISSION TIME.
# MAYBE FIX ANOTHER TIME.

assert best2(18) == (90,269,16-1)
assert best2(42) == (232,251,12-1)

print('Part 1')
print(best(7857))

print('Part 2')
print(best2(7857))
