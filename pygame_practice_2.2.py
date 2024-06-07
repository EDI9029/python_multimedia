import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

rect_position_x = 50
rect_position_y = 50

rect_width = 40
rect_height = 60
rect_single_displacement = 20

jump_command = False
jump_count = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT] and rect_position_x > rect_single_displacement:
        rect_position_x -= rect_single_displacement

    if pressed_keys[pygame.K_RIGHT] and rect_position_x < 500 - rect_width - rect_single_displacement:
        rect_position_x += rect_single_displacement
    
    if not(jump_command):
        if pressed_keys[pygame.K_UP] and rect_position_y > rect_single_displacement:
            rect_position_y -= rect_single_displacement

        if pressed_keys[pygame.K_DOWN] and rect_position_y < 500 - rect_height - rect_single_displacement:
            rect_position_y += rect_single_displacement

        if pressed_keys[pygame.K_SPACE]:
            jump_command = True
    else:
        if jump_count >= -10:
            neg = 2
            if jump_count < 0:
                neg = -2
            rect_position_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        
        else:
            jump_command = False
            jump_count = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (rect_position_x, rect_position_y, rect_width, rect_height))
    pygame.display.update()

pygame.quit()