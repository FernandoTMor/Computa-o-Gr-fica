import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Variáveis globais para transformação
zoom = 1.0
rotation_anglex = 0
rotation_angley = 0
translacao_X, translacao_Y = 0.0, 0.0
theta = 0  # Ângulo de rotação automática

# Configuração inicial do OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)  # Ajuste da tela para 800x600
    glMatrixMode(GL_MODELVIEW)

# Função para desenhar um quadrado com linhas
def draw_square_lines():
    glLoadIdentity()
    glTranslatef(translacao_X, translacao_Y, -6.0)
    glScalef(zoom, zoom, 1.0)
    glRotatef(rotation_anglex, 1, 0, 0)
    glRotatef(rotation_angley, 0, 1, 0)
    glRotatef(theta, 0, 0, 1)  # Rotação automática no eixo Z

    glColor3f(0.0, 0.0, 1.0)  # Azul
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

# Função principal
def main():
    global zoom, rotation_anglex, rotation_angley, translacao_X, translacao_Y, theta
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_s:
                    translacao_Y -= 0.1
                elif event.key == K_w:
                    translacao_Y += 0.1
                elif event.key == K_a:
                    translacao_X -= 0.1
                elif event.key == K_d:
                    translacao_X += 0.1
                elif event.key == K_f:
                    rotation_anglex += 5
                elif event.key == K_r:
                    rotation_anglex -= 5
                elif event.key == K_q:
                    rotation_angley += 5
                elif event.key == K_e:
                    rotation_angley -= 5
                elif event.key == K_z:
                    zoom /= 1.1
                elif event.key == K_x:
                    zoom *= 1.1

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom *= 1.1
                elif event.button == 5:
                    zoom /= 1.1

        theta += 1  # Incrementa o ângulo para rotação contínua

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square_lines()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()