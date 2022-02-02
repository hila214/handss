
import pygame

# screen size 
WINDOW_W = 1000
WINDOW_H = 700
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
laser_list = []
play = True
score = 0


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

# www.pngaaa.com
bk_image = pygame.image.load("space.jpg")
ship_image = pygame.image.load("ship.png")
ship_image = pygame.transform.scale(ship_image, (50, 80)) 
laser_image = pygame.image.load("laser.jpg")
laser_image = pygame.transform.scale(laser_image, (10, 20)) 

pygame.font.init()  
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def is_laser_hit(laser_pos):
  return abs(laser_pos[0]-circle_x) <50 and abs(laser_pos[1]-circle_y) <50 


def print_lasers():
  for i in range(len(laser_list)):
    global score
    global circle_x
    laser = laser_list[i]
    screen.blit(laser_image,(laser[0],laser[1]))
    laser_list[i] = [laser[0],laser[1]-30]
    if is_laser_hit(laser):
      score += 1
      circle_x = 0 




if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])




clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
ship_x = WINDOW_W /2
ship_y = WINDOW_H - 80

circle_x_step = 10
x_step = 10
laser_list = []
play = True

SOUND_FILLE = "musich.mp3"
GON_SHOT= "sound.mp3"
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILLE)
pygame.mixer.music.load(GON_SHOT)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(SOUND_FILLE)) 


# laser_list = [[121,780],[171,780]]
# i=1
# l=[171,10]
# l[0] = 171
# l[1] = 10


# prints all the laser on the screen
def print_lasers():
  for i in range(len(laser_list)):
    l = laser_list[i]
    screen.blit(laser_image,(l[0],l[1]))
    laser_list[i] = [l[0],l[1]-30]

  if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])




while play:
  screen.blit(bk_image,(0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ship_x -= x_step
      if event.key == pygame.K_RIGHT:
        ship_x += x_step
      if event.key == pygame.K_SPACE:
        laser_list.append([ship_x+21,ship_y])
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(GON_SHOT))


  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),20)

  textsurface = myfont.render('score points:', False, (255, 255, 255))
  print_lasers()
  screen.blit(textsurface,(0,0))

  circle_x +=circle_x_step
  if circle_x > WINDOW_W:
    circle_x_step = -10
  if circle_x <0 :
    circle_x_step = 10
  
  pygame.display.flip()


  clock.tick(10)

pygame.quit()