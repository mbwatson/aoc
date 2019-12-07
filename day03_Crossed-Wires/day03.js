const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('input.txt', 'utf8')

const vectorAddition = (v1, v2) => {
    if (v1.length !== v2.length) return
    const newVector = []
    for (let i = 0; i < v1.length; i++) {
        newVector.push(v1[i] + v2[i])
    }
    return newVector
}

const instructionVector = instruction => {
    const dir = instruction[0]
    const step = parseInt(instruction.slice(1, instruction.length))
    let vector = [0, 0]
    switch (dir) {
        case 'U':
            vector = [0, step]
            break
        case 'D':
            vector = [0, -step]
            break
        case 'L':
            vector = [-step, 0]
            break
        case 'R':
            vector = [step, 0]
            break
        default:
            break
    }
    return vector
}

const parseInstructions = instructionString => {
    return instructionString
        .split(',')
        .map(inst => instructionVector(inst))
}

const vertices = steps => {
    let positions = [steps[0]]
    for (let i = 0; i < steps.length - 1; i++) {
        const lastPosition = positions[positions.length - 1]
        positions.push(vectorAddition(lastPosition, steps[i + 1]))
    }
    return [[0, 0], ...positions]
}

const positions = instructionString => {
    let instructions = instructionString.split(',')
    let positionCoords = [[0, 0]]
    for (let i = 0; i < instructions.length - 1; i++) {
        const dir = instruction[0]
        const step = parseInt(instruction.slice(1, instruction.length))
        const lastPosition = positionCoords[positionCoords.length - 1]
        switch (dir) {
            case 'U':
                for (let y = lastPosition[1]; y < step; y++) {
                    positionCoords.push(vectorAddition(lastPosition, [0, y]))
                }
                break
            case 'D':
                for (let y = lastPosition[1]; y < step; y--) {
                    positionCoords.push(vectorAddition(lastPosition, [0, y]))
                }
                break
            case 'L':
                for (let x = lastPosition[0]; y < step; x--) {
                    positionCoords.push(vectorAddition(lastPosition, [-1, 0]))
                }
                break
            case 'R':
                for (let x = lastPosition[0]; y < step; x++) {
                    positionCoords.push(vectorAddition(lastPosition, [1, 0]))
                }
                break
            default:
                break
        }
        
    }
    return positionCoords    
}

// test

assert(true === true)
assert.deepEqual(vectorAddition([1, 2], [0, -3]), [1, -1])
assert.deepEqual(parseInstructions('R8,U5,L5,D3'), [[8, 0], [0, 5], [-5, 0], [0, -3]])
assert.deepEqual(parseInstructions('U7,R6,D4,L4'), [[0, 7], [6, 0], [0 ,-4], [-4, 0]])
assert.deepEqual(vertices(parseInstructions('R8,U5,L5,D3')), [[0, 0], [8, 0], [8, 5], [3, 5], [3, 2]])
assert.deepEqual(vertices(parseInstructions('U7,R6,D4,L4')), [[0, 0], [0, 7], [6, 7], [6, 3], [2, 3]])

console.log(positionCoords('U7,R6,D4,L4'))
// solution

console.log('--- Day 3: Crossed Wires ---')

const [wire1steps, wire2steps] = input.split('\n').map(string => parseInstructions(string))
// console.log('WIRE 1:', wire1steps)
// console.log('WIRE 2:', wire2steps)

// part 1


// part 2

