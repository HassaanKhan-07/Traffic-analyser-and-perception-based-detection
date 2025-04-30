import pygame
import sys
import threading
from time import sleep

# Initialize Pygame
pygame.init()

# Screen setup
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("SIMULATION")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load signal images
redSignal = pygame.Surface((50, 50))  # Placeholder for red signal
redSignal.fill((255, 0, 0))

yellowSignal = pygame.Surface((50, 50))  # Placeholder for yellow signal
yellowSignal.fill((255, 255, 0))

greenSignal = pygame.Surface((50, 50))  # Placeholder for green signal
greenSignal.fill((0, 255, 0))

# Font setup
font = pygame.font.Font(None, 30)

# Traffic signal data
noOfSignals = 4
currentGreen = 0
currentYellow = 0
timeElapsed = 0

# Signal coordinates and dummy data
signalCoods = [(100, 100), (200, 100), (300, 100), (400, 100)]
signalTimerCoods = [(110, 160), (210, 160), (310, 160), (410, 160)]
vehicleCountCoods = [(110, 200), (210, 200), (310, 200), (410, 200)]

class Signal:
    def _init_(self):
        self.green = 10
        self.yellow = 3
        self.red = 15
        self.signalText = "---"

signals = [Signal() for _ in range(noOfSignals)]
vehicles = {"north": {"crossed": 0}, "south": {"crossed": 0}, "east": {"crossed": 0}, "west": {"crossed": 0}}
simulation = []

# Vehicle class
class Vehicle:
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.currentImage = pygame.Surface((20, 20))  # Placeholder for vehicle image
        self.currentImage.fill((0, 0, 255))  # Blue vehicle

    def move(self):
        self.y += 1  # Move downward for simplicity

# Generate vehicles
def generateVehicles():
    while True:
        vehicle = Vehicle(100, 0)  # Create a vehicle at the top
        simulation.append(vehicle)
        sleep(2)  # Add a new vehicle every 2 seconds

# Start vehicle generation thread
thread3 = threading.Thread(name="generateVehicles", target=generateVehicles, args=())
thread3.daemon = True
thread3.start()

# Main simulation loop
def Main():
    global currentGreen, currentYellow, timeElapsed
    clock = pygame.time.Clock()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display background
        screen.fill(black)

        # Display signals and timers
        for i in range(noOfSignals):
            if i == currentGreen:
                if currentYellow == 1:
                    if signals[i].yellow == 0:
                        signals[i].signalText = "STOP"
                    else:
                        signals[i].signalText = signals[i].yellow
                    screen.blit(yellowSignal, signalCoods[i])
                else:
                    if signals[i].green == 0:
                        signals[i].signalText = "SLOW"
                    else:
                        signals[i].signalText = signals[i].green
                    screen.blit(greenSignal, signalCoods[i])
            else:
                if signals[i].red <= 10:
                    if signals[i].red == 0:
                        signals[i].signalText = "GO"
                    else:
                        signals[i].signalText = signals[i].red
                else:
                    signals[i].signalText = "---"
                screen.blit(redSignal, signalCoods[i])

            # Render signal text
            signalText = font.render(str(signals[i].signalText), True, white, black)
            screen.blit(signalText, signalTimerCoods[i])

            # Display vehicle count
            vehicleCountText = font.render(str(vehicles["north"]["crossed"]), True, black, white)
            screen.blit(vehicleCountText, vehicleCountCoods[i])

        # Time elapsed
        timeElapsedText = font.render(("Time Elapsed: " + str(timeElapsed)), True, white, black)
        screen.blit(timeElapsedText, (500, 50))

        # Display vehicles
        for vehicle in simulation:
            screen.blit(vehicle.currentImage, (vehicle.x, vehicle.y))
            vehicle.move()

        pygame.display.update()
        clock.tick(30)  # Limit to 30 FPS

# Run the main function
if _name_ == "_main_":
    Main()