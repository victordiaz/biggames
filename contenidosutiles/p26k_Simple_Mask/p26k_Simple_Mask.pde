/** 
 * Medialab Prado Media Wall super basic template.
 * 23 Jan 2011, Chris Sugrue
 *
 * Press spacebar to toggle outline on/off
 * The outline is just outside the facade area. Does not appear on the screen.
 */ 

// boolean to toggle mask on/off
boolean bShowMask = true; 

// facade setup variables, offset from top left is 40,40
int leftOffset  = 40;
int topOffset   = 40;

int screenWidth   = 192;
int screenHeight  = 157;


void setup() 
{
  size(1024, 768); // facade computer runs at 1024x768
  frameRate(24);  // lock the frame rate
}

void draw() 
{
  // refresh background
  background(127);
  fill(0);
  noStroke();
  
  rect(40,40,72,16);
  rect(40,56,36,16);
  rect(160,40,72,16);
  rect(196,56,36,16);
  
  
  
  pushMatrix();
  translate(40,40);
 // write your code here for the top bars
 
 pushMatrix();
 translate(0,32);
 
     // write your code here for main part
 
  popMatrix();
  popMatrix();
  
  //-----------------------------
  // keep this at the end of draw
  drawMaskOutline();

}


void keyPressed() 
{
  if( key == ' ' ) bShowMask = !bShowMask;
}


void drawMaskOutline()
{
  if(bShowMask){
    noFill();
    stroke(255);
    rect( leftOffset-1, topOffset-1, screenWidth+1, screenHeight+1);
 // rect(39,39,193,158); //draw outside of facade area
  }
}



