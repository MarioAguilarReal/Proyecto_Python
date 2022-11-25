import time
from Servo import *
servo=Servo()
# Sentado
def rutina1():
    print("Hola soy la rutina 1")
    try:
        for i in range(60):
            
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            
            time.sleep(0.01)
        for i in range(90):
            
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)
            
            time.sleep(0.01)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
#posicion de jugar
def rutina2():
    print("Hola soy la rutina 2")
    try:
        for i in range(60):
            servo.setServoAngle(6,90-i)#Estirar hacia adelane para izquierda con el hombro (trasera)
            servo.setServoAngle(9,90+i)#Estirar hacia adelante pata derecha con el homobro (Trasera)
            servo.setServoAngle(5,90-i)#Estirar rodilla izquierda (trasera)
            servo.setServoAngle(10,90+i)#Estirar rodilla deracha (trasera)
            time.sleep(0.01)
        time.sleep(5.00)
        for i in range(90):
            servo.setServoAngle(3,90-i)#Estirar hacia adelane para izquierda con el hombro (delantera)
            servo.setServoAngle(12,90+i)#Estirar hacia adelante pata derecha con el homobro (delantera)
            servo.setServoAngle(2,90-i)#Estirar rodilla izquierda (delantera)
            servo.setServoAngle(13,90+i)#Estirar rodilla deracha (delantera)
            time.sleep(0.01)
        
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
#perro
def rutina3():
    print("Hola soy la rutina 3")
    try:
        for i in range(60):
            
            servo.setServoAngle(6,90-i)#Estirar hacia adelane para izquierda con el hombro (trasera)
            servo.setServoAngle(9,90+i)#Estirar hacia adelante pata derecha con el homobro (Trasera)
            
            time.sleep(0.01)
        for i in range(90):
            
            servo.setServoAngle(5,90-i)#Estirar rodilla izquierda (trasera)
            servo.setServoAngle(10,90+i)#Estirar rodilla deracha (trasera)
            
            time.sleep(0.01)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

