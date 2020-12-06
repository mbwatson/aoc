const fs = require('fs')
const assert = require('assert')

/*-------------------------------------*/

const countTrees = (map, rise, run) => {
  let treeCount = 0
  const TREE = '#'
  const lines = map.split('\n')
  const mapWidth = lines[0].length
  let column = 0, row = 0
  while (row < lines.length) {
    if (lines[row][column] === TREE) {
      treeCount += 1
    }
    row += rise
    column = (column + run) % mapWidth
  }
  return treeCount
}

/*----------  TESTS  ----------*/

const testInput = `..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#`

assert(countTrees(testInput, 1, 1) === 2)
assert(countTrees(testInput, 1, 3) === 7)
assert(countTrees(testInput, 1, 5) === 3)
assert(countTrees(testInput, 1, 7) === 4)
assert(countTrees(testInput, 2, 1) === 2)

/*----------  SOLUTIONS  ----------*/

console.log('--- Day 3: Toboggan Trajectory ---')

const map = fs.readFileSync('input.txt', 'utf8')

// part 1

let part1 = countTrees(map, 1, 3)
console.log(`Part 1: ${ part1 }`)

// part 2

const slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
let part2 = slopes.reduce((product, [rise, run]) => {
  return product * countTrees(map, rise, run)
}, 1)
console.log(`Part 2: ${ part2 }`)
