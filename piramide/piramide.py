from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GL import glVertex3fv
from math import pi as PI
from math import cos, sin

import sys

# Altura geral da pirâmide.
Y = 1

a = (-1, 0, -1)
b = (-1, 0, 1)
c = (1, 0, 1)
d = (1, 0, -1)

# tuplas com os vertices dos lados da pirâmide.
l_vertices = (
    a,
    (0, Y, 0),
    b,
    b,
    (0, Y, 0),
    c,
    c,
    (0, Y, 0),
    d,
    d,
    (0, Y, 0),
    a
)

# tuplas com os vertices da base da pirâmede.
b_vertices = (
    a,
    b,
    c,
    d
)

linhas = (
    (0, 1),
    (1, 2),
    (2, 0)
)

# Cores (vermelho, verde, azul, amarelo e cinza).
cores = (
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0.5, 0.5, 0.5),
)


a = 5


def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glPushMatrix()
    glBegin(GL_TRIANGLES)

    # constroi os lados da pirâmide.
    for i, v in enumerate(l_vertices):
        if i % 3 == 0:
            glColor3fv(cores[i // 3])
        glVertex3fv(v)
    glEnd()

    # desenha a  base da pirâmide.
    glColor3fv(cores[4])
    glBegin(GL_QUADS)
    for v in b_vertices:
        glVertex3fv(v)
    glEnd()
    # glPopMatrix()1
    glRotate(a, 1, 0, 0)

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
    glutCreateWindow("Pirâmide")
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
