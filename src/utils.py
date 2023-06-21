import random

import pygame

from constants import IMG_PATH, SOUNDS_PATH


def fetch_image(img_name: str):
    return pygame.image.load(IMG_PATH / img_name)


def fetch_sound(sound_name: str):
    return pygame.mixer.Sound(SOUNDS_PATH / sound_name)


class Image:

    def __init__(
            self,
            img_name: str
        ):
        self.img = fetch_image(img_name)
        self.rect = self.img.get_rect()
        self.direction_x = 1
        self.direction_y = 1
        self.random_x = 1
        self.random_y = 1
        self._choices = [-1.25,-1.5,-2,1.25,1.5,2]

    def reset_position(self, screen: pygame.Surface):
        self.rect.centerx = screen.get_width() / 2
        self.rect.centery = screen.get_height() / 2

    def change_direction_x(self, x: float):
        self.rect.centery = x
        self.direction_x *= -1
        self.random_x = random.choice(self._choices)

    def change_direction_y(self, y: float):
        self.rect.centery = y
        self.direction_y *= -1
        self.random_y = random.choice(self._choices)

    def move(self, rt: float):
        self.rect.centery += self.direction_y * 300 * rt * self.random_y
        self.rect.centerx += self.direction_x * 300 * rt * self.random_x

    def bound_image(
        self,
        ymin: int = 100,
        ymax: int = 620,
        xmin: int = 100,
        xmax: int = 1180,
    ):
        """Ensure image stays within screen bounds by changing direction."""
        if self.rect.centery <= ymin:
            self.change_direction_y(ymin)
        if self.rect.centery > ymax:
            self.change_direction_y(ymax)
        if self.rect.centerx < xmin:
            self.change_direction_x(xmin)
        if self.rect.centerx > xmax:
            self.change_direction_x(xmax)
