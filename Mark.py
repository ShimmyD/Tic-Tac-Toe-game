import pygame
import numpy as np
import tkMessageBox
import math
import collections

class Mark:
    """ Mark class for action of placing a mark on screen and checking for win
        Attributs:
            screen (pygame surface)
            length (int/float) representing radius for a circle or width for a line
            color (tuple) representing color rgb 
            pos (tuple): representing coordinates of the center point of grid on pygame surface when clicking a grid
            pos_rot (tuple): representing new coordinates after rotating the axes for 45 degree
            pos_list (list of tuples): a list of pos 
            pos_rot_list (list of tuples): a list of pos_rot
    """
    def __init__(self,screen,length, color=None,pos=None,pos_rot=None,pos_list=None,pos_rot_list=None):
        self.screen=screen
        if color==None:
            self.color=()
        else:
            self.color=color
        if pos==None:
            self.pos=()
        else:
            self.pos=pos
        self.length=length
        if pos_rot==None:
            self.pos_rot=()
        else:
            self.pos_rot=pos_rot
        if pos_list==None:
            self.pos_list=[]
        else:
            self.pos_list=pos_list
        if pos_rot_list==None:
            self.pos_rot_list=[]
        else:
            self.pos_rot_list=pos_rot_list

    def rotate_around_point_lowperf(self, radians=math.pi/4, origin=(0, 0)):
        """ Function to calculate new coordinates after rotate axes aroud origin (0,0).

            This function is copied from Lyle Scott's github from https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302 

            Args:
                radians (float) degree to rotate axes
                origin (tuple) 
            Returns:
                tuple : new coordinates
        """
        x,y=self.pos
        ox, oy = origin
        qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
        qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)
        self.pos_rot=(qx,qy)
        return self.pos_rot

    def set_center(self):
        """ Function to find center point in a grid when placing a mark in a grid
            Args:
                None
            Returns:
                pos (tuple): center point coordinates of a grid
                pos_list (list of tuples) : a list of pos tuple
                pos_rot_list (list of tuples) : a list of new coordinates of pos after rotate axes 
        """
        center_points=np.array([[100, 300, 500],[100, 300, 500]])
        pos_arr=np.array([[self.pos[0]],[self.pos[1]]])
        idx = np.abs((center_points - pos_arr)).argmin(axis=1)
        center=center_points.flat[idx]
        self.pos=(center[0],center[1])
        self.pos_rot=self.rotate_around_point_lowperf()
        self.pos_list.append(self.pos)
        self.pos_rot_list.append(self.pos_rot)
        return self.pos,self.pos_list,self.pos_rot_list

    def check_game(self):
        """
            function to check if a player won the game
            Args:
                None
            Returns:
                True or False : if a player won, return False to stop the while loop, otherwise True to continue
        """
        ## if there is less than 3 of a type of mark on the pygame surface, don't check
        if len(self.pos_list)<3:  
            return True
        ## if there are three idential x or y center cooridnates of a type of mark, one player has his marks on horizontal or vertical line.
        ##  if there are three idential x or y center cooridnates of a type of mark after rotating axes, one player has his marks on diagonal line.
        elif 3 in [i[1] for i in collections.Counter([i[0] for i in self.pos_list]).most_common()]\
        or 3 in [i[1] for i in collections.Counter([i[1] for i in self.pos_list]).most_common()]\
        or 3 in [i[1] for i in collections.Counter([np.round(i[0],0) for i in self.pos_rot_list]).most_common()]\
        or 3 in [i[1] for i in collections.Counter([np.round(i[1],0) for i in self.pos_rot_list]).most_common()]:
            return False
        else:
            return True


