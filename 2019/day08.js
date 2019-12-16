const assert = require('assert')
const fs = require('fs')
const input = fs.readFileSync('day08.txt', 'utf8')

const imageCodeToLayers = (w, h, code) => {
    let layers = {}
    let layerCount = 0
    for (let i = 0; i < code.length; i += w) {
        if (i % (w * h) === 0) {
            layerCount += 1
        }
        if (layers.hasOwnProperty(layerCount)) {
            layers[layerCount].push(code.slice(i, i + w))
        } else {
            layers[layerCount] = [code.slice(i, i + w)]
        }
    }
    return layers
}

const countInstancesInArray = (arr, value) => arr.filter(x => x == value).length
const countInstancesInString = (str, value) => countInstancesInArray(str.split(''), value)
const countInstancesInLayer = (layer, value) => {
    return layer.reduce((total, row) => { return total + countInstancesInString(row, value)}, 0)
}

const findLayerWithFewestZeros = imageLayers => {
    // Object.keys(imageLayers).forEach(key => {
    //     imageLayers[key].forEach(layer => {
    //         console.log(key, layer)
    //     })
    // })
    let layerWithFewestZeros = -1
    let leastNumberOfZeros = Infinity
    Object.entries(imageLayers).forEach(([key, layer]) => {
        const zeroCount = countInstancesInLayer(layer, 0)
        if (zeroCount < leastNumberOfZeros) {
            leastNumberOfZeros = zeroCount
            layerWithFewestZeros = key
        }
    })
    return imageLayers[layerWithFewestZeros]
}

const decodeImage = (w, h, image) => {
    let newImageCode = [...Array(w * h).keys()].map(i => '2')
    for (let i = 0; i < image.length; i++) {
        const layerNumber = Math.floor(i / (w * h))
        const position = i % (w * h)
        if (newImageCode[position] === '2') {
            newImageCode[position] = image[i]
        }
    }
    return newImageCode
}

const printImage = (w, h, imageCode) => {
    // console.log('input', imageCode)
    for (let y = 0; y < h; y++) {
        console.log(imageCode.slice(w * y, w * y + w).map(val => val === '1' ? ' ' : val).join(''))
    }
}

// tests

assert(true === true)
assert(countInstancesInArray([1, 3, 5, 7, 5, 3, 1], 4) === 0)
assert(countInstancesInArray([1, 3, 5, 7, 5, 3, 1], 3) === 2)
assert(countInstancesInString('987234987234987234987456', 4) === 4)
assert(countInstancesInLayer(['123','345'], 3) === 2)
assert.deepEqual(decodeImage(2, 2, '0222112222120000'), ['0', '1', '1', '0'])

// solution

console.log('--- Day 8: Space Image Format ---')

// part 1

console.log('Part 1:')

const layers = imageCodeToLayers(25, 6, input)
const fewestZerosLayer = findLayerWithFewestZeros(layers)
console.log(`#1: ${ countInstancesInLayer(fewestZerosLayer, 1) }`)
console.log(`#2: ${ countInstancesInLayer(fewestZerosLayer, 2) }`)
console.log(`#1 * #2: ${ countInstancesInLayer(fewestZerosLayer, 1) * countInstancesInLayer(fewestZerosLayer, 2) }`)

// console.log(part1)

// part 2

console.log('Part 2:')

const decodedImage = decodeImage(25, 6, input)
printImage(25, 6, decodedImage)

// const decodedImage = decodeImage(2, 2, '0222112222120000')
// printImage(2, 2, decodedImage)