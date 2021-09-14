"""atl_thymio controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

import math

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = Robot.getDevice('prox.horizontal.0')
#  ds.enable(timestep)

ds_index = 0
send_message =""
prox_horizontal = ["prox.horizontal.0", "prox.horizontal.1", "prox.horizontal.2", "prox.horizontal.3", "prox.horizontal.4", "prox.horizontal.5", "prox.horizontal.6"]
for sensor in prox_horizontal:
  prox_horizontal[ds_index] = robot.getDevice(sensor)
  prox_horizontal[ds_index].enable(timestep)
  ds_index = ds_index + 1
  print(sensor)
robot.wwiSendText("[0] [1] [2] [3] [4] [5] [6] [7] [8]")

# prox_ground_0 = robot.getDevice("prox.ground.0")
# prox_ground_0.enable(timestep)
# prox_ground_1 = robot.getDevice("prox.ground.1")
# prox_ground_1.enable(timestep)



# Actuators
## Motors
left_motor = robot.getDevice("motor.left")
right_motor = robot.getDevice("motor.right")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

## LEDs
LED_FREQ = 4.0
time = robot.getTime()
#rgb_red = float(0.5 * math.sin(math.pi() / float(LED_FREQ) * float(time)) + 0.5);
#rgb_green = 0.5 * math.sin(math.pi() / float(LED_FREQ) * float(time) + float(math.pi()/3)) + 0.5;
#rgb_blue = 0.5 * math.sin(math.pi() / float(LED_FREQ) * float(time) + float(2*math.pi()/3)) + 0.5;

leds_top = robot.getDevice("leds.top")
leds_bottom_left = robot.getDevice("leds.bottom.left")
leds_bottom_right = robot.getDevice("leds.bottom.right")
leds_buttons_led = [
    robot.getDevice("leds.buttons.led0"),
    robot.getDevice("leds.buttons.led1"),
    robot.getDevice("leds.buttons.led2"),
    robot.getDevice("leds.buttons.led3")
    ]
leds_circle_led = [
    robot.getDevice("leds.circle.led0"),
    robot.getDevice("leds.circle.led1"),
    robot.getDevice("leds.circle.led2"),
    robot.getDevice("leds.circle.led3"),
    robot.getDevice("leds.circle.led4"),
    robot.getDevice("leds.circle.led5"),
    robot.getDevice("leds.circle.led6")
    ]
leds_prox_h_led = [
    robot.getDevice("leds.prox.h.led0"),
    robot.getDevice("leds.prox.h.led1"),
    robot.getDevice("leds.prox.h.led2"),
    robot.getDevice("leds.prox.h.led3"),
    robot.getDevice("leds.prox.h.led4"),
    robot.getDevice("leds.prox.h.led5"),
    robot.getDevice("leds.prox.h.led6")
    ]
leds_prox_v_led = [
    robot.getDevice("leds.prox.v.led0"),
    robot.getDevice("leds.prox.v.led1")
    ]
leds_sound = robot.getDevice("leds.sound")
leds_rc = robot.getDevice("leds.rc")
leds_temperature_red = robot.getDevice("leds.temperature.red")
leds_temperature_blue = robot.getDevice("leds.temperature.blue")

print(str(leds_prox_v_led))

# Controller welcome message in webots console
print("Autre TechLab ThymioII controller - I am ready now!")
print("TIME STAMP = " +str(timestep))
# **********************************************************************************
# Main loop:
# - perform simulation steps until Webots is stopping the controller
#
# General structure:
# - Read the and update robot window

# - Read the sensors
while robot.step(timestep) != -1:
    # Update and Read Robot Window
    ds_index =0
    send_message = ""
    while ds_index < 7:
        send_message = (send_message + str(int(prox_horizontal[ds_index].getValue())) + " ")
        print(str(ds_index) + " " + send_message)
        ds_index = ds_index + 1
    robot.wwiSendText(send_message)

    message = robot.wwiReceiveText()
    if (message):
        print("robot window message: " + str(message))

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    # val = ds.getValue()
    left_dist = prox_horizontal[0].getValue()
    right_dist = prox_horizontal[4].getValue()
    # print("left_dist " + str(left_dist) + " right_dist " + str(right_dist)) 
    # Process sensor data here.
    # compute behavior (user functions)
    left = 5
    right = 5

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    if left_dist < 1000:
        leds_prox_h_led[0].set(1)
        leds_prox_h_led[4].set(1)
        leds_circle_led[0].set(1)
        left_motor.setVelocity(10)
        right_motor.setVelocity(10)
    else:
        leds_prox_h_led[0].set(1)
        leds_prox_h_led[4].set(1)
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
    pass

# Enter here exit cleanup code.
