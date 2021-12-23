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

list_of_vehicles = []

STEP = 5
FPS = 8
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Roads")

vehicles = []

for vehicle in vehicle_images:
    transform_image = pygame.transform.scale(
        pygame.image.load(vehicle), (125, 125))
    vehicles.append(transform_image)


player_img = pygame.transform.scale(
    pygame.image.load("./Assets/pizza.png", "player"), (50, 50))


def player_move(player, key_pressed):
    if key_pressed[K_w]:
        player.y -= STEP


def vehicle_move(vehicle):
    vehicle.x -= STEP


def draw_window(player_surface, player_rect, vehicle_surface, vehicle_rect, ycor):
    pygame.Surface.fill(WINDOW, WHITE)
    # drawing player using image asset and applying rect attributes to the image
    WINDOW.blit(player_surface, player_rect)
    vehicle_rect.y = ycor
    list_of_vehicles.append(vehicle_surface)

    WINDOW.blit(vehicle_surface,
                (vehicle_rect.x, vehicle_rect.y))

    pygame.display.flip()


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

        # Generates random y coordinate for vehicles
        random_position = random.randint(20, HEIGHT - 100)

        # Vehicle stuff
        vehicle_img = random.choice(vehicles)
        vehicle_as_rect = pygame.Surface.get_rect(vehicle_img)

        vehicle_as_rect.x = WIDTH - 100

        player_move(player_as_rect, pygame.key.get_pressed())
        # vehicle_move(vehicle_as_rect)
        draw_window(player_img, player_as_rect,
                    vehicle_img, vehicle_as_rect, random_position)
    pygame.display.quit()


main()
