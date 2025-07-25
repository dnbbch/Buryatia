"""
Система камеры для слежения за спрайтами и плавного перемещения (видовая область).
"""

import pygame
from typing import Tuple, Optional, Union
from .sprite import AnimatedSprite


class Camera:
    """Камера, которая следует за спрайтами и управляет областью просмотра."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0.0
        self.y = 0.0
        self.target: Optional[AnimatedSprite] = None
        self.smooth_follow = True
        self.follow_speed = 5.0

    def follow(self, sprite: AnimatedSprite, smooth: bool = True) -> None:
        """Установить спрайт, за которым нужно следовать."""
        self.target = sprite
        self.smooth_follow = smooth

    def update(self, dt: float) -> None:
        """Обновить позицию камеры."""
        if self.target:
            target_pos = self.target.get_position()
            target_x = target_pos[0] - self.width // 2
            target_y = target_pos[1] - self.height // 2

            if self.smooth_follow:
                self.x += (target_x - self.x) * self.follow_speed * dt
                self.y += (target_y - self.y) * self.follow_speed * dt
            else:
                self.x = target_x
                self.y = target_y

    def get_offset(self) -> Tuple[int, int]:
        """Получить смещение камеры для отрисовки."""
        return (int(-self.x), int(-self.y))
