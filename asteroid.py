from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        

    def split(self,group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_angle1 = self.velocity.rotate(random_angle)
            new_angle2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            one = Asteroid(self.position.x, self.position.y, new_radius)
            one.velocity = new_angle1 * 1.2
            two = Asteroid(self.position.x, self.position.y, new_radius)
            two.velocity = new_angle2 * 1.2
            group.add(one)
            group.add(two)

        


