from turtle import circle
import pygame
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

BK_COLOR = (255,204,204)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hila First Game")
bk_image = pygame.image.load("bk_img.jpg")

clock= pygame.time.Clock()
circle_x = 10
circle_y= WINDOW_H/2
x_step = 10

play = True
while play:
  # screen.fill(BK_COLOR)
  screen.blit(bk_image,(0,0))
  pygame.draw.circle(screen,(120,89,255),(circle_x , circle_y  ),10)


  circle_x +=x_step
  if circle_x > WINDOW_W:
    x_step = -10
  if circle_x<0:
    x_step=10
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
  clock.tick(20)      

pygame.quit()

