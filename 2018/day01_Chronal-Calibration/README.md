# Day 01 Notes

## A Cool Approach

I had an outer loop to manage looping through the input values.
The itertools library takes care of this--namely [`itertools.cycle`](https://docs.python.org/2/library/itertools.html).


```python
>>> from itertools import cycle
>>> count = 0
>>> for item in cycle('XYZ'):
...     if count > 7:
...         break
...     print(item)
...     count += 1
... 
X
Y
Z
X
Y
Z
X
Y
```

This allows this code

```python
while not found_repeat:
    for step in sequence:
        total += step
        prev_size = len(frequencies)
        frequencies.add(total)
        if total in frequencies:
            found_repeat = True
            break
print(f'First repeated frequency is {total}.')
```

to be slimmed down a bit to this

```python
for step in cycle(sequence):
    total += step
    if total in frequencies:
        break
    prev_size = len(frequencies)
    frequencies.add(total)
print(f'First repeated frequency is {total}.')
```

Not severely slimmer, but one loop is better than two, and `itertools.cycle` is in the toolbelt.
