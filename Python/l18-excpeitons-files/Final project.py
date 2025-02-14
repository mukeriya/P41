import time
import pygame
from random import choice

width = int(input('Enter the width of the maze: '))
height = int(input('Enter the height of the maze: '))
resolution = width + 2, height + 2
tile = int(input('Enter the tile size: '))
cols = width // tile
rows = height // tile
maze_done = False
stack_was_last = False

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.visited_for_exit = False

    def draw_current_cell(self):
        x = self.x * tile
        y = self.y * tile
        pygame.draw.rect(screen, pygame.Color('red'), (x + 2, y + 2, tile - 2, tile - 2))

    def draw_normal_cell(self):
        x = self.x * tile
        y = self.y * tile
        pygame.draw.rect(screen, pygame.Color('black'), (x + 2, y + 2, tile - 2, tile - 2))

    def draw_exit(self):
        x = self.x * tile
        y = self.y * tile
        pygame.draw.rect(screen, pygame.Color('lightgreen'), (x + 2, y + 2, tile - 2, tile - 2))

    def draw(self):
        x = self.x * tile
        y = self.y * tile
        if self.visited:
            pygame.draw.rect(screen, pygame.Color('black'), (x, y, tile, tile))

        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('green'), (x, y), (x + tile, y,), 2)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('green'), (x + tile, y), (x + tile, y + tile,), 2)
        if self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('green'), (x + tile, y + tile), (x, y + tile,), 2)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('green'), (x, y + tile), (x, y,), 2)

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return cell_grid[find_index(x, y)]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        return choice(neighbors) if neighbors else False

    def check_neighbors_for_exit(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited_for_exit:
            if not top.walls['bottom']:
                neighbors.append(top)
        if right and not right.visited_for_exit:
            if not right.walls['left']:
                neighbors.append(right)
        if bottom and not bottom.visited_for_exit:
            if not bottom.walls['top']:
                neighbors.append(bottom)
        if left and not left.visited_for_exit:
            if not left.walls['right']:
                neighbors.append(left)

        return choice(neighbors) if neighbors else False


def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


cell_grid = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = cell_grid[0]
stack = []
potential_exits = [cell for cell in cell_grid if cell.x == cols - 1 or cell.y == rows - 1]
exit = choice(potential_exits)

while not maze_done:
    screen.fill(pygame.Color('gray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in cell_grid]
    current_cell.visited = True
    current_cell.draw_current_cell()
    exit.draw_exit()

    next_cell = current_cell.check_neighbors()

    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell

    elif stack:
        current_cell = stack.pop()

    pygame.display.flip()
    clock.tick(50)
    if current_cell == cell_grid[0]:
        maze_done = True

current_cell = cell_grid[0]
stack = []

maze_ready_for_solving = False

while not maze_ready_for_solving:
    user_input = input('Do you want it to be solved automatically')
    if user_input == 'Yes':
        maze_ready_for_solving = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    current_cell.visited_for_exit = True
    if not stack_was_last:
        current_cell.draw_current_cell()
    next_cell = current_cell.check_neighbors_for_exit()

    if next_cell:
        next_cell.visited_for_exit = True
        stack.append(current_cell)
        current_cell = next_cell
        stack_was_last = False
    elif stack:
        stack_was_last = True
        current_cell = stack.pop()
        current_cell.draw_normal_cell()

    if current_cell == exit:
        time.sleep(10)
        print('Exit found')
        break

    pygame.display.flip()
    clock.tick(100)
