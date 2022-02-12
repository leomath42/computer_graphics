from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import math
import random


class Paraboloide():

    def __init__(self, a, b, c, r=1):
        # assert a != 0
        # assert b != 0
        # assert c != 0

        self.a = a
        self.b = b
        self.c = c
        self.r = r

    def z_axis(self, x, y):
        z = self.c * ((x/self.a)**2 + (y/self.b)**2)
        return z

    def func(self, rad):
        x = self.r * math.sin(rad)
        z = self.r * math.cos(rad)
        y = self.z_axis(x, z)

        return (x, y, z)

    def draw(self, graus=360):
        rad_dx = 2*math.pi

        glPushMatrix()
        glBegin(GL_QUADS)
        glColor3fv((1, 1, 0))
        anterior = (0, 0, 0)
        for i in range(graus):
            aux = self.func(i)
            # glVertex3fv(anterior)
            glVertex3fv(aux)
            anterior = aux

        glEnd()
        glPopMatrix()


CHUNKS = 10
vertices = []
rad_dx = math.pi/180
raio = 1
# for z in range(CHUNKS):
#     z = z/CHUNKS
#     y = z**2
#     vertices.append((0, y, z))


for i in range(360):

    for j in range(CHUNKS):
        z = j/CHUNKS * math.sin(rad_dx*i)
        x = j/CHUNKS * math.cos(rad_dx*i)
        y = j/CHUNKS
        vertices.append((x, y**2, z))

cores = (
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0.5, 0.5, 0.5),
)


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_LINES)
    for i in range(1, len(vertices)):
        glColor3fv(cores[i % 5])
        glVertex3fv(vertices[i-1])
        glVertex3fv(vertices[i])

    glEnd()
    glRotate(1, 1, 1, 0)
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA |
                        GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Sólidos de Revolução.")
    glutDisplayFunc(draw)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -20)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()


if __name__ == '__main__':
    main()
