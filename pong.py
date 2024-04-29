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

blocks = pygame.Surface((100, 100))
blocks.fill((25, 87, 3))
blocks_rect = blocks.get_rect()


while running:
    # clock.tick(60)
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
    paddle.blit(blocks, blocks_rect)
    window.blit(paddle, paddle_rect)
    
    pygame.display.flip()

pygame.quit()