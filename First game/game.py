from ast import While
from re import A
import pygame
pygame.init()

##### NO ANIMATION ######

#Screen size
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

#Game name
pygame.display.set_caption("Game")

class player(object):
    def __init__(self, x, y, width, height):
        #Variables for playable character
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        
        #Variables for Dash
        self.dash_distance = 50
        self.cooldown = False
        self.Direction = 1
        #0, Default | 1, Left | 2, Right | 3, Up | 4, Down
        self.dash_cooldown = pygame.USEREVENT + 1
        #Keys
        self.keys = pygame.key.get_pressed()
        
    def dash(self,win):
        if self.keys[pygame.K_SPACE] and self.cooldown == False:
            self.cooldown = True
            pygame.time.set_timer(self.dash_cooldown, 100)
            
            if self.Direction == 1:
                if self.x > self.dash_distance:
                    self.x -= self.dash_distance
            elif self.Direction == 2:
                if self.x < screenWidth - self.width - self.dash_distance:
                    self.x += self.dash_distance
            elif self.Direction == 3:
                if self.y > self.dash_distance:
                    self.y -= self.dash_distance
            elif self.Direction == 4:
                if self.y < screenHeight - self.height - self.dash_distance:
                    self.y += self.dash_distance
                    
    def movment(self,win):
        self.keys = pygame.key.get_pressed()
    
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a] and  self.x > self.vel:
            self.x -= self.vel
            self.Direction = 1 
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d] and self.x < screenWidth - self.width - self.vel:
            self.x += self.vel
            self.Direction = 2
        if self.keys[pygame.K_UP] or self.keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
            self.Direction = 3
        if self.keys[pygame.K_DOWN] or self.keys[pygame.K_s] and self.y < screenHeight - self.height - self.vel:
            self.y+= self.vel
            self.Direction = 4   
    
    def events(self,win):
        #Check for event
        for event in pygame.event.get():
        #Cooldown for dash
            if event.type == self.dash_cooldown:
                self.cooldown = False
                pygame.time.set_timer(self.dash_cooldown, 0)
            
            if event.type == pygame.QUIT:
                self.run = False                             
                        
                    
#X, Y, Width, Height
iden = player(40, 40, 40, 60)
iden.run = True
while iden.run:
    pygame.time.delay(100)
    
    iden.events(win)
    iden.movment(win)    
    iden.dash(win)    

    #Window color
    win.fill((0, 0, 0))
    #Chracter size & color
    pygame.draw.rect(win, (255, 0, 0), (iden.x, iden.y, iden.width, iden.height))
    pygame.display.update()

pygame.quit()
