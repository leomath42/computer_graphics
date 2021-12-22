Integer WIDTH = 800;
Integer HEIGHT = 800;


int[] P0 = {-200, 0};
int[] P1 = {0, 200};
int[] P2 = {200, 0};

public void settings() {
    size(800, 800);
}

void mouseMoved() {
    System.out.println("x: " + mouseX + " y: " + mouseY);
    P1[0] = mouseX - WIDTH/2;
    P1[1] = -(mouseY - HEIGHT/2);
}

void setup(){
}


void draw(){
    background(200);
    translate(WIDTH/2, HEIGHT/2);
    
    scale(1, -1);
    circle(P0[0], P0[1], 10);
    circle(P2[0], P2[1], 10);
    circle(P1[0], P1[1], 10);

    beginShape();
    for(float f=0; f<1; f+=0.01){
        // reta 1 p1 - p0
        float xr1 = P0[0] + (P1[0] - P0[0]) * f;
        float yr1 = P0[1] + (P1[1] - P0[1]) * f;

        // reta 2 p2 - p1
        float xr2 = P1[0] + (P2[0] - P1[0]) * f;
        float yr2 = P1[1] + (P2[1] - P1[1]) * f;


        // Bezier curve/reta entre reta2 - reta1
        float bx = xr1 + (xr2 - xr1) * f;
        float by = yr1 + (yr2 - yr1) * f;
        
        circle(xr1, yr1, 1);
        circle(xr2, yr2, 1);
        vertex(bx,  by);
    }
    endShape();
}