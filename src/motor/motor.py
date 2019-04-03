import RPi.GPIO as GPIO
from time import sleep


class SetupMotor:
    pwmPower = 25

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
        self.pwm.start(self.pwmPower)

    def changePower(self, power):
        self.pwmPower = power
        self.pwm.ChangeDutyCycle(power)


class MotorDriver:

    def __init__(self, motorA, motorB):
        self._motorA = motorA
        self._motorB = motorB

    def forward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorA.in2_pin, GPIO.LOW)
        GPIO.output(self._motorB.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in2_pin, GPIO.LOW)
        sleep(distance)
        GPIO.cleanup()

    def backward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.LOW)
        GPIO.output(self._motorA.in2_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in1_pin, GPIO.LOW)
        GPIO.output(self._motorB.in2_pin, GPIO.HIGH)
        sleep(distance)
        GPIO.cleanup()

    def turnLeftInPlace(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorA.in2_pin, GPIO.LOW)
        GPIO.output(self._motorB.in1_pin, GPIO.LOW)
        GPIO.output(self._motorB.in2_pin, GPIO.HIGH)
        sleep(distance)
        GPIO.cleanup()

    def turnRightInPlace(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.LOW)
        GPIO.output(self._motorA.in2_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in2_pin, GPIO.LOW)
        sleep(distance)
        GPIO.cleanup()

    def turnLeftForward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorA.in2_pin, GPIO.LOW)
        sleep(distance)
        GPIO.cleanup()

    def turnRightBackward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorB.in1_pin, GPIO.LOW)
        GPIO.output(self._motorB.in2_pin, GPIO.HIGH)
        sleep(distance)
        GPIO.cleanup()

    def turnLeftBackward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorA.in1_pin, GPIO.LOW)
        GPIO.output(self._motorA.in2_pin, GPIO.HIGH)
        sleep(distance)
        GPIO.cleanup()

    def turnRightForward(self, distance):
        self._motorA.setup()
        self._motorB.setup()
        GPIO.output(self._motorB.in1_pin, GPIO.HIGH)
        GPIO.output(self._motorB.in2_pin, GPIO.LOW)
        sleep(distance)
        GPIO.cleanup()

    def endSession(self):
        self._motorA.pwm.stop()
        self._motorB.pwm.stop()
        GPIO.cleanup()
