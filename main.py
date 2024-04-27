import env, sensors
import pygame
import math

environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertainity=(0.5, 0.01))
environment.map.fill((0, 0, 0)) # fill the map with black
environment.infomap = environment.map.copy()

running = True
while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
        position = pygame.mouse.get_pos() # get cursor position as Robot position through get_pos() function
        laser.position = position
        sensor_data = laser.sense_obstacles() # sense the obstacles once the robot has entered the environment
        environment.dataStorage(sensor_data) # store the cloud points data
        environment.show_sensorData() # show the cloud points data on the map

    environment.map.blit(environment.infomap, (0, 0))
    pygame.display.update()
