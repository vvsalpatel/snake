import pygame
from constantes import *
from map import *
from pygame.locals import *
from snake import *


class Game:
    """Game class"""

    def __init__(self):
        self.game_score = 0
        self.game_time = 0

    def start_invisible(self, neural_net=None):
        snake = Snake(neural_net=neural_net)
        map = Map(snake)
        cont = True
        while cont:
            self.game_time += 1
            map.scan()
            snake.AI()
            snake.update()
            map.update()
            if not snake.alive or self.game_time > 300:
                cont = False
                self.game_time = 0
        self.game_score = snake.fitness()
        return self.game_score

    def start_visible(self, playable=False, neural_net=None):
        pygame.init()
        gameWindow = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # Opening game window
        pygame.display.set_caption(WINDOW_TITLE)                          # Title
        snake = Snake(neural_net=neural_net)
        snake.neural_net = Network(shape=[16, 16, 4])
        map = Map(snake)
        update = 0
        cont = True
        while cont:
            pygame.time.Clock().tick(30)
            self.render(gameWindow, map)
            for event in pygame.event.get():
                if event.type == QUIT:
                    cont = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        cont = False
                    if event.key == K_RIGHT:
                        snake.direction = RIGHT
                    elif event.key == K_LEFT:
                        snake.direction = LEFT
                    elif event.key == K_UP:
                        snake.direction = UP
                    elif event.key == K_DOWN:
                        snake.direction = DOWN
            update += 1
            if update > 0:
                update = 0
                if not playable:
                  map.scan()
                  snake.AI()
                snake.update()
                map.update()
            if not snake.alive:
                cont = False
        self.game_score = snake.fitness()
        return self.score

    def render(self, window, map):
        map.render(window)
        pygame.display.flip()