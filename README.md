# Understanding the Functionality of LIDAR Sensor
LIDAR, which stands for Light Detection and Ranging, is a remote sensing method that utilizes light in the form of a pulsed laser to measure variable distances to the Earth. It operates on the principle of measuring the time it takes for a laser pulse to travel to an object or surface and return to the sensor. This technology is widely used in various fields such as surveying, geology, autonomous vehicles, and archaeology due to its high precision and accuracy.

## Basic Components:
- **Laser Emitter**: The LIDAR sensor emits short pulses of laser light towards the target area. These pulses are typically in the form of infrared light, which is invisible to the human eye but easily detectable by the sensor.
- **Scanner**: The scanner directs the emitted laser pulses over the desired area. It can be either a rotating mirror or a stationary multi-beam setup, depending on the specific LIDAR design.
- **Receiver**: After the laser pulse interacts with objects in the target area, a portion of the light is reflected back towards the sensor. The receiver collects these returning light pulses.
- **Timing and Distance Measurement System**: By precisely measuring the time it takes for the laser pulses to travel to the object and back, the LIDAR system calculates the distance to each point in the scanned area.

## Functionality
**sense_obstacles()**
The core functionality of obstacle detection is implemented in the sense_obstacles() function within the LidarSensor class. Here's how it works:

1. **Initialization**: The function initializes an empty list data to store the detected obstacles and their measurements.
2. **Looping Through Angles**: It iterates through a range of angles from 0 to 2π (i.e., a full circle) with a certain granularity (in this case, 60 angles). This covers the sensor's field of view.
3. **Calculating Endpoints**: For each angle, it calculates the endpoint (x2, y2) based on the robot's position (x1, y1) and the sensor's maximum range.
4. **Sampling**: Within each angle, it further samples points along the line segment between (x1, y1) and (x2, y2). This is achieved by linear interpolation (u ranges from 0 to 1). The number of samples is determined by the loop from 0 to 100.
5. **Obstacle Detection**: For each sampled point, it checks if the color of the pixel in the map at that point is black (0, 0, 0), indicating an obstacle. If so, it calculates the distance to the obstacle using the distance() method.
6. **Adding Uncertainty**: After obtaining the distance and angle to the obstacle, some uncertainty is added to these measurements using the uncertainty_add() function. This step simulates real-world noise and imperfections in the sensor's measurements.
7. **Storing Measurements**: The obstacle's distance, angle, and position are appended to the data list as a tuple.
8. **Returning Data**: If any obstacles are detected (data is not empty), the function returns the list of obstacle measurements. Otherwise, it returns False to indicate no obstacles were detected.

## Usage
1. Clone this repository to your local machine:
```bash
git clone https://github.com/VivekSai07/Pythonic-LIDAR-Simulation-Building-a-Sensor-from-Scratch.git
```
2. Navigate to the project directory and run the main script:
```bash
python main.py
```

## Output
![Demo](https://github.com/VivekSai07/Pythonic-LIDAR-Simulation-Building-a-Sensor-from-Scratch/blob/main/Output.png)
