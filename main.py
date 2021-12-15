import pygame, os, sys


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((700, 700))
cords_mouse = (None, None)
image = load_image("arrow.png")
fps = 100
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cords_mouse = event.pos
    if cords_mouse[0] and pygame.mouse.get_focused():
        screen.blit(image, cords_mouse)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

