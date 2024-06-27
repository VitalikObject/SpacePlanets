import pygame
import os
from settings import *
from planet import Planet
from checkbox import Checkbox
from functions import check_collision, remove_collided_planets, add_planet, make_planets, disperse_planets, mouse_paint

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PlanetMovies")

custom_font = pygame.font.Font(FONT_PATH, FONT_SIZE)

planets = []

checkbox_remove = Checkbox(20, 19, 15, 15, "REMOVE PLANET IF COLLIDED")
checkbox_make = Checkbox(20, 35, 15, 15, "MAKE PLANETS")
checkbox_drag = Checkbox(20, 53, 15, 15, "DRUG MOUSE")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if checkbox_remove.is_clicked(mouse_pos):
                    checkbox_remove.toggle()
                    checkbox_make.set_state(False)
                    checkbox_drag.set_state(False)
                elif checkbox_make.is_clicked(mouse_pos):
                    checkbox_make.toggle()
                    checkbox_remove.set_state(False)
                    checkbox_drag.set_state(False)
                elif checkbox_drag.is_clicked(mouse_pos):
                    checkbox_drag.toggle()
                    checkbox_remove.set_state(False)
                    checkbox_make.set_state(False)
                else:
                    add_planet(planets)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and checkbox_make.is_checked():
                disperse_planets(planets)

    screen.fill(BLACK)

    for planet in planets:
        if checkbox_make.is_checked():
            planet.move_towards_target()
        planet.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        planet.draw(screen)

    text_surface = custom_font.render(f"AMOUNT OF PLANETS: {len(planets)}", True, WHITE)
    screen.blit(text_surface, (5, 5))

    checkbox_remove.draw(screen)
    checkbox_make.draw(screen)
    checkbox_drag.draw(screen)

    if checkbox_remove.is_checked():
        remove_collided_planets(planets)
    if checkbox_make.is_checked():
        make_planets(planets)
    if checkbox_drag.is_checked():
        mouse_paint(planets, checkbox_drag.is_checked())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
