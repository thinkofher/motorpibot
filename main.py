import RPi.GPIO as GPIO
from time import sleep

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

# Motor A1, A2: setup
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

GPIO.output(in1, GPIO.OUT)
GPIO.output(in2, GPIO.OUT)

# Motor B1, B2: setup
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

GPIO.output(in3, GPIO.OUT)
GPIO.output(in4, GPIO.OUT)

power = 50
pa = GPIO.PWM(ena, 1000)
pa.start(power)

pb = GPIO.PWM(enb, 1000)
pb.start(power)

distance = 3

GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)

GPIO.output(in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)

sleep(distance)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)

GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.HIGH)

sleep(distance)

GPIO.cleanup()
