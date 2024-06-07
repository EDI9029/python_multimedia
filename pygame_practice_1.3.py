import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
displacement = 8

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT]:
        x -= displacement
    

    if pressed_keys[pygame.K_RIGHT]:
        x += displacement
    

    if pressed_keys[pygame.K_UP]:
        y -= displacement
    

    if pressed_keys[pygame.K_DOWN]:
        y += displacement
    

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()