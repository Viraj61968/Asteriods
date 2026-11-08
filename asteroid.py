import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen: pygame.Surface) -> None:
        screen = pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        CircleShape.update(self,dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.kill()
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_vector = self.velocity.rotate(angle)
        second_new_vector = new_vector.rotate(-angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        one_ast_obj = Asteroid(self.position.x,self.position.y,new_radius)
        sec_ast_obj = Asteroid(self.position.x,self.position.y,new_radius)
        one_ast_obj.velocity = new_vector * 1.2
        sec_ast_obj.velocity = second_new_vector * 1.2
