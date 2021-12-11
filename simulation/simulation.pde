int WIDTH = 800;
int HEIGHT = 800;

// Interface with Figure's definitions.
interface Figure {

    public void draw();
    
    public void move(int x, int y);

    public void verifyCollision();

    public void verifyWorldCollision();
}

// Interface with physical's laws rules
interface PhysicalBody {
    // // // // // // // // |
    // 10 m/s²              |
    // no caso 10 pixels/s² |
    // // // // // // // // / 
    static final float GRAVITY = 10.0;

    float bodyAcceleration = 0.0;
    float bodyVelocity = 0.0;
    float bodyMass = 0.0;

    public void computeNewtonForce();

    public void computeVelocity();

    public void computeBodyPosition();

}

class Ball implements Figure, PhysicalBody {

    // default position axis
    float x = 0.0;
    float y = 0.0;

    // 1 Radian
    float RAD = 0.01745;
    
    int radius = 0;

    public Ball(int radius, int x, int y){
        this.radius = radius;
        this.x = x;
        this.y = y;
    }

    public Ball(int radius){
        // create de body in the origin of the graph;
        this(radius, 0, 0); 
    }

    @Override
    public void draw(){

        drawFigure();
    }

    public void drawFigure(){
        beginShape();
        for(int i=0; i< 360; i++){
            float o = i*RAD;
            x = cos(o) * this.radius;
            y = sin(o) * this.radius;
            vertex(x, y);
        }
        endShape(CLOSE);
    }

    public void move(int x, int y){
        push();
        translate(x, y);
        drawFigure();
        pop();
    }

    public void verifyCollision(){}

    public void verifyWorldCollision(){}

    public void computeNewtonForce(){}
}

void settings(){
    size(WIDTH, HEIGHT);
}

Ball ball = new Ball(10);

void setup() {
    // translate(WIDTH/2, HEIGHT/2);
    // ball.draw();
    // ball.move(0, 5);
}

void draw(){
    translate(WIDTH/2, HEIGHT/2);
    ball.draw();
    // ball.move(0, frameCount);
}
