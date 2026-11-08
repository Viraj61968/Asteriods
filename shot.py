import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self,x,y)-> None:
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen: pygame.Surface) -> None:
        screen = pygame.draw.circle(screen,"white",self.position,SHOT_RADIUS,LINE_WIDTH)

    def update(self, dt: float) -> None:
        CircleShape.update(self,dt)
