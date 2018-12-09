
let snowflakes = []; // create snowflakes

function setup() {
  createCanvas(1920, 1080);
  fill(300); 
  noStroke();
}

function draw() {
  background('blue');
  let t = frameCount / 100; // counts the number of frames displayed

  // create a random number of snowflakes each frame
  for (var i = 0; i < random(10); i++) {
    snowflakes.push(new snowflake()); // append snowflake object
  }

  // create loop display
  for (let flake of snowflakes) {
    flake.update(t); // update snowflake position
    flake.display(); // draw snowflake
  }
}

// snowflake class
function snowflake() {
  // initiate coordinates
  this.posX = 0;
  this.posY = random(-10, 0);
  this.initialangle = random(0, 10 * PI);
  this.size = random(2, 10);

  // create sprial among the snowflakes
  // make sure that the snowflakes are spread across the screen
  this.radius = sqrt(random(pow(width / 3, 3)));

 this.update = function(time) {
    // x position follows a circle
    let w = 0.1; // the snowflakes move around in an anglular speed
    let angle = w * time + this.initialangle;
    this.posX = width / 6 + this.radius * sin(angle);

    // x is different size snowflakes and y is speed
    this.posY += pow(this.size, 0.1);

    // if any snowflake is passing the edge of the screen it must disappear
    if (this.posY > height) {
      let index = snowflakes.indexOf(this);
      snowflakes.splice(index, 1);
    }
  };

  this.display = function() {
    ellipse(this.posX, this.posY, this.size);
  };
}


 