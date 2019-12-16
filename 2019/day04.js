const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day04.txt', 'utf8')

const validate = password => {
    const arr = password.toString().split('').map(x => +x)
    let i = 0
    let previousValue = -Infinity
    let foundDescent = false
    let foundDouble = false
    while (i < arr.length && !foundDescent) {
        if (arr[i] < previousValue) return false
        if (!foundDouble && arr[i] === previousValue) foundDouble = true
        previousValue = arr[i]
        i += 1
    }
    return foundDouble
}

const strictValidate = password => {
    const arr = password.toString().split('').map(x => +x)
    let i = 0
    let previousValue = -Infinity
    let foundDescent = false
    let repeats = {}
    while (i < arr.length && !foundDescent) {
        if (repeats.hasOwnProperty(arr[i])) {
            repeats[arr[i]] += 1
        } else {
            repeats[arr[i]] = 1
        }
        if (arr[i] < previousValue) return false
        previousValue = arr[i]
        i += 1
    }
    return Object.values(repeats).includes(2)
}

// tests

assert(true === true)
assert(validate(111123) === true)
assert(validate(122345) === true)
assert(validate(135679) === false)
assert(validate(111111) === true)
assert(validate(223450) === false)
assert(validate(123789) === false)

assert(strictValidate(112233) === true)
assert(strictValidate(123444) === false)
assert(strictValidate(111122) === true)

// solution

console.log('--- Day 4: Secure Container ---')
const [start, end] = input.split('-')

// part 1

console.log('Part 1:')

const validPasswords = []

for (let i = start; i <= end; i++) {
    if (validate(i)) {
        validPasswords.push(i)
    }
}
console.log(validPasswords)
console.log(validPasswords.length)

// part 2

console.log('Part 2:')

const veryValidPasswords = []

for (let i = start; i <= end; i++) {
    if (strictValidate(i)) {
        veryValidPasswords.push(i)
    }
}
console.log(veryValidPasswords)
console.log(veryValidPasswords.length)

