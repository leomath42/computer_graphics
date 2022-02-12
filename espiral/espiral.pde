int WIDTH = 800;
int HEIGHT = 800;
int FRAMES = 60;


void settings(){
    size(WIDTH, HEIGHT);
}

void setup() {
    background(200);
    frameRate(FRAMES);
}


float x_aux = 0;
float y_aux = 0;

void draw(){
    // background(200);
    scale(1, -1);
    translate(WIDTH/2, -HEIGHT/2);

    float rad = map(frameCount % 60, 0, 60, 0, 2*PI);

    float x = frameCount * cos(rad);
    float y = frameCount * sin(rad);

    line(x_aux, y_aux, x, y);
    x_aux = x;
    y_aux = y;

}
