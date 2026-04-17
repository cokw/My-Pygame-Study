# My-Pygame-Study
Python Library 파이게임 기초부터 공부하기


<img width="731" height="524" alt="스크린샷 2026-04-17 230848" src="https://github.com/user-attachments/assets/0ee0d8e6-ff43-443c-8c6d-39c701588608" />


\```python
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

\```



