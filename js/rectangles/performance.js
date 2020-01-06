const Benchmark = require('benchmark')
const rectangles = require('./rectangles')

var suite = new Benchmark.Suite

const point = (x, y) => ({x, y})
const points = [point(0,0), point(0, 1), point(1,1), point(1,0), point(0,2), point(1,2)]

suite.add('test single point', function() {
  rectangles.countRectangles(points)
})
.on('cycle', function(event) {
  console.log(String(event.target))
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').map('name'))
})
.run({ 'async': true })
