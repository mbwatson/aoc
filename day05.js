const assert = require('assert')
const fs = require('fs')
const inputFile = fs.readFileSync('day05.txt', 'utf8')

const parseInstruction = (intcode, position) => {
    const instruction = intcode[position].toString().padStart(5, '0')
    const opcode = +instruction.slice(-2)
    const params = intcode.slice(position + 1, position + paramCount(opcode) + 1)
    const modes = instruction.split('').reverse().slice(2, 2 + params.length).map(x => +x)
    return ({
        opcode: opcode,
        params: params,
        modes: modes,
    })
}

const run = (intcode, input) => {
    let position = 0
    let output = []
    const program = intcode.split(',').map(i => +i)
    // traverse program values until 99 is hit
    while (program[position] !== 99) {
        const instruction = program[position].toString().padStart(5, '0')
        const opcode = +instruction.slice(-2)
        const modes = instruction.split('').reverse().slice(2).map(x => +x)
        switch (opcode) {
            case 1:
                const a = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const b = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                program[program[position + 3]] = a + b
                position += 4
                break                
            case 2:
                const c = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const d = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                program[program[position + 3]] = c * d
                position += 4
                break
            case 3:
                program[program[position + 1]] = input
                position += 2
                break
            case 4:
                if (modes[0] === 0) {
                    output.push(program[program[position + 1]])
                } else {
                    output.push(program[position + 1])
                }
                position += 2
                break
            case 5:
                const e = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const f = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                position = (e !== 0) ? f : position + 3 
                break
            case 6:
                const g = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const h = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                position = (g === 0) ? h : position + 3
                break
            case 7:
                const i = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const j = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                program[program[position + 3]] = (i < j) ? 1 : 0
                position += 4
                break
            case 8:
                const k = modes[0] === 0 ? program[program[position + 1]] : program[position + 1]
                const l = modes[1] === 0 ? program[program[position + 2]] : program[position + 2]
                program[program[position + 3]] = (k === l) ? 1 : 0
                position += 4
                break
            default:
                break
        }
    }
    return output
}

// tests

assert(true === true)
assert.deepEqual(run('3,0,4,0,99', 1), [1])
assert.deepEqual(run('3,0,4,0,99', 100), [100])
assert.deepEqual(run('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0), [0])
assert.deepEqual(run('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0), [0])
assert.deepEqual(run('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 1), [1])
assert.deepEqual(run('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 1), [1])
assert.deepEqual(run('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 7), [999])

// solution

console.log('--- Day 5: Sunny with a Chance of Asteroids ---')

// part 1

console.log('Part 1:')

const part1 = run(inputFile, 1)
console.log(`Diagnostic code: ${ part1.slice(-1) }`)

// part 2

console.log('Part 2:')

const part2Output = run(inputFile, 5)
console.log(`Diagnostic code: ${ part2Output }`)

// export

module.exports = run