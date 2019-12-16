import time
from functools import reduce
from operator import mul

###

def part1():
    counts = { 2: 0, 3: 0 }
    with open('input.txt') as f:
        codes = [code.strip() for code in f.readlines()]
        for code in codes:
            bucket = {}
            for letter in code:
                if letter in bucket:
                    bucket[letter] += 1
                else:
                    bucket[letter] = 1
            if 2 in bucket.values():
                counts[2] += 1
            if 3 in bucket.values():
                counts[3] += 1
    print(counts)
    reduce(mul, counts.values(), 1)
    print(reduce(mul, list(counts.values()), 1))


def part2():
    with open('input.txt') as f:
        codes = [code.strip() for code in f.readlines()]
        for i in range(len(codes) - 1):
            for j in range(i + 1, len(codes)):
                diff = [num for num in range(len(codes[i])) if codes[i][num] != codes[j][num]]
                if len(diff) == 1:
                    slice_point = diff[0]
                    print(codes[i][:slice_point] + codes[i][slice_point+1:])

###

start_time = time.time()
part1()
print(f' >> Completed in { time.time() - start_time } seconds.')

start_time = time.time()
part2()
print(f' >> Completed in { time.time() - start_time } seconds.')
