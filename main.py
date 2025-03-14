import pygame

from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def game_loop():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	
	player_one = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
	
	updateable = pygame.sprite.Group(player_one)
	draweable = pygame.sprite.Group(player_one)
	asteroids = pygame.sprite.Group()

	Player.containers = (updateable, draweable)
	Asteroid.containers = (asteroids, updateable, draweable)
	AsteroidField.containers = (updateable)

	asteroidfield_zero = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updateable.update(dt)
	
		for asteroid in asteroids:
			if asteroid.collision_check(player_one) == True:
				print("Game Over!")
				return pygame.QUIT 

		screen.fill(000, rect = None, special_flags = 0)
		
		for obj in draweable:
			obj.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	game_loop()

if __name__ == "__main__":
	main()
