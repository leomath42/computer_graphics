int WIDTH = 800;
int HEIGHT = 800;
int FRAMES = 60;

class Vector {

    float x;
    float y;

    public Vector(float x, float y){
        this.x = x;
        this.y = y;
    }

    public void add(Vector v){
        this.x += v.x;
        this.y += v.y;
    }

    public void mult(Vector v){

    }

    public void mult(float a){
        this.x *= a;
        this.y *= a;
    }
}
class Ball {

    float raio;
    int [] rgb;
    
    Vector position = new Vector(0, 0);
    Vector velocity = new Vector(0, 0);

    public Ball(float raio, int [] rgb){
        this.raio = raio;
        this.rgb = rgb;
    }

    public void draw() {

    }
    
    public void move(int x, int y){

    }
}

void settings(){
    size(WIDTH, HEIGHT);
}

void setup() {
    background(200);
    frameRate(FRAMES);
}

void draw(){
    background(200);
    translate(WIDTH/2, 0);
}
