import time
import re
from datetime import datetime
# dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

test_input = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up',
]

def ingest(filename):
    with open(filename) as f:
        input = [line for line in f.readlines()]
    return(input)

def sum_lengths(intervals):
    total = 0
    for interval in intervals:
        total += interval[1] - interval[0]
    return total

assert sum_lengths([(-1, 3), (4, 4), (8, 9)]) == 5

def make_records(input):
    input = sorted(input)
    record_regex = '^\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2})\:(\d{2})\] ([\w\W]+)$'
    action_regex = '(Guard #)(\d+) (.+)$'
    records = []
    guard = 0
    for record in input:
        matches = re.match(record_regex, record)
        year, month, day, hour, minute, action = matches.groups()
        if '#' in action:
            matches = re.match(action_regex, action)
            _, guard, action = matches.groups()
        records.append({ 'guard': int(guard), 'minute': int(minute), 'action': action })
    return records

def make_naps(records):
    nap_records = [record for record in records if record['action'] != 'begins shift']
    # Find sleepiest guard
    naps = {}
    for i in range(0, len(nap_records), 2):
        nap_interval = (nap_records[i]['minute'], nap_records[i+1]['minute'])
        if nap_records[i]['guard'] in naps:
            naps[nap_records[i]['guard']].append(nap_interval)
        else:
            naps[nap_records[i]['guard']] = [nap_interval]
    return naps

def part1(input):
    records = make_records(input)
    naps = make_naps(records)
    max_sleep_time = max([sum_lengths(naps[guard]) for guard in naps])
    sleepiest_guard = -1
    for guard_id, nap_intervals in naps.items():
        if sum_lengths(nap_intervals) == max_sleep_time:
            sleepiest_guard = guard_id
    # Find minute most slept during by sleepiest guard
    minutes = {}
    for nap_intervals in naps[sleepiest_guard]:
        for i in range(nap_intervals[0], nap_intervals[1]):
            if i in minutes:
                minutes[i] += 1
            else:
                minutes[i] = 1
    sleepiest_minute = max(minutes.items(), key=lambda k: k[1])[0]
    print(f'Sleepiest guard #{ sleepiest_guard } slept most during minute { sleepiest_minute }.')
    print(f'sleepiest_guard * sleepiest_minute = { sleepiest_guard * sleepiest_minute }.')

def most_slept_minute(naps):
    guard_id = 0
    minutes = {}
    for guard_id in naps.keys():
        for interval in naps[guard_id]:
            for i in range(interval[0], interval[1]):
                if (guard_id, i) in minutes:
                    minutes[(guard_id, i)] += 1
                else:
                    minutes[(guard_id, i)] = 1
    print(minutes)
    return max(minutes.items(), key=lambda k: k[1])[0]

def part2(input):
    records = make_records(input)
    naps = make_naps(records)
    guard_id, minute = most_slept_minute(naps)
    print(guard_id * minute)

###

start_time = time.time()

input = ingest('input.txt')
# input = test_input
print('Part 1')
part1(input)
print('Part 2')
part2(input)

print(f'\n >> Completed in { time.time() - start_time } seconds.')
