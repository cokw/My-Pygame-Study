import pygame, sys, math, time

pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0

mainScreen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Hello")
drawing = 0
mainScreen.fill(WHITE)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                 drawing = 2

        if event.type == pygame.MOUSEBUTTONUP:
                drawing = 0

        if drawing != 0:
            new_pos_x = int(event.pos[0] // 10) * 10
            new_pos_y = int(event.pos[1] // 10) * 10
            mouse_pos = (new_pos_x, new_pos_y)

            if drawing == 1:
                 pygame.draw.circle(mainScreen, BLACK, mouse_pos, 5)

            if drawing == 2:
                 pygame.draw.circle(mainScreen, WHITE, mouse_pos, 5)

    pygame.display.flip()


