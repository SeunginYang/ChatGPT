import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (400, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tetris')

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the block size and margin
block_size = 20
margin = 5

# Set the initial position of the tetromino
x_pos = window_size[0] // 2
y_pos = 0

# Set the shapes and colors of the tetrominoes
tetrominoes = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 2, 2],
     [2, 2, 0]],
    [[3, 3, 0],
     [0, 3, 3]],
    [[4, 0, 0],
     [4, 4, 4]],
    [[0, 0, 5],
     [5, 5, 5]],
    [[6, 6, 6, 6]],
    [[7, 7],
     [7, 7]]
]
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 255),
    (128, 0, 128)
]

# Set the initial tetromino and rotation
tetromino = random.choice(tetrominoes)
rotation = 0

# Set the falling speed
fall_speed = 500

# Set the game over flag
game_over = False

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while not game_over:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x_pos -= block_size + margin
      elif event.key == pygame.K_RIGHT:
        x_pos += block_size + margin
      elif event.key == pygame.K_UP:
        rotation = (rotation + 1) % len(tetromino)
        tetromino = tetrominoes[tetrominoes.index(tetromino)][rotation]
      elif event.key == pygame.K_DOWN:
        y_pos += block_size + margin
  
  # Update the position of the tetromino
  y_pos += block_size + margin
  
  # Draw the tetromino
  for y, row in enumerate(tetromino):
    for x, block in enumerate(row):
      if block > 0:
        pygame.draw.rect(window, colors[block - 1], (x_pos + x * (block_size + margin), y
