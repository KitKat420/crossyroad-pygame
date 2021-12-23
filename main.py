import pygame
from pygame import key
from pygame import transform
from pygame.draw import rect
from pygame.constants import K_w
import random

pygame.init()


clock = pygame.time.Clock()

STEP = 5
FPS = 60
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Roads")

player_img = pygame.transform.scale(
    pygame.image.load("./Assets/pizza.png", "player"), (50, 50))


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        player.y -= STEP


def draw_window(player_surface, player_rect, cars):
    # drawing player using image asset and applying rect attributes to the image
    WINDOW.fill(WHITE)
    WINDOW.blit(player_surface, player_rect)

    for i in cars:
        pygame.draw.rect(WINDOW, BLACK, i)
    pygame.display.flip()


def main():
    is_game_on = True
    cars = []
    # basically converting Surface object into a Rect object
    player_as_rect = pygame.Surface.get_rect(player_img)
    # setting starting position of player
    player_as_rect.x = WIDTH / 2 - 50
    player_as_rect.y = HEIGHT - 50

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 5000)

    while is_game_on:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_game_on = False
            elif event.type == my_event:
                pass
        car = pygame.Rect(WIDTH - 100, HEIGHT - 50, 75, 20)
        car.y = random.randint(50, HEIGHT - 50)
        cars.append(car)
        player_move(player_as_rect, pygame.key.get_pressed())
        draw_window(player_img, player_as_rect, cars)

        for car in cars:
            car.x -= 5
    pygame.display.quit()


main()
