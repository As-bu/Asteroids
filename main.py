import pygame

from constants import *
from player import Player

def game_loop():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	player_one = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		player_one.update(dt)
		screen.fill(000, rect = None, special_flags = 0)
		player_one.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	game_loop()

if __name__ == "__main__":
	main()
