const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day02.txt', 'utf8').split(',').map(i => +i)

const run = intcode => {
    for (let i = 0; i < intcode.length; i += 4) {
        switch(intcode[i]) {
            case 1:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
                break
            case 2:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
                break
            default:
                return intcode
        }
    }
    return intcode
}

const initialize = (arr, noun, verb) => [arr[0], noun, verb, ...arr.slice(3, arr.length)]

// tests

assert(true === true)
assert.deepEqual(run([1,9,10,3,2,3,11,0,99,30,40,50]), [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
assert.deepEqual(run([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
assert.deepEqual(run([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
assert.deepEqual(run([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
assert.deepEqual(run([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])

// solution

console.log('--- Day 2: 1202 Program Alarm ---')

// part 1

const program = [input[0], 12, 2, ...input.slice(3, input.length)]

console.log(run(program)[0])

// part2

for (let n = 0; n < 100; n++) {
    for (let v = 0; v < 100; v++) {
        const program = initialize(input, n, v)
        if (run(program)[0] === 19690720) {
            console.log(100*n + v)
        }
    }
}
