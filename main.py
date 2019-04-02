#!/usr/bin/env python3
import RPi.GPIO as GPIO
from motor.motor import SetupMotor, MotorDriver

# Motor A1, A2
in1 = 24
in2 = 23
ena = 25

# Motor B1, B2
in3 = 14
in4 = 15
enb = 18
temp1 = 1

GPIO.setmode(GPIO.BCM)

motor1 = SetupMotor(in1, in2, ena)
motor2 = SetupMotor(in3, in4, enb)
motor1.setup()
motor2.setup()
motor1.changePower(100)
motor2.changePower(100)

driver = MotorDriver(motor1, motor2)
driver.turnLeftForward(2)
driver.turnRightBackward(2)
driver.turnRightForward(2)
driver.turnLeftBackward(2)
driver.endSession()
