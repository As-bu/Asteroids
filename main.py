import pygame

from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
	loop = 0
	while loop == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(000, rect = None, special_flags = 0)
		pygame.display.flip()

def main():
	print("Starting Asteroids!", 
		f"Screen width: {SCREEN_WIDTH}", 
		f"Screen height: {SCREEN_HEIGHT}"
	)
	game_loop()

if __name__ == "__main__":
	main()
