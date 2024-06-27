import pygame
from settings import WHITE, BLACK, CHECKBOX_SIZE

class Checkbox:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.checked = False
        self.checkbox_image = pygame.image.load('checkbox_1.png')
        self.checkbox_image = pygame.transform.scale(self.checkbox_image, CHECKBOX_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        if self.checked:
            screen.blit(self.checkbox_image, (self.rect.x, self.rect.y))
        font = pygame.font.SysFont(None, 20)
        text_surface = font.render(self.label, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 50, self.rect.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def toggle(self):
        self.checked = not self.checked

    def set_state(self, state):
        self.checked = state

    def is_checked(self):
        return self.checked
