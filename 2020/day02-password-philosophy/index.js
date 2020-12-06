const fs = require('fs')
const assert = require('assert')

/*-------------------------------------*/

String.prototype.validate = function(letter, min, max) {
  // count occurrendces of letter in word
  const pattern = new RegExp(letter, 'g')
  const matches = this.match(pattern) || []
  // return if count is valid
  return min <= matches.length && matches.length <= max
}

const findValidPasswords = list => {
  const passwords = []

  const lines = list.split('\n')
  for (let line of lines) {
    // split line into min, max, letter, & password
    const validationDetails = line.match(/^(\d+)-(\d+) (\w): (\w+)$/) || []
    // validate word, push to pw array if so
    const [, min, max, letter, word] = validationDetails
    if (word.validate(letter, +min, +max)) {
      passwords.push(word)
    }
  }
  return passwords
}

// just count response from findValidPasswords function
const countValidPasswords = list => findValidPasswords(list).length

//

String.prototype.validate2 = function(letter, positions) {
  // look at only given positions
  let substring = ''
  for (let position of positions) {
    substring += this[position - 1]
  }
  // count occurrences in those positions
  const matches = substring.match(new RegExp(letter, 'g')) || []
  // exactly one match is valid
  return matches.length === 1
}

const findValidPasswords2 = list => {
  const passwords = []

  const lines = list.split('\n')
  for (let line of lines) {
    // split line into min, max, letter, & password
    const pattern = new RegExp(/^(\d+)-(\d+) (\w): (\w+)$/)
    const validationDetails = line.match(pattern) || []
    // validate word, push to pw array if so
    const [, min, max, letter, word] = validationDetails
    if (word.validate2(letter, [+min, +max])) {
      passwords.push(word)
    }
  }
  return passwords
}

// just count response from findValidPasswords function
const countValidPasswords2 = list => findValidPasswords2(list).length

/*----------  TESTS  ----------*/

const testInput = `1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc`

assert('abcde'.validate('a', 1, 3) === true)
assert('cdefg'.validate('b', 1, 3) === false)
assert('ccccccccc'.validate('c', 2, 9) === true)

assert(countValidPasswords(testInput) === 2)

assert('abcde'.validate2('a', [1, 3]) === true)
assert('cdefg'.validate2('b', [1, 3]) === false)
assert('ccccccccc'.validate2('c', [2, 9]) === false)

assert(countValidPasswords2(testInput) === 1)

/*----------  SOLUTIONS  ----------*/

console.log('--- Day 2: Password Philosophy ---')

const list = fs.readFileSync('input.txt', 'utf8')

// part 1

let part1 = countValidPasswords(list)
console.log(`Part 1: ${ part1 }`)


// part 2

let part2 = countValidPasswords2(list)
console.log(`Part 2: ${ part2 }`)


