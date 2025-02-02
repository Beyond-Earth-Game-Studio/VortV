import math
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem

class RenderEngine():

    def __init__(self, screen_width, screen_height, textures, world_map, camera, viewport, bg):
        super().__init__()
        
        # init class variables
        self.bg = bg
        self.camera = camera
        self.viewport = viewport
        self.world_map = world_map
        self.ceiling_and_floor = False
        self.screen_width = screen_width
        self.screen_height = screen_height

        # create buffer
        self.buffer = QImage(screen_height, screen_width, QImage.Format_ARGB32)
        self.buffer_bits = self.buffer.bits()

        # texture setup
        self.textures = textures
        self.texWidth = self.textures[0].width()
        self.texHeight = self.textures[0].height()
    
    def tick_frame(self):
        
        self.buffer.fill("#00000000")
        self.render() # update the buffer
        pixmap = QPixmap.fromImage(self.buffer)
        pixmap = pixmap.scaled(700,400)
        
        bg = self.bg.scaled(700,600)
        
        fg = QGraphicsPixmapItem(pixmap)
        fg.setOffset(0,200)
        fg = QGraphicsPixmapItem(pixmap)
        fg.setOffset(0,200)
        #viewport.scene().fuckFish()
        return(fg,bg)
        
    def render(self):
            #FLOOR CASTING
            if (self.ceiling_and_floor == True):

                for y in range(int(self.screen_height) ):

                    p = y - self.screen_height / 2
                    posZ = 0.5 * self.screen_height
                    if p == 0:
                        continue
                    rowDistance = posZ / (p)

                    floorStepX = (rowDistance * (self.camera.dir_x + self.camera.plane_x - self.camera.dir_x + self.camera.plane_x)) / self.screen_width
                    floorStepY = (rowDistance * (self.camera.dir_y + self.camera.plane_y - self.camera.dir_y + self.camera.plane_y)) / self.screen_width

                    floorX = self.camera.player_pos_x + rowDistance * (self.camera.dir_x - self.camera.plane_x)
                    floorY = self.camera.player_pos_y + rowDistance * (self.camera.dir_y - self.camera.plane_y)

                    for x in range(self.screen_width):
                        self.buffer_bits = self.buffer.bits()
                        cellX, cellY = int(floorX), int(floorY)
                        tx, ty = int(self.texWidth * (floorX - cellX)) % self.texWidth, int(self.texHeight * (floorY - cellY)) % self.texHeight

                        floorX += floorStepX
                        floorY += floorStepY

                        # Using constBits to access texture pixels, pre process more
                        floor_texture = self.textures[3]  # Texture index for the floor
                        cell_texture = self.textures[6]
                        
                        # Calculating byte index (greatest coder alive fr)
                        tex_index = (ty * floor_texture.bytesPerLine() + tx * 4)
                        color = floor_texture.constBits()[tex_index:tex_index + 4]
                        color2 = cell_texture.constBits()[tex_index:tex_index + 4]

                        buffer_index = ((self.screen_height - y - 1) * self.screen_width + x) * 4
                        self.buffer_bits[buffer_index:buffer_index + 4] = color

                        buffer_index = ((y) * self.screen_width + x) * 4
                        self.buffer_bits[buffer_index:buffer_index + 4] = color2
                   
            #RENDER WALLS!
            for x in range(self.screen_width):

                self.camera_x = 2 * x / self.screen_width - 1
                ray_dir_x = self.camera.dir_x + self.camera.plane_x * self.camera_x
                ray_dir_y = self.camera.dir_y + self.camera.plane_y * self.camera_x

                map_x = int(self.camera.player_pos_x)
                map_y = int(self.camera.player_pos_y)

                delta_dist_x = abs(1 / ray_dir_x + 0.00000000001)
                delta_dist_y = abs(1 / (ray_dir_y + 0.0000000001))

                hit = 0
                side = 0

                if ray_dir_x < 0:
                    step_x = -1
                    side_dist_x = (self.camera.player_pos_x - map_x) * delta_dist_x

                else:
                    step_x = 1
                    side_dist_x = (map_x + 1.0 - self.camera.player_pos_x) * delta_dist_x

                if ray_dir_y < 0:
                    step_y = -1
                    side_dist_y = (self.camera.player_pos_y - map_y) * delta_dist_y

                else:
                    step_y = 1
                    side_dist_y = (map_y + 1.0 - self.camera.player_pos_y) * delta_dist_y

                # Perform DDA
                while not hit:

                    if side_dist_x < side_dist_y:
                        side_dist_x += delta_dist_x
                        map_x += step_x
                        side = 0

                    else:
                        side_dist_y += delta_dist_y
                        map_y += step_y
                        side = 1

                    if self.world_map[map_x][map_y] > 0:
                        hit = 1

                # Calculate distance projected on self.camera direction
                if side == 0:
                    perp_wall_dist = (map_x - self.camera.player_pos_x + (1 - step_x) / 2) / ray_dir_x
                    wall_x = self.camera.player_pos_y + perp_wall_dist * ray_dir_y

                else:
                    perp_wall_dist = (map_y - self.camera.player_pos_y + (1 - step_y) / 2) / ray_dir_y
                    wall_x = self.camera.player_pos_x + perp_wall_dist * ray_dir_x

                wall_x -= int(wall_x)

                # Calculate value of tex_x
                tex_x = int(wall_x * self.texWidth)
                if (side == 0 and ray_dir_x > 0) or (side == 1 and ray_dir_y < 0):
                    tex_x = self.texWidth - tex_x - 1

                # Calculate height of line to draw
                line_height = int(self.screen_height / (perp_wall_dist))

                # Calculate lowest and highest pixel to fill in current stripe
                draw_start = max(int(-line_height / 2 + self.screen_height / 2), 0)
                draw_end = min(int(line_height / 2 + self.screen_height / 2), self.screen_height - 1)

                # Get the texture
                tex_num = self.world_map[map_x][map_y] - 1
                texture = self.textures[tex_num]
                texture_bits = texture.bits()
              
                for y in range(draw_start, draw_end):
                    
                    d = (y - draw_start) * 256
                    tex_y = ((d * self.textures[0].height()) // line_height) // 256
                    color_index = tex_y * texture.bytesPerLine() + tex_x * 4
                    color = texture_bits[color_index:color_index + 4]
                
                    # Perform bitwise operations to darken color if is side
                    if side == 1:
                        modified_color = memoryview(bytearray(color))
                        modified_color[0] = (modified_color[0] >> 1) & 0xFF  # Right shift by 1 and then bitwise AND with 0xFF
                        modified_color[1] = (modified_color[1] >> 1) & 0xFF
                        modified_color[2] = (modified_color[2] >> 1) & 0xFF
                    
                        modified_color = int.from_bytes(modified_color, byteorder='little')
                        self.buffer.setPixel(x,y,modified_color)

                    else:
                        color=int.from_bytes(color,byteorder="little")
                        self.buffer.setPixel(x,y,color)

