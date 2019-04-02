import RPi.GPIO as GPIO
from time import sleep


class SetupMotor:
    startingPower = 25

    def __init__(self, in1, in2, en):
        self.in1_pin = in1
        self.in2_pin = in2
        self.en = en

    def setup(self):
        # Setup of Motor IN1, IN2 inputs
        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)
        GPIO.output(self.in1_pin, GPIO.OUT)
        GPIO.output(self.in2_pin, GPIO.OUT)

        # Setup of EN pin
        GPIO.setup(self.en, GPIO.OUT)
        self.pwm = GPIO.PWM(self.en, 1000)
        self.pwm.start(self.startingPower)

    def changePower(self, power):
        self.pwm.ChangeDutyCycle(power)

class MotorDriver:

    def __init__(self, motorA, motorB):
        self._motorA = motorA
        self._motorB = motorB

    def forward(self, distance):
        GPIO.output(self._motorA.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorA.in2_pin, GPIO.LOW)
        GPIO.output(self._motorB.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in2_pin, GPIO.LOW)
        sleep(distance)

    def backward(self, distance):
        GPIO.output(self._motorA.in1_pin, GPIO.LOW)
        GPIO.output(self._motorA.in2_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in1_pin, GPIO.LOW)
        GPIO.output(self._motorB.in2_pin, GPIO.HIGH)
        sleep(distance)

    def endSession(self):
        self._motorA.pwm.stop()
        self._motorB.pwm.stop()
        GPIO.cleanup()
