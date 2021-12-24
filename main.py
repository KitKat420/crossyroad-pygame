import pygame
from pygame import key
from pygame import transform
from pygame.draw import rect
from pygame.constants import K_w
import random
import time
pygame.init()

image_paths = ["./Assets/tesla-model-bus.png",
               "./Assets/tesla-model-car.png",
               "./Assets/tesla-model-convertable.png",
               "./Assets/tesla-model-ems.png",
               "./Assets/tesla-model-pickup.png"]

car_images = []

for image in image_paths:
    car_images.append(pygame.transform.scale(
        pygame.image.load(image), (125, 125)))


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
bg_img = pygame.image.load("./Assets/mountain-bg.jpg", "mountain-bg")


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        player.y -= STEP


def draw_window(player_surface, player_rect, cars):
    # drawing player using image asset and applying rect attributes to the image
    WINDOW.blit(bg_img, (0, 0))
    WINDOW.blit(player_surface, player_rect)

    for car in cars:
        WINDOW.blit(car[0], car[1])
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
    pygame.time.set_timer(my_event, 1000)
    while is_game_on:
        clock.tick(FPS)

        random_car = random.choice(car_images)
        car_as_rect = random_car.get_rect()
        car_as_rect.y = random.randint(50, HEIGHT - 125)
        car_as_rect.x = WIDTH - 100
        car = (random_car, car_as_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_game_on = False
            elif event.type == my_event:

                cars.append(car)

        player_move(player_as_rect, pygame.key.get_pressed())
        draw_window(player_img, player_as_rect, cars)

        for car in cars:
            car[1].x -= 5
    pygame.display.quit()


main()
