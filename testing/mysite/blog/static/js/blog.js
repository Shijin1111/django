var parts = [];
var waves = []
var can = document.getElementById("cs");
var ctx = can.getContext("2d")
can.width = window.innerWidth;
can.height = window.innerHeight;
function randFrom(min,max) {
   //This function selects a random   decimal number from the minimum to the maximum value 
return Math.random() * (max - min) + min;
}
function randBet(c1,c2) {
   //This function picks a random item between choice 1 and choice 2
var nArr = [c1,c2];
return nArr[Math.floor(Math.random()*2)];
}
function Wave(period,amp,waveL,dir) {
   //This is an object function for creating a Wave with attributes of: period,amplitude,wavelength and direction, all in terms of pixels
this.phase = 0
if(dir == "left") {
var dirVal = 1
} else if(dir == "right") {
var dirVal = -1
}
this.applyTo = function(points) {
    //This sub-function applies the wave properties to a list of points
for(var i = 0; i < points.length; i++) {
var initPhase = 2*Math.PI*points[i].x/waveL
points[i].y += amp*Math.sin(this.phase + (initPhase*dirVal))
var yVal = amp*Math.sin(this.phase + (initPhase*dirVal))
var angVel = 2*Math.PI/period
points[i].acc += -(angVel**2)*yVal
}
this.phase += 2*Math.PI/period
 }
}
function particle(x) {
    //This is an object function that creates a particle with an x-coordinate
this.x = x
this.y = 0
this.acc = 0
this.upd = function() {
    //This sub-function renders and updates the state of the particle
ctx.strokeStyle = "hsl(280,100%," + (Math.abs(this.acc*60)+30) + "%)"
ctx.beginPath();
ctx.arc(this.x,can.height/2+this.y,10,0,2*Math.PI);
ctx.stroke();
this.y = 0
this.acc = 0
}}
function gameMake() {
   //This function determines the initial setup of the program
var num = 400
for(var i = 0; i < num; i++) {
parts.push(new particle(i/(num-1)*can.width))
}
var waveNum = 8
for(var i = 0; i < waveNum; i++) {
waves.push(new Wave(randFrom(50,120),can.height/(2*waveNum),randFrom(200,can.width),randBet("left","right")))
}
}
function gameMove() {
    //This function updates and animates the program
requestAnimationFrame(gameMove)
ctx.clearRect(0,0,can.width,can.height)
for(var i = 0; i < waves.length; i++) {
waves[i].applyTo(parts)
}
for(var i = 0; i < parts.length; i++) {
parts[i].upd();
}}
gameMake()
gameMove()
window.addEventListener('resize', function() {
    can.width = window.innerWidth;
    can.height = window.innerHeight;
});