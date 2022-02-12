int WIDTH = 800;
int HEIGHT = 800;
int FRAMES = 20;

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

    public void mult(float a){
        this.x *= a;
        this.y *= a;
    }
}
class Ball {

    float raio;
    int [] rgb;
    // Distância diagonal entre o centro(um planeta, sol, etc) e o objeto atual;
    float distance = 10;
    
    Vector position = new Vector(0, 0);
    Vector velocity = new Vector(0, 0);

    public Ball(float raio, int [] rgb){
        this.raio = raio;
        this.rgb = rgb;
    }

    public Ball(float raio, int [] rgb, Vector position){
        this(raio, rgb);
        this.position = position;
    }
    
    public Ball(float raio, int [] rgb, float distance){
        this(raio, rgb);
        this.distance = distance;
    }

    public void setDistance(float distance){
        this.distance = distance;
    }

    public float getDistance(){
        return this.distance;
    }

    public void draw() {
        pushMatrix();
        // scale(0, 0);
        // translate(0, 0);
        fill(rgb[0], rgb[1], rgb[2]);
        circle(position.x, position.y, this.raio);
        popMatrix();
    }
    
    public void move(Vector v){
        this.position.add(v);
    }

    public void move(float rad){
        float y = this.distance * sin(rad);
        float x = this.distance * cos(rad);

        this.position = new Vector(x, y);
    }
}

void settings(){
    size(WIDTH, HEIGHT);
}

void setup() {
    background(200);
    frameRate(FRAMES);
}

Ball sol = new Ball(100, new int[]{200, 150, 0});
Ball terra = new Ball(40, new int[]{0, 0, 150}, 200);
Ball lua = new Ball(10, new int[]{150, 150, 150}, 50);

void draw(){
    scale(1, -1);
    translate(WIDTH/2, -HEIGHT/2);
    background(200);
    
    float terra_rad = map(frameCount % 600, 0, 600, 0, 2*PI);
    float lua_rad = map(frameCount % 60, 0, 60, 0, 2*PI);
    
    sol.draw();
    terra.draw();
    terra.move(terra_rad);
    translate(terra.position.x, terra.position.y);
    lua.draw();
    lua.move(lua_rad);
}
