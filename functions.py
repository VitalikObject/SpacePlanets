import random
import math
import pygame
from planet import Planet
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def check_collision(planet1, planet2):
    dx = planet1.x - planet2.x
    dy = planet1.y - planet2.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance <= (planet1.radius + planet2.radius)

def remove_collided_planets(planets):
    collided_planets = []
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            if check_collision(planets[i], planets[j]):
                collided_planets.extend([planets[i], planets[j]])

    for planet in collided_planets:
        if planet in planets:
            planets.remove(planet)

def add_planet(planets):
    x, y = pygame.mouse.get_pos()
    radius = random.randint(1, 3)
    speed = random.randint(1, 3)
    angle = random.uniform(0, 2 * math.pi)
    planets.append(Planet(x, y, radius, speed, angle))

def make_planets(planets):
    if len(planets) >= 5 and len(planets) % 5 == 0:
        group_size = len(planets) // 5 
        groups = [planets[i*group_size:(i+1)*group_size] for i in range(5)]
        for group in groups:
            disperse_group(group)
    elif len(planets) >= 4 and len(planets) % 4 == 0 and len(planets) // 4 <= 4:
        pass

def disperse_group(group):
    if not group:
        return

    counselor_index = random.randint(0, len(group) - 1)
    counselor_planet = group.pop(counselor_index)
    counselor_planet.speed = 0

    if len(group) <=20:
        radius = 10
    elif len(group) > 20 and len(group) <= 50:
        radius = 30
    elif len(group) > 50 and len(group) <= 100:
        radius = 60
    elif len(group) > 100 and len(group) <= 300:
        radius = 90
    else:
        radius = 100
    counselor_planet.x = max(min(counselor_planet.x, SCREEN_WIDTH - radius), radius)
    counselor_planet.y = max(min(counselor_planet.y, SCREEN_HEIGHT - radius), radius)

    num_planets = len(group)
    angle_increment = 2 * math.pi / num_planets

    for i, planet in enumerate(group):
        angle = i * angle_increment
        planet.target_x = counselor_planet.x + radius * math.cos(angle)
        planet.target_y = counselor_planet.y + radius * math.sin(angle)
        planet.speed = 0

def disperse_planets(planets):
    for planet in planets:
        planet.target_x = random.randint(0, SCREEN_WIDTH)
        planet.target_y = random.randint(0, SCREEN_HEIGHT)
        planet.speed = random.uniform(1, 2)
        planet.angle = random.uniform(0, 7 * math.pi)

def mouse_paint(planets, drug_mouse_if_collided_box_flag):
    if drug_mouse_if_collided_box_flag:
        disperse_planets(planets)
        add_planet(planets)
