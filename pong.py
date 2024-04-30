import pygame

pygame.init()
running = True

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 590
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

paddle = pygame.Surface((25, 90))
paddle.fill((255, 255, 255))
paddle_rectangle = paddle.get_rect()
paddle_rectangle.center = (20, WINDOW_HEIGHT // 2)
paddle_direction = -1
paddle_speed = 5

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paddle_rectangle.move_ip(0, (paddle_direction * paddle_speed))
   
    window.fill((0, 0, 255))
    window.blit(paddle, paddle_rectangle)
    pygame.display.update()

pygame.quit()