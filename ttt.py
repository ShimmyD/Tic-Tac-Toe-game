import pygame
import numpy as np
import tkMessageBox
import math
import collections
from Mark import Mark

class Circle(Mark):
    """
        Circle class for creating a circle mark 
    """
    def __init__(self,screen,length, color=None,pos=None,pos_rot=None,pos_list=None,pos_rot_list=None):
        Mark.__init__(self,screen, length,color,pos,pos_rot,pos_list,pos_rot_list)
    def draw_mark(self):
        """
            function to show circle mark on pygame surface after clicking on the grids 
            Args:
                None
            Returns:
                None
        """
        self.pos,self.pos_list,self.pos_rot_list_=self.set_center()
        pygame.draw.circle(self.screen, self.color, self.pos, self.length)
        pygame.display.update()

class Cross(Mark):
    """
        Cross class for creating a cross mark
    """
    def __init__(self,screen,length, color=None,pos=None,pos_rot=None,pos_list=None,pos_rot_list=None):
        Mark.__init__(self,screen, length,color,pos,pos_rot,pos_list,pos_rot_list)

    def draw_mark(self):
        """
            function to show cross mark on pygame surface after clicking on the grids
            Args:
                None
            Returns:
                None
        """
        self.pos,self.pos_list,self.pos_rot_list_=self.set_center()
        pygame.draw.line(self.screen, self.color, self.pos, (self.pos[0]+45, self.pos[1]+45), self.length)
        pygame.draw.line(self.screen, self.color, self.pos, (self.pos[0]+45, self.pos[1]-45), self.length)
        pygame.draw.line(self.screen, self.color, self.pos, (self.pos[0]-45, self.pos[1]+45), self.length)
        pygame.draw.line(self.screen, self.color, self.pos, (self.pos[0]-45, self.pos[1]-45), self.length)
        pygame.display.update()
    
def drawGrid():
    """
        function to draw grid lines  on pygame surface
        Args:
            None
        Returns:
            None
    """
    blockSize = 200 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)

          
def main():
    global BLACK,WINDOW_WIDTH,WINDOW_HEIGHT,count,screen
    BLACK = (0, 0, 0)
    Green = (208, 240, 192)
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    count=1

    pygame.init()
    screen=pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    pygame.display.set_caption('Tic-Tac-Toe')
    screen.fill(Green)
    drawGrid()
    pygame.display.update()
    circle=Circle(screen,50,BLACK,None,None,None,None)
    cross=Cross(screen,5,BLACK,None,None,None,None)

    running=True
    while running:
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                ## alternate between two plays. if  count is a even number, circle plays, cross plays 
                if count % 2 == 0:
                    circle.pos=pos
                    circle.draw_mark()
                    running=circle.check_game()
                    
                    if running==False:
                        ## if game over, popup window
                        tkMessageBox.showinfo('Game over','Circle won, Cross lost.')
                        # restart = input('do you want to restart Y/N?')
                        # if restart == 'N':
                        #     break
                        # elif restart == 'Y':
                        #     continue
                                        
                else:
                    cross.pos=pos
                    cross.draw_mark()
                    print('pos_list:',cross.pos_list)
                    print('pos_rot:',cross.pos_rot_list)
                    running=cross.check_game()
                    if running==False:
                        tkMessageBox.showinfo('Game over','Cross won,Circle lost')

                count=count+1
        pygame.display.update()

main()