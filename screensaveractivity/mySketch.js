let Ox = 0; // Origin
let Oy = 0;
let x = 0;
let r = false;
let t = 0; // T for 'tab'     :)
let tabd= false;
let col = 255;
const w = 20;

const c = [randomColor(), randomColor(), randomColor(), randomColor(), randomColor(), randomColor(), randomColor(), randomColor()];
	
function setup() {
  createCanvas(windowWidth, windowHeight);
  frameRate(10); // The faster it is, the bigger the blur is (it's because get() and image() can't keep up)
  noStroke();
  background(35);
  
  Ox = width/16;
  Oy = height-w*3;
  
  x = Ox;
}

function draw() {
	fill(255);
	ellipse(windowWidth-1720,height-53,7,7);
  
  r = (random()>0.75 && r==false);
  
  // Color
  if (random()<0.2 && r) col = color(random(c))
  else if (r) col = 255;
  
  if (tabd) fill("#FFDA3C")
  else fill(col);
  
  if (x==Ox) {
    rect(Ox+t*w-w*tabd, Oy, w, w, 30);
  }else{
    
    if (r) x+=w/2
    else rect(x-w+t*w-w*tabd,Oy, w+w, w, 30);

  }
  
  x+=w;
  
  if ((random() < 0.12 && x>=5*w+t*w) || x>=width-w*3) { // New line
    
    if (tabd) tabd = false;
    
    translate(0, -(4*w/3));
    const g = get(0, 0, width, height);
    image(g, 0, 0, width, height);
    x=Ox;
    
    if (random()<0.45) {
      tabd = true;
      t++;
      x=Ox;
    }else if ((random()<0.8 || t>=6) && t>0) t--;
  }
}