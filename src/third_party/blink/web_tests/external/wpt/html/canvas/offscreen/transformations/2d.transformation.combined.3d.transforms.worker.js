// DO NOT EDIT! This test has been generated by /html/canvas/tools/gentest.py.
// OffscreenCanvas test in a worker:2d.transformation.combined.3d.transforms
// Description:perspective and rotate3d work together
// Note:

importScripts("/resources/testharness.js");
importScripts("/html/canvas/resources/canvas-tests.js");

var t = async_test("perspective and rotate3d work together");
var t_pass = t.done.bind(t);
var t_fail = t.step_func(function(reason) {
    throw reason;
});
t.step(function() {

var offscreenCanvas = new OffscreenCanvas(100, 50);
var ctx = offscreenCanvas.getContext('2d');

ctx.fillStyle = '#0f0';
ctx.fillRect(0, 0, 100, 50);

// Create a perspective transform in combiation with fillRect to draw a red
// trapezoid then draw a smaller green trapezoid inside it.
ctx.translate(50, 5);
ctx.perspective(100);
ctx.rotate3d(Math.PI/4, 0, 0);
ctx.fillStyle = "#f00";
ctx.fillRect(-30, 0, 60, 40);
ctx.fillStyle = "#0f0";
ctx.fillRect(-15, 10, 30, 20);

// These are the expected points of those two trapezoids from putting
// the corners of the filled rectangles through the perspective transform.
const bigTrapezoid = [[81, 5], [93, 45], [7, 45], [19, 5]];
const smallTrapezoid = [[32, 31], [68, 31], [65, 13], [35, 13]];

// Now filling a shape with green at those exact points with an identity
// transform should result in a purely green image.
ctx.resetTransform();
ctx.beginPath();
ctx.moveTo(bigTrapezoid[3][0], bigTrapezoid[3][1]);
for (const point of bigTrapezoid) ctx.lineTo(point[0], point[1])
ctx.lineTo(smallTrapezoid[3][0], smallTrapezoid[3][1]);
for (const point of smallTrapezoid) ctx.lineTo(point[0], point[1])
ctx.fill();
_assertPixel(offscreenCanvas, 21,11, 0,255,0,255, "21,11", "0,255,0,255");
_assertPixel(offscreenCanvas, 79,11, 0,255,0,255, "79,11", "0,255,0,255");
_assertPixel(offscreenCanvas, 21,39, 0,255,0,255, "21,39", "0,255,0,255");
_assertPixel(offscreenCanvas, 79,39, 0,255,0,255, "79,39", "0,255,0,255");
_assertPixel(offscreenCanvas, 39,19, 0,255,0,255, "39,19", "0,255,0,255");
_assertPixel(offscreenCanvas, 61,19, 0,255,0,255, "61,19", "0,255,0,255");
_assertPixel(offscreenCanvas, 39,31, 0,255,0,255, "39,31", "0,255,0,255");
_assertPixel(offscreenCanvas, 61,31, 0,255,0,255, "61,31", "0,255,0,255");
t.done();

});
done();
