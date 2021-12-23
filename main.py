import pygame

pygame.init()

clock = pygame.time.Clock()

FPS = 60
WIDTH, HEIGHT = (800, 500)
WHITE = (255, 255, 255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Roads")


def draw_window():
    pygame.Surface.fill(WINDOW, WHITE)

    pygame.display.update()


def main():
    is_game_on = True
    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        draw_window()
    pygame.display.quit()


main()
