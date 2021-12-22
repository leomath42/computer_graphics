int WIDTH = 800;
int HEIGHT = 800;
int FRAMES = 60;

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

    // return a float array with ax and ay
    public void computeAcceleration();

    // return a float array with vx and vy
    public void computeVelocity();

    public void computePosition();

    public void setVelocity(float vx, float vy);

    public float[] getVelocity();

    public void setAcceleration(float ax, float ay);

    public float[] getAcceleration();

    public float[] getPosition();

    public void setPosition(float x, float y);


    // public static void applyPhysics(PhysicalBody object){

    // }
}

class Ball implements Figure, PhysicalBody {

    // 1 Radian
    float RAD = 0.01745;
    
    // default position axis
    float[] position = {0.0, 0.0};

    float[] acceleration = {0.0, PhysicalBody.GRAVITY};
    float[] velocity = {0.0, 0.0};
    float[] velocityDirection = {0.0, 1.0};

    float bodyMass = 0.0;

    int radius = 0;

    final float dt = 1/(FRAMES*1/3.0);
    // final float dt = 3.0/(FRAMES);

    public Ball(int radius, int x, int y){
        this.radius = radius;
        this.position[0] = x;
        this.position[1] = y;
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
        float x = 0;
        float y = 0;

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

    public void computeAcceleration(){

        // float[] aacceleration = {
        //     acceleration[0],
        //     acceleration[1] + GRAVITY,
        // };

        // setAcceleration(acceleration[0], acceleration[1]);
    }
    
    public void computeVelocity(){
        
        float[] vvelocity = {
                velocityDirection[0] * velocity[0] +  acceleration[0] * this.dt,
                velocityDirection[1] * velocity[1] +  acceleration[1] * this.dt
        };

        System.out.println("------computeVelocity------");
        System.out.println("dt:" + this.dt);
        System.out.println("vx: "+ vvelocity[0] + " vy: "+ vvelocity[1]);

        setVelocity(vvelocity[0], vvelocity[1]);
    }
    
    public void computePosition(){
        float[] pposition = {
                position[0] + velocity[0] * this.dt,
                position[1] + velocity[1] * this.dt
        };
        System.out.println("-------computePosition------");
        System.out.println("x: "+ pposition[0] + " y: "+ pposition[1]);
        setPosition(pposition[0], pposition[1]);
    }

    // public void computeVelocity(){
    //     // this.bodyAcceleration;
    //     // v0^2+2aDS
    //     velocity = getVelocity();
    //     acceleration = getAcceleration();

    //     float[] vvelocity = {
    //             velocity[0]*velocity[0] + 2 * acceleration[0] * position[0],
    //             velocity[1]*velocity[1] + 2 * acceleration[1] * position[1]
    //     };

    //     setVelocity(velocity[0], velocity[1]);
    // }

    public void setVelocity(float vx, float vy){
        this.velocity[0] = vx;
        this.velocity[1] = vy;
    }

    public float[] getVelocity(){
        return this.velocity;
    }

    public void setAcceleration(float ax, float ay){
        this.acceleration[0] = ax;
        this.acceleration[1] = ay;
    }

    public void setVelocityDirection(float vxd, float vyd){
        this.velocityDirection[0] = vxd;
        this.velocityDirection[1] = vyd;
    }

    public float[] getAcceleration(){
        return this.acceleration;
    }

    public float[] getPosition(){
        return this.position;
    }

    public void setPosition(float x, float y){
        position[0] = x;
        position[1] = y;
    }
}

void settings(){
    size(WIDTH, HEIGHT);
}

Ball ball = new Ball(10);

void applyPhysics(Ball ball){
    ball.computeVelocity();
    ball.computePosition();
    
    float position[] = ball.getPosition();
    

    if(position[1] > HEIGHT){
        // ball.move((int) position[0], HEIGHT - ball.radius);
        ball.setVelocityDirection(0.0, -1.0);
    }
    else if(position[1] < HEIGHT){
        // ball.move((int) position[0], (int) position[1]);
        ball.setVelocityDirection(0.0, 1.0);
    }
    
    ball.move((int) position[0], (int) position[1]);
    // else{
    //     // ball.computeVelocity();
    //     // ball.computePosition();
    //     ball.move((int) position[0], (int) position[1]);
    // }

    System.out.println("-------position------");
    System.out.println("x: "+ position[0] + " y: "+ position[1]);

}

void setup() {
    // translate(WIDTH/2, HEIGHT/2);
    // ball.draw();
    // ball.move(0, 5);
    background(200);
    frameRate(FRAMES);
}

void draw(){
    background(200);
    translate(WIDTH/2, 0);
    // ball.draw();
    // applyPhysics(ball);
    // ball.move(0, frameCount);
    // translate(0, -10);
    // ball.draw();
    applyPhysics(ball);
}
