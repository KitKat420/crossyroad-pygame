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

car_img = pygame.transform.scale(
    pygame.image.load("./Assets/tesla-model-car.png", "car"), (50, 50))


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        player.y -= STEP


def draw_window(player, rect):
    pygame.Surface.fill(WINDOW, WHITE)
    # drawing player using image asset and applying rect attributes to the image
    WINDOW.blit(player, rect)
    WINDOW.blit(car_img, (100, 100))
    pygame.display.update()


def main():
    is_game_on = True
    # basically converting Surface object into a Rect object
    player_as_rect = pygame.Surface.get_rect(player_img)
    # setting starting position of player
    player_as_rect.x = WIDTH / 2 - 50
    player_as_rect.y = HEIGHT - 50

    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        player_move(player_as_rect, pygame.key.get_pressed())
        draw_window(player_img, player_as_rect)
    pygame.display.quit()


main()
