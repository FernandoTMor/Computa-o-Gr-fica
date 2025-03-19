import pygame  # Biblioteca para gerenciamento de janelas e eventos
from pygame.locals import *  # Importa constantes do Pygame
from OpenGL.GL import *  # Importa funções do OpenGL
from OpenGL.GLU import *  # Importa funções utilitárias do OpenGL
import math  # Importa a biblioteca matemática para cálculos trigonométricos

zoom = 1.0
rotation_angle = 0
translacao_X, translacao_Y = 0.0, 0.0

def init():
    """Configuração inicial do OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo como preta
    glClearDepth(1.0)  # Define a profundidade do buffer de profundidade
    glEnable(GL_DEPTH_TEST)  # Ativa o teste de profundidade para ocultação
    glDepthFunc(GL_LEQUAL)  # Define a função de profundidade como "menor ou igual"
    glMatrixMode(GL_PROJECTION)  # Define a matriz de projeção
    glLoadIdentity()  # Reseta a matriz de projeção
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)  # Define a perspectiva 3D
    glMatrixMode(GL_MODELVIEW)  # Retorna à matriz de modelo/visualização

def draw_circle(radius, num_segments=100):
    """Desenha um círculo usando OpenGL."""
    glLoadIdentity()  # Reseta a matriz de modelagem
    glTranslatef(translacao_X, translacao_Y, -5.0)  # Aplica a translação
    glScalef(zoom, zoom, 1.0)  # Aplica o zoom
    glRotatef(rotation_angle, 0, 1, 0)  # Aplica a rotação no eixo Z

    glColor3f(0.0, 1.0, 0.0)  # Define a cor do círculo como verde

    glBegin(GL_LINE_LOOP)  # Inicia o desenho de uma linha fechada (círculo)
    for i in range(num_segments):  # Loop para desenhar os pontos do círculo
        angle = 2.0 * math.pi * i / num_segments  # Calcula o ângulo do ponto atual
        x = radius * math.cos(angle)  # Calcula a coordenada X do ponto
        y = radius * math.sin(angle)  # Calcula a coordenada Y do ponto
        glVertex2f(x, y)  # Define o ponto no círculo
    glEnd()  # Finaliza o desenho do círculo

def main():
    """Função principal para inicializar o Pygame e renderizar o círculo."""
    global zoom, rotation_angle, translacao_X, translacao_Y  # Declara as variáveis globais

    pygame.init()  # Inicializa o Pygame
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)  # Cria a janela com suporte a OpenGL
    init()  # Configurações iniciais do OpenGL

    running = True  # Variável de controle do loop principal
    while running:  # Loop principal do programa
        for event in pygame.event.get():  # Verifica eventos do Pygame
            if event.type == pygame.QUIT:  # Se o usuário fechar a janela
                running = False  # Sai do loop
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Se pressionar ESC
                    running = False  # Sai do loop
                elif event.key == K_s:  # Mover para cima
                    translacao_Y -= 0.1
                elif event.key == K_w:  # Mover para baixo
                    translacao_Y += 0.1
                elif event.key == K_a:  # Mover para a esquerda
                    translacao_X -= 0.1
                elif event.key == K_d:  # Mover para a direita
                    translacao_X += 0.1
                elif event.key == K_f:  # Rotacionar sentido horário
                    rotation_angle += 5
                elif event.key == K_r:  # Rotacionar sentido anti-horário
                    rotation_angle -= 5
                elif event.key == K_z:  # Zoom out
                    zoom /= 1.1
                elif event.key == K_x:  # Zoom in
                    zoom *= 1.1

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom *= 1.1
                elif event.button == 5:
                    zoom /= 1.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela e o buffer de profundidade
        draw_circle(2)  # Chama a função para desenhar o círculo com raio 2
        pygame.display.flip()  # Atualiza a tela
        pygame.time.wait(10)  # Pequeno atraso para controlar a taxa de atualização

    pygame.quit()  # Finaliza o Pygame quando o loop termina

if __name__ == "__main__":
    main()  # Executa a função principal se o script for rodado diretamente
