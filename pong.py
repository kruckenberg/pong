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
paddle_speed = 10

ball = pygame.Surface((30, 30))
ball.fill((0, 0, 255))
ball_rectangle = pygame.draw.circle(ball, (255, 255, 255), (15, 15), 15)
ball_rectangle.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
ball_direction = -1

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and paddle_rectangle.top > 0:
                paddle_rectangle.move_ip(0, -paddle_speed)
            if event.key == pygame.K_a and paddle_rectangle.bottom < WINDOW_HEIGHT:
                paddle_rectangle.move_ip(0, paddle_speed)
   
    ball_rectangle.move_ip(2 * ball_direction, 0)
    if ball_rectangle.colliderect(paddle_rectangle):
        ball_direction = ball_direction * -1

    if ball_rectangle.left <= 0:
        ball_rectangle.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    window.fill((0, 0, 255))
    window.blit(ball, ball_rectangle)
    window.blit(paddle, paddle_rectangle)
    
    pygame.display.update()

pygame.quit()