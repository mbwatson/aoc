const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day07.txt', 'utf8')
const run = require('./day05')

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

const arr = [...Array(3).keys()]
const arrPerms = permutations(arr)
console.log('- array:', arr)
console.log(`- permutations ${ arrPerms.length }:`, arrPerms)
// tests

assert(true === true)
assert.deepEqual(permutations([0,1,2]).map(p => p.toString()), [ '0,1,2', '0,2,1', '1,0,2', '1,2,0', '2,0,1', '2,1,0' ])
assert(permutations([0,1,2,3,4]).length === 120)

// solution

console.log('--- Day 7: Amplification Circuit ---')

// part 1

console.log('Part 1:')

// part 2

console.log('Part 2:')
