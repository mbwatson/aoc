import time
import re

###

def ingest(input):
    input = input.strip().split('\n')
    return input

def find_prerequisites(rules):
    steps = { step for pair in rules for step in pair }
    befores = { step: set() for step in steps}
    for a, b in rules:
        befores[b].add(a)
    return befores

def read_rules(input):
    line_regex = '^Step (\w) must be finished before step (\w) can begin.$'
    rules = []
    for line in input:
        pair = re.match(line_regex, line).groups()
        rules.append((pair[0], pair[1]))
    return rules

def find_order(rules):
    order = []
    done = False
    while not done:
        candidates = {pre for pre in rules if len(rules[pre]) == 0 and pre not in order}
        if len(candidates) > 0:
            next = min(candidates)
            candidates.remove(next)
            order.append(next)
            for pre in rules:
                preuire_cleanup = [pre for pre in rules if next in rules[pre]]
                for rule in preuire_cleanup:
                    rules[rule].remove(next)
        else:
            done = True
    return ''.join(order)

def part1(input):
    lines = read_rules(input)
    rules = find_prerequisites(lines)
    return find_order(rules)

def cost(char):
    if char is not None:
        # return ord(char) - 64
        return ord(char) - 4
    else:
        return 0

class Worker:
    def __init__(self, name, job, time):
        self.id = name
        self.job = job
        self.time = time

    def __repr__(self):
        return f'< Worker {self.id}: job={self.job}, time={self.time} >'

    def busy(self):
        return self.job is not None

    def assign(self, job):
        self.job = job
        self.time = cost(job)
        return True

    def work(self):
        self.time -= 1
        return True

def anyone_working(workers):
    workers = [worker for worker in workers if worker.busy()]
    return len(workers) > 0

def find_time(prereqs, num_workers):
    time = 0
    workers = [Worker(i+1, None, 0) for i in range(num_workers)]
    while prereqs or anyone_working(workers):
        print('Time:', time, '= ' * 20)
        available_workers = [worker for worker in workers if worker.busy() == False]
        candidates = [job for job, reqs in prereqs.items() if not reqs]
        print('Available workers:', available_workers)
        print('Job candidates:', candidates)
        while available_workers and candidates:
            next_worker = available_workers.pop()
            next_job = min(candidates)
            next_worker.assign(next_job)
            candidates.remove(next_job)
            prereqs.pop(next_job)
        for worker in workers:
            if worker.busy():
                print(' Working:', worker)
                worker.work()
                if worker.time == 0:
                    for job in prereqs:
                        if worker.job in prereqs[job]:
                            prereqs[job].remove(worker.job)
                    worker.assign(None)
            else:
                print('    Free:', worker)
        time += 1
    return time
    
def part2(input):
    lines = read_rules(input)
    prereqs = find_prerequisites(lines)
    time = find_time(prereqs, 5)
    print(time)

###

input = ''
with open('input.txt') as f:
    input = f.read()

test_input = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""

input = ingest(input)
print(input)
start_time = time.time()

print('\nPart 1')
print(part1(input))

print('\nPart 2')
print(part2(input))

print(f'\n >> Completed in { time.time() - start_time } seconds.')
