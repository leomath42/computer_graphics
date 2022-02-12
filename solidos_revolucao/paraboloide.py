from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import math


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

# def z_axis(x, y, a, b, c):
#     z = c * ((x/a)**2 + (y/b)**2)


# def paraboloide():
#     x = r * sin(rad)
#     y = r * cos(rad)
#     z = z_axis(x, y, 1, 1, 1)

p = Paraboloide(1, 1, 0, 1)
# p0 = Paraboloide(1, 1, 2, 1)
# p1 = Paraboloide(1, 1, 1, 1)
# p2 = Paraboloide(2, 2, 2, 1)
# p3 = Paraboloide(3, 3, 3, 1)


# aux = [p]

# for i in range(1, 10):
#     for j in range(1, 10):
#         p_aux = Paraboloide(i, j, 1, 1)
#         aux.append(p_aux)
# aux = []
# P = 4
CHUNKS = 10
vertices = []
for z in range(CHUNKS):
    z = z/CHUNKS
    y = z**2
    vertices.append((0, y, z))

# vertices = (
#     (0, 0.0, 0.0),
#     (0, 0.010000000000000002, 0.1),
#     (0, 0.04000000000000001, 0.2),
#     (0, 0.09, 0.3),
#     (0, 0.16000000000000003, 0.4),
#     (0, 0.25, 0.5),
#     (0, 0.36, 0.6),
#     (0, 0.48999999999999994, 0.7),
#     (0, 0.6400000000000001, 0.8),
#     (0, 0.81, 0.9),
# )


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # p.draw()
    # p1.draw()
    # p2.draw()
    # p3.draw()

    # for i in aux:
    #     i.draw()
    glBegin(GL_LINES)
    for i in range(1, len(vertices)):
        glVertex3fv(vertices[i-1])
        glVertex3fv(vertices[i])

    glEnd()
    glRotate(1, 0, 1, 0)
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
    # glutMotionFunc(mouseMove)
    # glutPassiveMotionFunc(mouseMove)
    # glutMouseFunc(mouse)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -20)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()


if __name__ == '__main__':
    main()
