import pygame, sys, math

pygame.init()

WIDTH = 1048
HEIGHT = 720

WHITE = 255, 255, 255
BLACK = 0, 0, 0
PIE = math.pi

DIV_RATIO = 10
ANGLE_ROT = int(DIV_RATIO * PIE * 2)
RADIUS = 300

mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PerlinNoise")
mainScreen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(0, ANGLE_ROT, 1):
        x = RADIUS * math.cos(i / DIV_RATIO) + (WIDTH / 2)
        y = RADIUS * math.sin(i / DIV_RATIO) + (HEIGHT / 2)
        dot_point = (x , y)
        pygame.draw.circle(mainScreen, BLACK, dot_point, 3)
    
    pygame.display.flip()
