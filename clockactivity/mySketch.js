let sec;
let min;
let hr;

function setup() {
	createCanvas(windowWidth, windowHeight);
	frameRate(60);
}

function draw() {
	background(35);
	rectMode(CENTER);
	angleMode(DEGREES);
	sec = second();
	min = minute();
	hr = hour();
	strokeWeight(12);
	push();
	translate(width/2,height/2);
	
	ellipse(0,0,60);
	push();
	stroke(255);
  let secHand = map(millis(),0,999,0,359);
  rotate(secHand);
	line(0,0,0,-90);
  ellipse(0,-90,25);
  pop();
  
  push();
	stroke(255);
  let minuteHand = map(second(),0,59,0,359);
  rotate(minuteHand);
	line(0,0,0,-160);
  ellipse(0,-160,30);
  pop();
	
	push();
	stroke(255);
	let hourHand = map(minute(),0,59,0,359);
	rotate(hourHand);
	line(0,0,0,-220);
	ellipse(0,-220,35);
	pop();
	
	push();
	stroke(255);
	let dayHand = map(hour(),0,12,0,359);
	rotate(dayHand);
	line(0,0,0,-270);
	ellipse(0,-270,40);
	pop();
	
	fill(255);
	textSize(80);
	text(sec,width-1450,height-1080);
	text(":",width-1490,height-1080);
	text(min,width-1570,height-1080);
	text(":",width-1600,height-1080);
	text(hr,width-1690,height-1080);

}