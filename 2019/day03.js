const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day03.txt', 'utf8')

const positionSet = instructions => {
    let positions = [[0, 0]]
    instructions.split(',').map(instruction => {
        const dir = instruction[0]
        const step = parseInt(instruction.slice(1, instruction.length))
        let lastPosition = positions[positions.length - 1]
        switch (dir) {
            case 'U':
                for (let y = 1; y <= step; y++) {
                    positions.push([lastPosition[0], lastPosition[1] + y])
                }
                break
            case 'D':
                for (let y = 1; y <= step; y++) {
                    positions.push([lastPosition[0], lastPosition[1] - y])
                }
                break
            case 'L':
                for (let x = 1; x <= step; x++) {
                    positions.push([lastPosition[0] - x, lastPosition[1]])
                }
                break
            case 'R':
                for (let x = 1; x <= step; x++) {
                    positions.push([lastPosition[0] + x, lastPosition[1]])
                }
                break
            default:
                break
        }
    })
    return positions.map(pos => pos.toString())
}

const findIntersections = (w1, w2) => {
    const intersection = w1.filter(pos => w2.includes(pos) && pos !== '0,0')
    return intersection
}

const distance = pos => {
    const [x, y] = pos.split(',').map(x => Math.abs(parseInt(x)))
    return x + y
}

const minDistance = positions => {
    const positionReducer = (minDist, pos) => {
        if (distance(pos) < minDist) {
            return distance(pos)
        } else {
            return minDist
        }
    }
    return positions.reduce(positionReducer, Infinity)
}

const findClosestIntersectionPoint = (w1, w2) => {
    console.log('calculating first positions...')
    const w1positions = positionSet(w1)
    console.log('calculating second positions...')
    const w2positions = positionSet(w2)
    console.log('calculating intersection points...')
    const intersectionPoints = w1positions.filter(pos => w2positions.includes(pos) && pos !== '0,0')
    console.log('finding closest intersection point...')
    return minDistance(intersectionPoints)
}

const findFirstIntersectionPoint = (w1, w2) => {
    console.log('calculating first positions...')
    const w1positions = positionSet(w1)
    console.log('calculating second positions...')
    const w2positions = positionSet(w2)
    console.log('calculating intersection points...')
    const intersectionPoints = w1positions.filter(pos => w2positions.indexOf(pos) > -1 && pos !== '0,0')
    console.log('finding first intersection point...')
    const pointsAndStepCounts = []
    intersectionPoints.forEach(pt => {
        pointsAndStepCounts.push({ point: pt, stepCount: w1positions.indexOf(pt) + w2positions.indexOf(pt) })
    })
    console.log('sorting intersection points...')
    pointsAndStepCounts.sort((x, y) => x.stepCount - y.stepCount)
    return pointsAndStepCounts[0]
}

// tests

assert(true === true)
assert(findClosestIntersectionPoint('R8,U5,L5,D3', 'U7,R6,D4,L4') === 6)
assert(findClosestIntersectionPoint('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') === 159)
assert(findClosestIntersectionPoint('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') === 135)

// solution

console.log('--- Day 3: Crossed Wires ---')

const [a, b] = input.split('\n')
console.log(a)
console.log(b)

// part 1

console.log('Part 1:', findClosestIntersectionPoint(a, b))

// part 2

console.log('Part 2:', findFirstIntersectionPoint(a, b))