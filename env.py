import math
import pygame

class buildEnvironment:
    def __init__(self, MapDimensions):
        pygame.init() # initialize the pygame instance
        self.pointCloud = [] # to save the 2D points in pointCloud
        self.externalMap = pygame.image.load('floorPlan.png') 
        self.mapH, self.mapW = MapDimensions
        self.MapWindowName = 'LIDAR Sensor'
        pygame.display.set_caption(self.MapWindowName) # to set the window name 
        self.map = pygame.display.set_mode((self.mapW, self.mapH))
        self.map.blit(self.externalMap, (0, 0)) # to place the floorPlan.png onto the screen of pygame application

        # Basic Colors
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.Blue = (0, 0 , 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)
    
    # converts sensons angle-distance data to cartesian coordinates
    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))
    
    def dataStorage(self, data):
        # print(len(self.pointCloud))
        for element in data:
            point = self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)
    
    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))
