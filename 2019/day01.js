const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day01.txt', 'utf8').split('\n')

const fuel = mass => Math.max(Math.floor(mass / 3) - 2, 0)

const fuelFromMassReducer = (total, mass) => {
    return total + fuel(mass)
}

const findTotalFuel = masses => {
    return masses.reduce(fuelFromMassReducer, 0)
}

const totalFuel = mass => {
    const thisFuel = fuel(mass)
    return thisFuel > 0 ? thisFuel + totalFuel(thisFuel) : 0
}

// tests

assert(true === true)
assert(findTotalFuel([12, 14]) === 2 + 2)
assert(totalFuel(1969) === 966)
assert(totalFuel(100756) === 50346)


// solution

console.log('--- Day 1: The Tyranny of the Rocket Equation ---')

// part 1

console.log(`Part 1: ${ findTotalFuel(input) }`)

// part 2

const fuelRequirements = input.reduce((total, mass) => total + totalFuel(mass), 0)
console.log(`Part 2: ${ fuelRequirements }`)
