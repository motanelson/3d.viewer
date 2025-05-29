import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import struct
import numpy as np
import os
from tkinter import Tk, filedialog

# Cores VGA (0x0 - 0xF)
VGA_COLORS = [
    (0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
    (170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170),
    (85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255),
    (255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)
]

def draw_cube(x, y, z, color_index):
    r, g, b = VGA_COLORS[color_index]
    glColor3f(r / 255, g / 255, b / 255)
    size = 1
    vertices = [
        (x, y, z),
        (x + size, y, z),
        (x + size, y + size, z),
        (x, y + size, z),
        (x, y, z + size),
        (x + size, y, z + size),
        (x + size, y + size, z + size),
        (x, y + size, z + size)
    ]
    faces = (
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 1, 5, 4),
        (2, 3, 7, 6),
        (1, 2, 6, 5),
        (0, 3, 7, 4)
    )
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def load_3d_file(filepath):
    with open(filepath, 'rb') as f:
        if f.read(2) != b'3D':
            raise ValueError("Ficheiro inválido.")
        x_size, xxx, y_size, z_size = struct.unpack('BBBB', f.read(4))
        data = f.read(x_size * y_size * z_size)
        cubes = []
        i = 0
        for z in range(z_size):
            for y in range(y_size):
                for x in range(x_size):
                    color = data[i]
                    if color != 0:
                        cubes.append((x, y, z, color))
                    i += 1
        return cubes

def escolher_ficheiro_3d():
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(
        title="Seleciona um ficheiro .3d",
        filetypes=[("Ficheiros 3D", "*.3d")]
    )
    root.destroy()
    return file_path

def main():
    filepath = escolher_ficheiro_3d()
    if not filepath or not os.path.exists(filepath):
        print("Ficheiro inválido ou cancelado.")
        return

    try:
        cubes = load_3d_file(filepath)
    except Exception as e:
        print("Erro ao carregar ficheiro:", e)
        return

    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Visualizador .3d")

    gluPerspective(45, 800 / 600, 0.1, 1000.0)
    glTranslatef(-10, -10, -40)

    angle = 0
    clock = pygame.time.Clock()
    last_rotate = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(60)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 0.0, 1.0)  # Fundo cinzento escuro
        glEnable(GL_DEPTH_TEST)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        now = pygame.time.get_ticks()
        if now - last_rotate > 2000:
            angle = (angle + 90) % 360
            last_rotate = now

        glPushMatrix()
        glRotatef(angle, 0, 1, 0)

        for cube in cubes:
            draw_cube(*cube)

        glPopMatrix()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
