import pygame
import random
import math


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.font.init()  

my_font = pygame.font.SysFont('Comic Sans MS', 30)


class bar:
	def __init__(self,x):
		self.x = x
		self.y = 320
		self.height = 80

class ball:
	cx = 640
	cy = 360
	radius = 8
	speed = 5
	def __init__(self):
		self.angle = random.random()*(math.pi/2.95837)
		self.speedx = self.speed * math.cos(self.angle)
		self.speedy = self.speed * math.sin(self.angle)



bar1 = bar(0)
bar2 = bar(1280)
myBall = ball()
score1 = 0
score2 = 0



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #GRAPHICS
    screen.fill("black")
    pygame.draw.line(screen,"white",(bar1.x,bar1.y),(bar1.x,bar1.y+bar1.height),20)
    pygame.draw.line(screen,"white",(bar2.x,bar2.y),(bar2.x,bar2.y+bar2.height),20)
    pygame.draw.circle(screen,"white",(myBall.cx,myBall.cy),myBall.radius,myBall.radius)
    
    

    score_text1 = my_font.render(f'Score 1: {score1}', False, (255, 255, 255))
    screen.blit(score_text1, (50, 50))
    score_text2 = my_font.render(f'Score 2: {score2}', False, (255, 255, 255))
    screen.blit(score_text2, (1100, 50))
    game_over = my_font.render(f'Game Over',False,"WHITE")
    #LOOP
    myBall.cx += myBall.speedx
    myBall.cy += myBall.speedy
    if myBall.cy >= 720 or myBall.cy <= 0:
    	myBall.speedy *= -1
    if myBall.cy <= bar2.height + bar2.y and bar2.height < myBall.cy and myBall.cx +myBall.radius >= bar2.x and myBall.speedx != 0 and myBall.speedy != 0:
    	myBall.speedx *= -1
    	score2 += 1
    if myBall.cy <= bar1.height + bar1.y and bar1.height < myBall.cy and myBall.cx - myBall.radius <= bar1.x and myBall.speedx != 0 and myBall.speedy != 0:
    	myBall.speedx *= -1
    	score1 += 1

    if myBall.cx >=1280 or myBall.cx <= 0:
        screen.blit(game_over,(600,360))
        myBall.speedx = 0
        myBall.speedy = 0
 	

   	# CONTROLS
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_UP]:
    	if 0 < bar2.y:
    		bar2.y -= 5
    if keys[pygame.K_w]:
    	if 0 < bar1.y:
    		bar1.y -= 5
    if keys[pygame.K_DOWN]:
    	if  bar2.y<640:
    		bar2.y += 5
    if keys[pygame.K_s]:
    	if  bar1.y<640:
    		bar1.y += 5

    pygame.display.flip()

    clock.tick(60)

pygame.quit()