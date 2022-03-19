import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from PIL import Image

vertices = (
    # front face
    (-1.0, -1.0, 1.0),
    (1.0, -1.0, 1.0),
    (1.0, 1.0, 1.0),
    (-1.0, 1.0, 1.0),
    # Back Face,
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    # Top Face,
    (-1.0, 1.0, -1.0),
    (-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),
    (1.0, 1.0, -1.0),
    # Bottom Face,
    (-1.0, -1.0, -1.0),
    (1.0, -1.0, -1.0),
    (1.0, -1.0, 1.0),
    (-1.0, -1.0, 1.0),
    # Right face,
    (1.0, -1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
    # Left Face
    (-1.0, -1.0, -1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (-1.0, 1.0, -1.0),
)

textures_coords = (
    # Front face (1),
    (0.0, 0.0),
    (0.0, 1 / 2),
    (1 / 3, 1 / 2),
    (1 / 3, 0.0),
    # Back Face (5),
    (1 / 3, 1 / 2),
    (1 / 3, 1),
    (2 / 3, 1),
    (2 / 3, 1 / 2),
    # Top Face (4),
    (0.0, 1 / 2),
    (0.0, 1),
    (1 / 3, 1),
    (1 / 3, 1 / 2),
    # Bottom Face (2)
    (1 / 3, 0.0),
    (1 / 3, 1 / 2),
    (2 / 3, 1 / 2),
    (2 / 3, 0.0),
    # Right face (6),
    (2 / 3, 1 / 2),
    (2 / 3, 1),
    (1, 1),
    (1, 1 / 2),
    # Left Face (3)
    (2 / 3, 0.0),
    (2 / 3, 1 / 2),
    (1.0, 1 / 2),
    (1.0, 0),
)


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
        # glLoadIdentity()

        glClearColor(0.5, 0.5, 0.5, 1.0)

        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glBegin(GL_QUADS)

        for t, v in zip(self.texture_coords, self.vertex):
            glTexCoord2f(*t)
            glVertex3f(*v)

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
    # load_texture()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo com textura")
    # glutReshapeFunc(ReSizeGLScene)
    # glutKeyboardFunc(keyPressed)
    # glutSpecialFunc(teclaEspecialPressionada)
    # LoadTextures()
    InitGL(640, 480)
    textures = load_textures(["dado.png"])
    dado = GLObject(
        texture_id=textures[0], vertex=vertices, texture_coords=textures_coords
    )
    count = 0

    def draw():
        nonlocal count
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(0, 0.0, -10)

        glRotatef(count, 1.0, 0.0, 0.0)
        glRotatef(count, 0.0, 1.0, 0.0)
        glRotatef(count, 0.0, 0.0, 1.0)
        dado.draw()
        # glTranslatef(100, 0.0, 0)
        glPopMatrix()
        if count > 360:
            count = 0
        count += 0.25

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glutMainLoop()


if __name__ == "__main__":
    main()
