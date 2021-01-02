#!/usr/bin/env python
# coding: utf-8

# In[5]:

import pygame

import sys

from plane_sprites import *

from plane_game import *

#SCREEN_RECT = pygame.Rect(0,0,480,700)

class tool(object) :
    
    def __init__(self , image_name) :

        self.image = pygame.image.load(image_name).convert_alpha()

        self.rect = self.image.get_rect()
    
    def update(self , pos , screen) :
        
        self.rect.center = pos
        
        screen.blit(self.image , self.rect)
        
class Botton(tool) :##################################
        
    def __init__(self , image1_name= '',  image2_name = '') :
            
        self.images = (image1_name , image2_name)
            
        super().__init__(image1_name)
        
    def update(self , pos , screen , state) :
            
        super().__init__(self.images[state])
       
        super().update(pos , screen)    
        
        self.state =state   
        
        
class menu(object) :

    def __dead_screen__(self) :

        self.deadimage = tool("./images/OVER.png")
  
        while True :
            
            for event in pygame.event.get() :
        
                if event.type == pygame.QUIT :
                    
                    print('游戏结束')
                    
                    pygame.quit()
            
                    sys.exit()

            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_SPACE]:

                print("跳出循环")

                self.background.update(self.background.rect.center , self.screen)

                self.startbotton.update(self.pos1 , self.screen ,  0)

                self.exitbotton.update(self.pos2 , self.screen , 0)

                
                break
            
            self.deadimage.update(self.background.rect.center , self.screen)

            pygame.display.update()

            print("你死了")
    
    def __init__(self ) :
        
        pygame.init()
        
#        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        
        self.background = tool("./images/background.png")
          
        self.background.update(self.background.rect.center , self.screen)

        self.startbotton = Botton( "./images/START1.png" , "./images/START2.png")#开始按钮
        
        self.pos1 = (SCREEN_RECT.centerx , SCREEN_RECT.centery-self.startbotton.rect.height)
        
        self.startbotton.update(self.pos1 , self.screen , 0)

        self.exitbotton = Botton( "./images/EXIT1.png" , "./images/EXIT2.png")#退出按钮
        
        self.pos2 = (SCREEN_RECT.centerx , SCREEN_RECT.centery+self.exitbotton.rect.height) 

        self.exitbotton.update(self.pos2 , self.screen , 0)

    def update(self) :
        
        while True :
            
            for event in pygame.event.get() :
        
                if event.type == pygame.QUIT :
                    
                    print('游戏结束')
                    
                    pygame.quit()
            
                    sys.exit()
                
            keys_pressed = pygame.key.get_pressed()   
            
                
            if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN] :
            
                print('按下按钮')
            
                self.background.update(self.background.rect.center , self.screen)

                self.startbotton.update(self.pos1 , self.screen ,  (self.startbotton.state+1)%2)

                self.exitbotton.update(self.pos2 , self.screen , (self.startbotton.state+1)%2)

            
            elif keys_pressed[pygame.K_SPACE] :
                
                if self.exitbotton.state :
                    
                    print('游戏退出')
                    
                    pygame.quit()
            
                    sys.exit()
                
                elif self.startbotton.state :
                   ''' self.deadimage = pygame.image.load("./image/OVER.png").convert_alpha()
                    self.deadrect = self.deadimage.get_rect()
                    self.deadrect.center = SCREEN_RECT.center
                    self.screen.blit(self.deadimage , self.deadrect)
                    '''
                   self.game = PlaneGame(self.screen)
                   
                   self.game.start_game()#####################################

                   self.__dead_screen__()
                
            pygame.display.update()
            
startmenu = menu()

startmenu.update()


# In[ ]:





# In[ ]:




