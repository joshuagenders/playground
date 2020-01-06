const range = (starting, finishing) => [...Array(finishing - starting).keys()]
    .map(x => parseInt(x, 10))
    .map(x => x + starting)

const unique = comparer => list => list.reduce((acc, val) => 
    !acc.some(v => comparer(v, val)) 
        ? [ ...acc, val ]
        : acc, [])

const pointsAreEqual = (p1, p2) => p1.x === p2.x && p1.y === p2.y

const uniquePoints = unique(pointsAreEqual)

function* traverseArray (inputArr, starting, finishing, levels) {
    if (!inputArr.length) return []
    if (levels > 1){
        for (const x of range(starting, finishing - (levels - 1))){
            for (next of traverseArray(inputArr, x + 1, finishing, levels - 1)){
                yield [inputArr[x], ...next]
            }
        }
    } else {
        for (const current of range(starting + levels - 1, finishing)){
            yield [inputArr[current]]
        }
    }
}

const uniquePermutationsOfLength = (inputArr, length) => {
    if (!inputArr || !inputArr.length) return []
    const p = uniquePoints(inputArr)
    return Array.from(traverseArray(p, 0, p.length, length))
}

const sameX = (p1, p2) => p1.x === p2.x
const sameY = (p1, p2) => p1.y === p2.y

const removeItem = (arr, item) => arr.filter(i => i !== item)

const isRectangle = (points) => {
    const startPoint = points[0]
    var remaining = points.slice(1)
    const matchingX = remaining.find(p => sameX(p, startPoint))
    if (!matchingX) return false
    remaining = removeItem(remaining, matchingX)
    const matchingY = remaining.find(p => sameY(p, matchingX))
    if (!matchingY) return false
    const lastPoint = removeItem(remaining, matchingY)[0]
    return sameY(lastPoint, startPoint) && sameX(lastPoint, matchingY)
}

const countRectangles = points => uniquePermutationsOfLength(points, 4)
    .filter(isRectangle)
    .reduce((acc, val) => val[1] ? acc + 1 : acc, 0)

module.exports.countRectangles = countRectangles