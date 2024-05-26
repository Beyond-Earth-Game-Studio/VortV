
import csv
from enum import Enum
from PySide6.QtGui import QImage,QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem
import camera
class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)


class VVAD():
   
    def __init__(self,data_source,cam):
        self.tony = cam
        self.last_bg = "un_init"

        self.tex_file=[QImage("assets/images/eagle.png"),
                       QImage("assets/images/redbrick.png"),
                       QImage("assets/images/purplestone.png"),
                       QImage("assets/images/greystone.png"),
                       QImage("assets/images/bluestone.png"),
                       QImage("assets/images/mossy.png"),
                       QImage("assets/images/wood.png"),
                       QImage("assets/images/colorstone.png")
                       ]
        
        #load these from the file eventually....
        self.map_texts = []
        for tex in self.tex_file:
            convert_text  = tex.convertToFormat(QImage.Format_ARGB32)
            print(convert_text.format())
            self.map_texts.append(convert_text)

        self.world_map = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 6, 4, 4, 6, 4, 6, 4, 4, 4, 6, 4],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [8, 0, 3, 3, 0, 0, 0, 0, 0, 8, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
    [8, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
    [8, 0, 3, 3, 0, 0, 0, 0, 0, 8, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 0, 0, 0, 0, 0, 6, 6, 6, 0, 6, 4, 6],
    [8, 8, 8, 8, 0, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 6, 0, 0, 0, 0, 0, 6],
    [7, 7, 7, 7, 0, 7, 7, 7, 7, 0, 8, 0, 8, 0, 8, 0, 8, 4, 0, 4, 0, 6, 0, 6],
    [7, 7, 0, 0, 0, 0, 0, 0, 7, 8, 0, 8, 0, 8, 0, 8, 8, 6, 0, 0, 0, 0, 0, 6],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 6, 0, 0, 0, 0, 0, 4],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 6, 0, 6, 0, 6, 0, 6],
    [7, 7, 0, 0, 0, 0, 0, 0, 7, 8, 0, 8, 0, 8, 0, 8, 8, 6, 4, 6, 0, 6, 6, 6],
    [7, 7, 7, 7, 0, 7, 7, 7, 7, 8, 8, 4, 0, 6, 8, 4, 8, 3, 3, 3, 0, 3, 3, 3],
    [2, 2, 2, 2, 0, 2, 2, 2, 2, 4, 6, 4, 0, 0, 6, 0, 6, 3, 0, 0, 0, 0, 0, 3],
    [2, 2, 0, 0, 0, 0, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 6, 0, 6, 3, 3, 0, 0, 0, 3, 3],
    [2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 2, 2, 2, 6, 6, 0, 0, 5, 0, 5, 0, 5],
    [2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 5, 0, 5, 0, 0, 0, 5, 5],
    [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 5, 0, 5, 0, 5, 0, 5, 0, 5],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 5, 0, 5, 0, 5, 0, 5, 0, 5],
    [2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 5, 0, 5, 0, 0, 0, 5, 5],
    [2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]


        # Loading
        self.map_data = self.load_map_data(data_source)
        print("loading complete")
        self.zone_name = self.get_zone_name() #Set initial zone name

    def load_map_data(self, file_path):#ECOR_1042
        map_data = {}
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                zone_name, p1, p2, p3, p4, zone_image_path = row
                zone_image_data = []
                with open(zone_image_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                    # Assuming image filenames are in the first two columns of each row
                         image_filenames = row[:8]
                         zone_image_data.append(image_filenames)
                
                map_data[zone_name] = tuple(tuple(map(float, point.split(','))) for point in [p1, p2, p3, p4]), zone_image_data
                print(map_data[zone_name])
        return map_data

    
    def is_in_zone(self,rectangle): #check is player position is in a zone
        sorted_rectangle = sorted(rectangle, key=lambda point: point[1])
        top_edge = tuple((sorted_rectangle[:2]))
        bottom_edge= tuple((sorted_rectangle[2:]))

        # Check if tony's y-coordinate is between the y-coordinates of the top and bottom edges
        if top_edge[1][1] <= self.tony.player_pos_y <= bottom_edge[1][1]:

            left_edge_x = min(rectangle, key=lambda point: point[0])[0]
            right_edge_x = max(rectangle, key=lambda point: point[0])[0]
            
            # Check if tony's x-coordinate is between the x-coordinates of the left and right edges
            if left_edge_x <= self.tony.player_pos_x<= right_edge_x:
                print("")
                return True
            print("Error no zone present")
        return False

    def get_zone_name(self): #iterate through map_data, checking position against the rectangle in each zone (WHERE ARE WE??)
        for zone_name, (rectangle, _) in self.map_data.items():
            if self.is_in_zone(rectangle):
                return zone_name
            print("YOU ARE IN THE VOID")
        return None
    
    
    def get_render_data(self):#determine the currently active fg and bg image
        #mapping for image location in data_list from direction
        self.tony_orientation = self.tony.normalize()

        direction_values = {
        Direction.NORTH.value: 0,
        Direction.SOUTH.value: 2,
        Direction.EAST.value:4,
        Direction.WEST.value:6
        }
        # Get images based on tony position and zone name
        if self.zone_name is not None:

            self.rectangle, zone_image_data = self.map_data[self.zone_name] #Use ECOR 1042 to pull image data from our active zone
            
            bg_image = zone_image_data[0][direction_values[self.tony_orientation.value]]  
            return (QPixmap(bg_image))
        

