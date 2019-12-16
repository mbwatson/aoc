import time

###

# N M N M  M  M  M N M N M M  M M M M 
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
# A -                           - - -
#     B - -  -  -  C -        -
#                      D - -  

def sum_metadata(data):
    children_count = data.pop(0)
    metadata_count = data.pop(0)
    sum = 0
    for i in range(children_count):
        sum += sum_metadata(data)
    for i in range(metadata_count):
        sum += data.pop(0)
    return sum

def part1(data):
    data = [int(x) for x in input.split()]
    print(sum_metadata(data))

#

def value_of_root(data):
    children_count = data.pop(0)
    metadata_count = data.pop(0)
    values = [value_of_root(data) for _ in range(children_count)]
    metadata = [data.pop(0) for _ in range(metadata_count)]
    if children_count == 0:
        return sum(metadata)
    return sum(values[i-1] for i in metadata if i-1 in range(children_count))

def part2(data):
    data = [int(x) for x in input.split()]
    sum = 0
    print(value_of_root(data))

###

test_input = '2  3  0  3 10 11 12  1  1  0  1 99  2  1  1  2'
#        A  -                                   -  -  -
#        |     B  -  -  -  -  C  -           -
#        |     |              |     D  -  -  
#        |     |              |     |
#        66    33             0     99

with open('input.txt') as f:
    input = f.read()

start_time = time.time()

print('\nPart 1')
part1(input)

print('\nPart 2')
part2(input)

print(f'\n >> Completed in { time.time() - start_time } seconds.')
