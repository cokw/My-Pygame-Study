import pygame, sys, math, time

pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0

mainScreen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Hello")
drawing = False
mainScreen.fill(WHITE)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

        if drawing == True:

            new_pos_x = int(event.pos[0] // 10) * 10
            new_pos_y = int(event.pos[1] // 10) * 10
            mouse_pos = (new_pos_x, new_pos_y)



            pygame.draw.circle(mainScreen, BLACK, mouse_pos, 5)


    pygame.display.flip()


