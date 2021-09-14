"""campfire controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Supervisor, LED, DistanceSensor
from controller import Supervisor
from controller import Speaker
import random
import math


def randomizePeriod():
    return 0.001 + (random.random() / 40 - 0.0001)

def randomizeAmplitude():
    return 0.4 + (random.random() / 2.5 - 0.2)

# create the Supervisor instance.
supervisor = Supervisor()

speaker = supervisor.getSpeaker("fire_speaker")
Speaker.playSound(speaker, speaker, "fire_burning.wav", 0.1, 1, 0, True)

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

led = supervisor.getLED('EmberLED')
lastLedIntensity = 0
currentStep = 0
random.seed()


ledBaseLevel = 0.6

amplitude = randomizeAmplitude()

period = randomizePeriod()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    ledIntensity = led.get()

    ledIntensity = (ledBaseLevel + math.sin(currentStep * period) * amplitude)

    ledIntensity = (ledIntensity * 0.2 + lastLedIntensity * 0.8)

    if ledIntensity <= ledBaseLevel:
        currentStep = 0
        period = randomizePeriod()
        amplitude = randomizeAmplitude()

    led.set(int(ledIntensity * 255))
    lastLedIntensity = ledIntensity
    currentStep += 1

# Enter here exit cleanup code.
