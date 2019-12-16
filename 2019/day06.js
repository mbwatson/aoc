const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day06.txt', 'utf8')

// tests

assert(true === true)

// solution

console.log('--- Day 6: Universal Orbit Map ---')

// part 1

console.log('Part 1:')

const bodies = {}
const orbits = input.split('\n')
    .forEach(line => {
        const [center, satellite] = line.split(')')
        if (!bodies.hasOwnProperty(center)) {
            bodies[center] = []
        }
        bodies[center].push(satellite)
    })

const countOrbits = body => {
    let ancestorCount = 0
    if (bodies.hasOwnProperty(body)) {
        bodies[body].forEach(child => {
            ancestorCount += countOrbits(child) + 1
        })
    }
    return ancestorCount
}

let orbitCount = 0
Object.keys(bodies).forEach(satellite => {
    orbitCount += countOrbits(satellite)
})

console.log(orbitCount)

// part 2

console.log('Part 2:')

const pathToRoot = body => {
    const parent = Object.keys(bodies).find(key => bodies[key].includes(body))
    return parent === 'COM' ? [] : pathToRoot(parent).concat([parent])
}

const orbitalTransferPath = (a, b) => {
    const aToRoot = pathToRoot(a)
    const bToRoot = pathToRoot(b)
    // symmettric difference
    const path = aToRoot.filter(x => !bToRoot.includes(x))
        .concat(bToRoot.filter(y => !aToRoot.includes(y)))
    // note this returns one fewer node, but a tree (and thus path)
    // with n nodes has n-1 edges, which we are actually counting here anyway
    return path
}
const fromYouToSan = orbitalTransferPath('YOU', 'SAN')
console.log(fromYouToSan.length)
