import pygame

pygame.init()
running = True

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

paddle = pygame.Surface((200, 200))
paddle.fill((37, 150, 47))
paddle_rect = paddle.get_rect()
paddle_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
paddle_direction = -1
paddle_speed = 1

ball = pygame.Surface((30, 30))
ball.fill((132, 60, 43))
ball_rectangle = pygame.draw.circle(ball, (53, 49, 222), (15, 15), 15)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paddle_direction *= -1
            if event.key == pygame.K_e:
                paddle_speed += 1
            if event.key == pygame.K_q:
                if paddle_speed > 0:
                    paddle_speed -= 1

    window.fill((132, 60, 43))
    if paddle_rect.left <= 0 or paddle_rect.right >= WINDOW_WIDTH:
        paddle_direction *= -1
    paddle_rect.move_ip(paddle_speed * paddle_direction, 0)
    ball_rectangle.move_ip(1, 1)
    window.blit(paddle, paddle_rect)
    window.blit(ball, ball_rectangle)
    
    pygame.display.flip()

pygame.quit()