import pygame, sys

# 초기화
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 화면 디스플레이
mainScreen = pygame.display.set_mode((1440, 720))
pygame.display.set_caption("Hi")
mainScreen.fill(WHITE)

# 변수 초기화
drawing = 0
last_pos = (0, 0)

# 메인루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = 1

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = 0


        if event.type == pygame.MOUSEMOTION:
            if drawing == 1:
                pygame.draw.line(mainScreen, BLACK, last_pos, event.pos, 3)

            last_pos = ( event.pos[0], event.pos[1] )
        
            

    pygame.display.flip()
