import pygame
from pygame import key
from pygame.draw import rect
from pygame.constants import K_w

pygame.init()

clock = pygame.time.Clock()

STEP = 5
FPS = 60
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Roads")


player_img = pygame.transform.scale(
    pygame.image.load("./Assets/pizza.png", "player"), (50, 50))


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        print("moved up")
        player.y -= STEP


def draw_window(player, rect):
    pygame.Surface.fill(WINDOW, WHITE)
    WINDOW.blit(player, rect)
    pygame.display.update()


def main():
    is_game_on = True
    rect_of_player = pygame.Surface.get_rect(player_img)
    rect_of_player.x = WIDTH / 2 - 50
    rect_of_player.y = HEIGHT - 50
    pygame.draw.rect(WINDOW, 0, rect_of_player, )

    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        player_move(rect_of_player, pygame.key.get_pressed())
        draw_window(player_img, rect_of_player)
    pygame.display.quit()


main()
