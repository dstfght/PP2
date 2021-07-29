import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lion")



YELLOW = (255, 255, 102)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

clock = pygame.time.Clock()
FPS = 30

block = 20
x, y = 300, 300
dx, dy = 0, 0
bad = [[0, 0],[100, 0]]
good = [[200, SCREEN_HEIGHT],[300, SCREEN_HEIGHT]]
score = 0

score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])

while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              x += block
          if event.key == pygame.K_LEFT:
              x -= block
          if event.key == pygame.K_UP:
              y -= block
          if event.key == pygame.K_DOWN:
              y += block
  
  
  screen.fill(WHITE)
  
  Your_score(score)
  
  if pygame.time.get_ticks() % 15 == 0:
    bad.append([round(random.randrange(0, SCREEN_WIDTH - block) / 20.0) * 20, 0])
    
  if pygame.time.get_ticks() % 25 == 0:
    good.append([round(random.randrange(0, SCREEN_WIDTH - block) / 20.0) * 20, SCREEN_HEIGHT]) 
  
  pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
  
  for i in range(len(bad)):
    if bad[i - 1][0] == x and bad[i - 1][1] == y:
      score -= 1
      bad.pop(i - 1)
  
  for i in range(len(bad)):
    bad[i][1] += block / 4
    pygame.draw.rect(screen, RED, [bad[i][0], bad[i][1], 20, 20])
    
  for i in range(len(good)):
    if good[i - 1][0] == x and good[i - 1][1] == y:
      score += 1
      good.pop(i - 1)
  
  for i in range(len(good)):
    good[i][1] -= block / 5
    pygame.draw.rect(screen, GREEN, [good[i][0], good[i][1], 20, 20])
  
  
  pygame.display.flip()
  
  clock.tick(FPS)

pygame.quit()