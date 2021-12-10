int WIDTH = 800;
int HEIGHT = 800;

// Interface with Figure's definitions.
interface Figure {
    float positionX = 0.0;
    float positionY = 0.0;

    public void draw();
    
    public void move(int x, int y);

    public void verify_collision();

    public void verify_world_collision();
}

// Interface with physical's laws rules
interface PhysicalBody {
    // // // // // // // // |
    // 10 m/s²              |
    // no caso 10 pixels/s² |
    // // // // // // // // / 
    float GRAVITY = 10.0;

    float bodyAcceleration = 0.0;
    float bodyVelocity = 0.0;
    float bodyMass = 0.0;

    public void computeNewtonForce();

}

class Ball implements Figure, PhysicalBody {


    public Ball(int radius, int x, int y){

    }

    public Ball(int radius){
        // create de body in the origin of the graph;
        Ball(radius, 0, 0); 
    }

    @Override
    public void draw(){}

    public void move(int x, int y){

    }

    public void verify_collision(){

    }

    public void verify_world_collision(){
    }

    public void computeNewtonForce(){}
}

void setup(){
}

void draw(){
}
