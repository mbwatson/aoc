import time
import re

def decode_claim(claim):
    claim_regex = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    matches = re.search(claim_regex, claim)
    claim_no = int(matches[1])
    x = int(matches[2])
    y = int(matches[3])
    w = int(matches[4])
    h = int(matches[5])
    return({ 'num': claim_no, 'x': x, 'y': y, 'w': w, 'h': h })

def main():
    counted_units = {}
    with open('input.txt') as f:
        input = [line.strip() for line  in f.readlines()]
        claims = list(map(decode_claim, input))
    non_overlaps = {claim['num'] for claim in claims}
    for claim in claims:
        for i in range(claim['x'], claim['x'] + claim['w']):
            for j in range(claim['y'], claim['y'] + claim['h']):
                if (i,j) in counted_units:
                    counted_units[(i,j)].add(claim['num'])
                    for claim_number in counted_units[(i,j)]:
                        non_overlaps.remove(claim_number) if claim_number in non_overlaps else ''
                else:
                    counted_units[(i,j)] = { claim['num'] }
    multiply_counted_units = [ unit for unit in counted_units if len(counted_units[unit]) > 1 ]
    print(f'{ len(multiply_counted_units) } units overlapped more than once.')
    print('Non-overlapping claim numbers:', non_overlaps)

###


start_time = time.time()

main()

print(f'\n >> Completed in { time.time() - start_time } seconds.')
