import math
from enum import Enum

class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)

class player_camera():
    def __init__(self):

        self.dir_x, self.dir_y = -1, 0  # Initially facing 'north'
        self.plane_x, self.plane_y =  0, 0.66 # Camera plane
        self.player_pos_x, self.player_pos_y = 22,12
        self.rotate = 0.06
        self.walkspeed = 0.1

    def move(self,key,world_map): # Take key input and change values. 
        
            self.key = key

            if key == 87:    
                   
                    if(world_map[int(self.player_pos_x + self.dir_x * self.walkspeed )][int(self.player_pos_y)] == False):
                       self.player_pos_x += self.dir_x *  self.walkspeed
                    if(world_map[int(self.player_pos_x)][int(self.player_pos_y + self.dir_y *  self.walkspeed)] == False) :
                       self.player_pos_y += self.dir_y *  self.walkspeed
                   
                    
            if key == 83:
                    if(world_map[int(self.player_pos_x - self.dir_x *  self.walkspeed)][int(self.player_pos_y)] == False):
                       self.player_pos_x -= self.dir_x *  self.walkspeed
                    if(world_map[int(self.player_pos_x)][int(self.player_pos_y - self.dir_y *  self.walkspeed)] == False) :
                        self.player_pos_y -= self.dir_y *  self.walkspeed
                   
                     
            if(key == 65):
                    oldDirX = self.dir_x
                    self.dir_x = self.dir_x * math.cos(self.rotate) - self.dir_y * math.sin(self.rotate)
                    self.dir_y = oldDirX * math.sin(self.rotate) + self.dir_y * math.cos(self.rotate)
                    oldPlaneX = self.plane_x
                    self.plane_x = self.plane_x * math.cos(self.rotate) - self.plane_y * math.sin(self.rotate)
                    self.plane_y = oldPlaneX * math.sin(1*self.rotate) + self.plane_y * math.cos(-1*self.rotate)
                   

                # rotate to the left
            if(key == 68):
                    # both camera direction and camera plane must be rotated
                    oldDirX = self.dir_x
                    self.dir_x = self.dir_x * math.cos(-1*self.rotate) - self.dir_y * math.sin(-1*self.rotate)
                    self.dir_y = oldDirX * math.sin(-1*self.rotate) + self.dir_y * math.cos(-1*self.rotate)
                    oldPlaneX = self.plane_x
                    self.plane_x = self.plane_x * math.cos(-1*self.rotate) - self.plane_y * math.sin(-1*self.rotate)
                    self.plane_y = oldPlaneX * math.sin(-1*self.rotate) + self.plane_y * math.cos(-1*self.rotate)


    def normalize(self):
        angle = math.degrees(math.atan2(self.dir_y, self.dir_x)) % 360

        #could add up to north north north west and etc
        if 30 <= angle < 135:
            return Direction.NORTH
        elif angle < 45 or angle >= 315:
            return Direction.EAST
        elif 225 <= angle < 315:
            return Direction.SOUTH
        elif 135 <= angle < 225:
            return Direction.WEST
        else:
            return None