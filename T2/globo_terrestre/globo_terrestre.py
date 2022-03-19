import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from PIL import Image

import math

r = 1
chunk = 30
theta_d = math.pi / chunk  # o in [-pi/2 , pi/2]
phi_d = 2 * math.pi / chunk  # phi in [0, 2pi]


def sphere(r, theta, phi):
    x = r * math.cos(theta) * math.cos(phi)
    z = r * math.cos(theta) * math.sin(phi)
    y = r * math.sin(theta)

    return x, y, z


class GLObject(object):
    def __init__(
        self,
        texture_id=None,
        vertex: list = [],
        texture_coords: list = [],
        *args,
        **kwargs
    ):

        self.texture_id = texture_id
        self.vertex = vertex
        self.texture_coords = texture_coords

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glBegin(GL_TRIANGLE_STRIP)
        glColor3fv((0.0, 0.0, 1))
        for i in range(30):
            for j in range(30):

                theta = j * theta_d - math.pi / 2
                phi = i * phi_d
                glTexCoord2f(i / 30, j / 30)
                glVertex3fv(sphere(r, theta, phi))

                theta_2 = (j + 1) * theta_d - math.pi / 2
                phi_2 = (i + 1) * phi_d
                glTexCoord2f((i + 1) / 30, (j + 1) / 30)
                glVertex3fv(sphere(r, theta_2, phi_2))
        glEnd()

        glutSwapBuffers()


def load_textures(images: list) -> list:
    n = len(images)

    textures = []
    if n < 2:
        textures = [glGenTextures(n)]
    else:
        textures = glGenTextures(n)

    for i, path in enumerate(images):
        ################################################################################
        glBindTexture(GL_TEXTURE_2D, textures[i])

        with Image.open(path) as img:
            w, h = img.size
            pixels = img.tobytes()

        modo = GL_RGB

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels)
        #    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        #    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        ################################################################################

    return textures


def InitGL(Width, Height):
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Globo terrestre")
    InitGL(640, 480)
    textures = load_textures(["mapa.png"])
    globo = GLObject(texture_id=textures[0], vertex=[], texture_coords=[])
    count = 0

    def draw():
        nonlocal count
        glLoadIdentity()
        glTranslatef(0, 0, -4)
        glRotatef(180, 0.0, 0.0, 1.0)
        glRotatef(count, 0.0, 1.0, 0.0)
        globo.draw()
        if count > 360:
            count = 0
        count += 0.25

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glutMainLoop()


if __name__ == "__main__":
    main()
