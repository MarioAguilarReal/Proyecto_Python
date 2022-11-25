import time
from Servo import *
servo=Servo()

def rutina1():
    print("Hola soy la rutina 1")
    try:
        for i in range(90):
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)
            servo.setServoAngle(11,90+i)
            time.sleep(0.01)

        for i in range(90):
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)
            servo.setServoAngle(13,90+i)
            time.sleep(0.01)
        for i in range(60):
            servo.setServoAngle(3,90-i)
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            servo.setServoAngle(12,90+i)
            time.sleep(0.01)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

def rutina2():
    print("Hola soy la rutina 2")
    try:
        for i in range(90):
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)
            servo.setServoAngle(11,90+i)
            time.sleep(0.01)

        for i in range(90):
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)
            servo.setServoAngle(13,90+i)
            time.sleep(0.01)
        for i in range(60):
            servo.setServoAngle(3,90-i)
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            servo.setServoAngle(12,90+i)
            time.sleep(0.01)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

def rutina3():
    print("Hola soy la rutina 3")
    try:
        for i in range(90):
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)
            servo.setServoAngle(11,90+i)
            time.sleep(0.01)

        for i in range(90):
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)
            servo.setServoAngle(13,90+i)
            time.sleep(0.01)
        for i in range(60):
            servo.setServoAngle(3,90-i)
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            servo.setServoAngle(12,90+i)
            time.sleep(0.01)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

