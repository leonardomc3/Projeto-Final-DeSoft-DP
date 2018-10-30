
import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


pygame.init() 

largura = 640
altura = 480

tamanho = 10
pos_x = largura/2
pos_y = largura/2




fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('PyTron')

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x -= 10
            if event.key == pygame.K_RIGHT:
                pos_x += 10
            if event.key == pygame.K_UP:
                pos_y -= 10
            if event.key == pygame.K_DOWN:
                pos_y += 10
                
                
                
        fundo.fill(white)
        pygame.draw.rect(fundo, blue, [pos_x, pos_y, tamanho, tamanho], )
        
    
    pygame.display.update()



pygame.quit()
























