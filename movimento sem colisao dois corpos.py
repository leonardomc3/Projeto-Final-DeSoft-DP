from pygame.locals import *
import pygame
import time


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)




class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        
        return False




class Player:
    x = [0]
    y = [100]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        if self.direction!= 1:
            self.direction = 0
            
        
 
    def moveLeft(self):
        if self.direction != 0:
            self.direction = 1
        
 
    def moveUp(self):
        if self.direction != 3:
            self.direction = 2
        
 
    def moveDown(self):
        if self.direction != 2:  
            self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 


class Player2:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[3] = 20
       self.x[4] = 44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        if self.direction!= 1:
            self.direction = 0
            
        
 
    def moveLeft(self):
        if self.direction != 0:
            self.direction = 1
        
 
    def moveUp(self):
        if self.direction != 3:
            self.direction = 2
        
 
    def moveDown(self):
        if self.direction != 2:  
            self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 



 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    player2 = 0
    _menu = True
    
    
    
    def texto(self, msg, color, tam, x, y):
        font = pygame.font.SysFont(None, tam)
        texto1 = font.render(msg, True, color)
        self._display_surf.blit(texto1, [x, y])
    
    
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        
        self.game = Game()
        self.player = Player(3) 
        self.player2 = Player2(3) 
        
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("bola-25X25.png").convert()
        #self._apple_surf = pygame.image.load("bola-25X25.png").convert()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        self.player2.update()
        
        for i in range(0,self.player.length):
            if self.game.isCollision(self.player2.x[0],self.player2.y[0],self.player.x[i], self.player.y[i],44):
                self._running = False
        for i in range(0,self.player2.length):
            if self.game.isCollision(self.player2.x[i],self.player2.y[i],self.player.x[0], self.player.y[0],44):
                self._running = False
       
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.player2.draw(self._display_surf, self._image_surf)
        pygame.display.flip()
        
        
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            while (self._menu):
                
                self._display_surf.fill(black)
                self.texto('SNAKE 2.0', green, 80, 260, 30)
                pygame.draw.rect(self._display_surf, white, [330, 320, 135, 30])
                self.texto('Jogar (J)', black, 30, 335, 325)
                pygame.draw.rect(self._display_surf, white, [330, 365, 135, 30])
                self.texto('Opções (O)', black, 30, 335, 370)
                pygame.draw.rect(self._display_surf, white, [330, 410, 135, 30])
                self.texto('Sair (S)', black, 30, 335, 415)
                pygame.display.update()
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            self._menu = False
                            self._running = False
                        if event.key == pygame.K_j:
                            self._menu = False
                        if event.key == pygame.K_o:
                            self._menu = False          
                            
                            
                            
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[pygame.K_RIGHT]):
                self.player.moveRight()
 
            if (keys[pygame.K_LEFT]):
                self.player.moveLeft()
 
            if (keys[pygame.K_UP]):
                self.player.moveUp()
 
            if (keys[pygame.K_DOWN]):
                self.player.moveDown()
            
            
            if (keys[pygame.K_d]):
                self.player2.moveRight()
 
            if (keys[pygame.K_a]):
                self.player2.moveLeft()
 
            if (keys[pygame.K_w]):
                self.player2.moveUp()
 
            if (keys[pygame.K_s]):
                self.player2.moveDown()
 
    

            if (keys[pygame.K_ESCAPE]):
                self._running = False
            
 
            self.on_loop()
            self.on_render()
            time.sleep (50.0 / 1000.0);
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
    
pygame.quit()
