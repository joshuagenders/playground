const rectangles = require('./rectangles')

const point = (x, y) => ({x, y})

test.each([
    [1, 4, [point(0,0), point(0,1), point(1,1), point(1,0)]],
    [1, 5, [point(0,0), point(0,1), point(1,0), point(0,2), point(1,2)]],
    [1, 9, [point(0,0), point(0,1), point(1,1), point(1,0), point(1,0), point(1,0), point(1,0), point(1,0), point(1,0)]],
    [3, 6, [point(0,0), point(0,1), point(1,1), point(1,0), point(0,2), point(1,2)]],
    [6, 8, [point(0,0), point(0,1), point(1,1), point(1,0), point(0,2), point(0,3), point(1,2), point(1,3)]],
    [0, 4, [point(1,0), point(1,1), point(0,1), point(0,2)]],
    [0, 4, [point(0,0), point(0,3), point(1,1), point(1,0)]],
    [0, 0, []],
    [0, 0, null],
    [0, 0, undefined]
])('rectangle counts are correct. %s rectangle(s), %s points', (rectangleCount, pointCount,  points) => {
    expect(rectangles.countRectangles(points)).toBe(rectangleCount)
})