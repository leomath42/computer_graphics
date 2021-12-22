static final int WIDTH = 800;
static final int HEIGHT = 800;


float[] P0 = {-200, 0};
float[] P1 = {-100, 200};
float[] P2 = {100, 200};
float[] P3 = {200, 0};

int point_to_change = -1;

public void settings() {
    size(800, 800);
}

void changePoint(float[] point){
    point[0] = mouseX - WIDTH/2;
    point[1] = -(mouseY - HEIGHT/2);
    System.out.println("x: " + point[0] + " y: " + point[1]);
}

void mouseMoved() {
    switch (point_to_change) {
        case 0 :
            changePoint(P0);
        break;
        case 1 :
            changePoint(P1);
        break;
        case 2 :
            changePoint(P2);
        break;	
        case 3 :
            changePoint(P3);
        break;
        case -1:
        break;		
    }
}

void keyTyped() {
    int code = key - 48;
    boolean isNumBetween_0_3 = 0 <= code && code <= 3;
    boolean isLowerCaseLetters = 49 <= code && code <= 74;

    if(isNumBetween_0_3){
        point_to_change = code;
    }
    else if(isLowerCaseLetters){
        point_to_change = -1;
    }

    println("typed " + int(key) + " " + code + " " + point_to_change);
}

void setup(){
}

float[] parametricStraightLine(float[] P0, float[] P1, float t){
    float x = P0[0] + (P1[0] - P0[0]) * t;
    float y = P0[1] + (P1[1] - P0[1]) * t;

    return new float[] {x, y};
}


void draw(){
    background(200);
    translate(WIDTH/2, HEIGHT/2);
    
    scale(1, -1);
    circle(P0[0], P0[1], 10);
    circle(P1[0], P1[1], 10);
    circle(P2[0], P2[1], 10);
    circle(P3[0], P3[1], 10);

    beginShape();
    for(float f=0; f<1; f+=0.01){
        
        // reta 1 p1 - p0
        float r1[] = parametricStraightLine(P0,  P1, f);
        
        // reta 2 p2 - p1
        float r2[] = parametricStraightLine(P1, P2, f);

        // reta 2 p2 - p1
        float r3[] = parametricStraightLine(P2, P3, f);

        // Bezier curve 2nd/reta entre reta1 - reta2
        float b2nd_1[] = parametricStraightLine(r1, r2, f);

        // Bezier curve 2nd/reta entre reta2 - reta3
        float b2nd_2[] = parametricStraightLine(r2, r3, f);

        circle(r1[0], r1[1], 1);
        circle(r2[0], r2[1], 1);
        circle(r3[0], r3[1], 1);

        circle(b2nd_1[0], b2nd_1[1], 1);
        circle(b2nd_2[0], b2nd_2[1], 1);

        // Bezier curve 3nd/reta entre bezier 2nd_1 - bezier 2nd_2
        float b[] = parametricStraightLine(b2nd_1, b2nd_2, f);
        vertex(b[0],  b[1]);
    }
    endShape();
}