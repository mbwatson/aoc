const fs = require('fs')
const assert = require('assert')

const input = fs.readFileSync('input.txt', 'utf8')
const expenses = input.split('\n').map(n => +n)

//

console.log('--- Day 1: Report Repair ---')

const findPairProduct = (arr, sum) => {
  for (let i = 0; i < arr.length - 1; i += 1) {
    for (let j = i + 1; j < arr.length; j += 1) {
      if (arr[i] + arr[j] === sum) {
        return arr[i] * arr[j]
      }
    }
  }
  return null
}

const findTripleProduct = (arr, sum) => {
  for (let i = 0; i < arr.length - 1; i += 1) {
    const p = findPairProduct(arr.slice(i), sum - arr[i])
    if (p) return p * arr[i]
  }
  return null
}

// tests

assert(findPairProduct([1721, 979, 366, 299, 675, 1456], 2020) === 514579)
assert(findTripleProduct([1721, 979, 366, 299, 675, 1456], 2020) === 241861950)

// solution

// part 1

const part1 = findPairProduct(expenses, 2020)
console.log(part1)

// part 2

const part2 = findTripleProduct(expenses, 2020)
console.log(part2)

