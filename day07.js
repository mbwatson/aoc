const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day07.txt', 'utf8')
const runProgram = require('./day05')

const permutations = arr => {
    if (arr.length === 1) {
        return arr
    }
    const perms = []
    let index = 0
    while (index < arr.length) {
        const reducedArr = arr.slice(0, index).concat(arr.slice(index + 1))
        const reducedArrPerms = permutations(reducedArr)
        reducedArrPerms.map(perm => [arr[index]].concat(perm)).forEach(perm => {
            perms.push(perm)
        })
        index += 1
    }
    return perms
}

const runAmplifiers = (program, inputSignal, phases) => {
    let output = inputSignal
    phases.forEach(phase => {
        output = runProgram(program, [phase, output])[0]
    })
    return output
}

const maxOutput = (program, inputSignal) => {
    const perms = permutations([...Array(5).keys()])
    let max = -Infinity
    perms.forEach(perm => {
        const output = runAmplifiers(program, inputSignal, perm)
        console.log(perm, output)
        if (output > max) {
            max = output
        }
    })
    return max
}

// tests

assert(true === true)
assert.deepEqual(permutations([0,1,2]).map(p => p.toString()), [ '0,1,2', '0,2,1', '1,0,2', '1,2,0', '2,0,1', '2,1,0' ])
assert(permutations([0,1,2,3,4]).length === 120)
assert(maxOutput('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', 0) === 43210)
assert(maxOutput('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', 0) === 54321)
assert(maxOutput('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', 0) === 65210)

// solution

console.log('--- Day 7: Amplification Circuit ---')

// part 1

console.log('Part 1:')

const part1 = maxOutput(input, 0)
console.log(part1)

// part 2

console.log('Part 2:')
