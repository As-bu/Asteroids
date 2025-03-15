import pygame

from constants import *
from player import Player, Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def game_loop():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	destroyed_asteroids = 0

	player_one = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
	
	updateable = pygame.sprite.Group(player_one)
	draweable = pygame.sprite.Group(player_one)
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updateable, draweable)
	Asteroid.containers = (asteroids, updateable, draweable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, draweable)

	asteroidfield_zero = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updateable.update(dt)
	
		for asteroid in asteroids:
			if asteroid.collision_check(player_one) == True:
				print("Game Over!")
				print(f"You destroyed {destroyed_asteroids} Asteroids")
				if destroyed_asteroids >= 10:
					print("Good Job!")
				else:
					print("Womp Womp")

				return pygame.QUIT

		for asteroid in asteroids:
			for obj in shots:
				if asteroid.collision_check(obj):
					obj.kill()
					asteroid.split()
					destroyed_asteroids += 1

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
