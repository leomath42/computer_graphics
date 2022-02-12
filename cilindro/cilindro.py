from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GL import glVertex3fv
from math import pi as PI
from math import cos, sin

import sys

raio = 1
# i = 1

rad_dx = PI/180


def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glPushMatrix()
    glBegin(GL_LINES)
    glColor3fv((1, 1, 0))
    for i in range(360):

        x = raio * sin(i*rad_dx)
        z = raio * cos(i*rad_dx)
        # Base
        glColor3fv((0.5, 0.5, 0.5))
        glVertex3fv((0, 0, 0))
        glVertex3fv((x, 0, z))

        # Corpo
        glColor3fv((i/360, i/360, 0))
        glVertex3fv((x, 0, z))
        glVertex3fv((x, 5, z))

        # Topo
        glColor3fv((0.5, 0, 0))
        glVertex3fv((0, 5, 0))
        glVertex3fv((x, 5, z))

    glEnd()
    glRotate(1, 1, 0, 0)
    # "Swap dos gráficos computados em background"
    # É necessário para reescrever toda a tela
    # a += 1
    # a = a % 60
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA |
                        GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cilindro")
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
