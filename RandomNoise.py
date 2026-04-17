import pygame, sys, math, time, random

# 초기화
pygame.init()

# 상수 설정
WHITE = 255, 255, 255
BLACK = 0, 0, 0
i = 0; j = 0

# 환경 설정
mainScreen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("RandomPixel")
mainScreen.fill(WHITE)

# 메인 루프
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for i in range(0, 720, 10):
        for j in range(0, 480, 10):
            dot_pos = (i, j)
            randint = random.randint(0,10)
            if randint == 1:
                pygame.draw.circle(mainScreen, BLACK, dot_pos, 5)
            else:
                pygame.draw.circle(mainScreen, WHITE, dot_pos, 5)



    pygame.display.flip()


