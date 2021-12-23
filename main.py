import pygame
from pygame import key
from pygame import transform
from pygame.draw import rect
from pygame.constants import K_w
import random

pygame.init()

vehicle_images = ["./Assets/tesla-model-bus.png",
                  "./Assets/tesla-model-car.png",
                  "./Assets/tesla-model-convertable.png",
                  "./Assets/tesla-model-ems.png",
                  "./Assets/tesla-model-pickup.png"]

clock = pygame.time.Clock()

STEP = 5
FPS = 60
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Roads")

vehicles = []

for vehicle in vehicle_images:
    transform_image = pygame.transform.scale(
        pygame.image.load(vehicle), (125, 125))
    vehicles.append(transform_image)

print(vehicles)

player_img = pygame.transform.scale(
    pygame.image.load("./Assets/pizza.png", "player"), (50, 50))


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        player.y -= STEP


def draw_window(player, player_rect, vehicle, vehicle_rect):
    pygame.Surface.fill(WINDOW, WHITE)
    # drawing player using image asset and applying rect attributes to the image
    WINDOW.blit(player, player_rect)
    WINDOW.blit(vehicle, vehicle_rect)
    pygame.display.update()


def main():
    is_game_on = True
    # basically converting Surface object into a Rect object
    player_as_rect = pygame.Surface.get_rect(player_img)
    # setting starting position of player
    player_as_rect.x = WIDTH / 2 - 50
    player_as_rect.y = HEIGHT - 50

    # Vehicle stuff
    random_vehicle = random.choice(vehicles)
    vehicle_as_rect = pygame.Surface.get_rect(random_vehicle)

    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        player_move(player_as_rect, pygame.key.get_pressed())
        draw_window(player_img, player_as_rect,
                    random_vehicle, vehicle_as_rect)
    pygame.display.quit()


main()
