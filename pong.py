import pygame

pygame.init()
running = True

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 590
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

score_left = 0
score_right = 0

font = pygame.font.Font(None, 64)


paddle_left = pygame.Surface((25, 90))
paddle_left.fill((255, 255, 255))
paddle_left_rectangle = paddle_left.get_rect()
paddle_left_rectangle.center = (20, WINDOW_HEIGHT // 2)

paddle_right = pygame.Surface((25, 90))
paddle_right.fill((255, 255, 255))
paddle_right_rectangle = paddle_left.get_rect()
paddle_right_rectangle.center = (WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2)

paddle_speed = 10

ball = pygame.Surface((30, 30))
ball.fill((0, 0, 255))
ball_rectangle = pygame.draw.circle(ball, (255, 255, 255), (15, 15), 15)
ball_rectangle.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
ball_x_direction = -1
ball_y_direction = -1

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and paddle_left_rectangle.top > 0:
                paddle_left_rectangle.move_ip(0, -paddle_speed)
            if event.key == pygame.K_a and paddle_left_rectangle.bottom < WINDOW_HEIGHT:
                paddle_left_rectangle.move_ip(0, paddle_speed)
   


    
    ball_rectangle.move_ip(2 * ball_x_direction, 2 * ball_y_direction)
    
    if ball_rectangle.colliderect(paddle_left_rectangle) or ball_rectangle.colliderect(paddle_right_rectangle):
        ball_x_direction = ball_x_direction * -1

    # detect wall collision, change y direction
    if ball_rectangle.top <= 0 or ball_rectangle.bottom >= WINDOW_HEIGHT:
        ball_y_direction = ball_y_direction * -1
    
    if ball_rectangle.left <= 0:
        ball_rectangle.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        score_right = score_right + 1
    
    if ball_rectangle.right >= WINDOW_WIDTH:
        ball_rectangle.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        score_left = score_left + 1

    scoreboard = font.render(f"{score_left}  - {score_right}", True, (255, 255, 255))

    window.fill((0, 0, 255))
    window.blit(scoreboard, (WINDOW_WIDTH // 2 + 15, 15))
    window.blit(ball, ball_rectangle)
    window.blit(paddle_left, paddle_left_rectangle)
    window.blit(paddle_right, paddle_right_rectangle)
    
    pygame.display.update()

pygame.quit()