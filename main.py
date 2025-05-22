import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  asteroid_field = AsteroidField()
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    screen.fill("black")
    for drawable_item in drawable:
      drawable_item.draw(screen)
      
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        print("Game over!")
        sys.exit()

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
  main()