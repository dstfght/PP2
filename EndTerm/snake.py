import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")


WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

clock = pygame.time.Clock()
FPS = 5

score = 0
level = 2

color = GREEN
block = 15
dx, dy = block, 0
radius = 10

food_x = round(random.randrange(0, SCREEN_WIDTH - block) / 15.0) * 15
food_y = round(random.randrange(0, SCREEN_HEIGHT - block) / 15.0) * 15

wall = [[-1, -1],[round(random.randrange(0, SCREEN_WIDTH - block) / 15.0) * 15, round(random.randrange(0, SCREEN_HEIGHT - block) / 15.0) * 15]]

body = [[60, 105], [75, 105], [90, 105]]

while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              dx, dy = block, 0
          if event.key == pygame.K_LEFT:
              dx, dy = -block, 0
          if event.key == pygame.K_UP:
              dx, dy = 0, -block
          if event.key == pygame.K_DOWN:
              dx, dy = 0, block
  
  if score == 5:
    level += 1
    score = 0
    wall.append([round(random.randrange(0, SCREEN_WIDTH - block) / 15.0) * 15, round(random.randrange(0, SCREEN_HEIGHT - block) / 15.0) * 15])
  
  for i in range(len(body) - 1, 0, -1):
      body[i][0] = body[i - 1][0]
      body[i][1] = body[i - 1][1]

  body[0][0] += dx
  body[0][1] += dy
  
  if body[0][0] >= SCREEN_WIDTH:
    body[0][0] = 0
  if body[0][1] >= SCREEN_HEIGHT:
    body[0][1] = 0
  if body[0][0] < 0:
    body[0][0] = SCREEN_WIDTH
  if body[0][1] < 0:
    body[0][1] = SCREEN_HEIGHT
    
  if body[0][0] == food_x and body[0][1] == food_y :
    body.append([0, 0])
    score += 1
    food_x = round(random.randrange(0, SCREEN_WIDTH) / 15.0) * 15
    food_y = round(random.randrange(0, SCREEN_HEIGHT) / 15.0) * 15
  
  for i in range(1, level):
    if i <= level / 2:
      if wall[i][0] <= body[0][0] <= (wall[i][0] + block) and wall[i][1] <= body[0][1] <= (wall[i][1] + 90):
        running = False
    else:
      if wall[i][0] <= body[0][0] <= (wall[i][0] + 90) and wall[i][1] <= body[0][1] <= (wall[i][1] + block):
        running = False
  
  screen.fill(WHITE)
  
  for i in range(1, level):
    if i <= level / 2:
      pygame.draw.rect(screen, BLACK, [wall[i][0], wall[i][1], block, 90])
    else:
      pygame.draw.rect(screen, BLACK, [wall[i][0], wall[i][1], 90, block])
  
  pygame.draw.circle(screen, GREEN, [food_x, food_y], radius)

  for i, point in enumerate(body):
    color = RED if i == 0 else BLUE
    pygame.draw.circle(screen, color, point, radius)
  
  
  
  pygame.display.flip()
  
  clock.tick(FPS + 2 * (level - 1))

pygame.quit()