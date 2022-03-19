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
l_vertices = (a, (0, Y, 0), b, b, (0, Y, 0), c, c, (0, Y, 0), d, d, (0, Y, 0), a)

# tuplas com os vertices da base da pirâmede.
b_vertices = (a, b, c, d)

linhas = ((0, 1), (1, 2), (2, 0))

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
    glPushMatrix()
    # glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)
    glRotate(a, 1, 1, 1)

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
    glPopMatrix()

    # "Swap dos gráficos computados em background"
    # É necessário para reescrever toda a tela
    a += 1
    # a = a % 60
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


def init():
    # bronze ref: http://learnwebgl.brown37.net/10_surface_properties/surface_properties_color.html
    mat_ambient = (0.2125, 0.1275, 0.054, 1.0)
    mat_diffuse = (0.714, 0.4284, 0.18144, 1.0)

    mat_specular = (0.393548, 0.271906, 0.166721, 1.0)
    mat_shininess = (25.6,)
    light_position = (0.2, 0.0, 0.0, 0.0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Pirâmide com Luz")
    init()
    glutDisplayFunc(draw)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)

    glutTimerFunc(10, timer, 1)
    glutMainLoop()


if __name__ == "__main__":
    main()
