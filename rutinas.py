import time
from Servo import *
servo=Servo()

# Sentado y dar la pata
def rutina1():
    print("[1] Sientate; Da la pata!")
    try:
        for i in range(50):
        # Sentar
            # Muslos
            servo.setServoAngle(6,90+i)
            servo.setServoAngle(9,90-i)
            # Corvejón     
            servo.setServoAngle(5,90+i)
            servo.setServoAngle(10,90-i) 

            time.sleep(0.01)
        for i in range(5):
            # Muslos
            servo.setServoAngle(6,140+i)
            servo.setServoAngle(9,40-i)

            time.sleep(0.01)
        for i in range(15):
            # Corvejón     
            servo.setServoAngle(5,125-i)
            servo.setServoAngle(10,40+i)

            time.sleep(0.01)
        for i in range(20):
            # Codo
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(13,90+i)
            # Brazo
            servo.setServoAngle(3,90+i)
            servo.setServoAngle(12,90-i)

            time.sleep(0.01)
        for i in range(50):
            # Codo
            servo.setServoAngle(2,70-i)
            servo.setServoAngle(13,110+i)

            time.sleep(0.01)
        time.sleep(3)
        for i in range(65):
        # Dar la pata
            servo.setServoAngle(3,110-i)

            time.sleep(0.01)   
        servo.setServoAngle(2,80)
        time.sleep(5)
        servo.setServoAngle(5,90)
        servo.setServoAngle(6,90)
        servo.setServoAngle(13,90)
        servo.setServoAngle(12,90)
        servo.setServoAngle(10,90)
        servo.setServoAngle(9,90)
        servo.setServoAngle(2,90)
        servo.setServoAngle(3,90)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

#posicion de jugar
def rutina2():
    print("[2] Posicion de Juego")
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
        time.sleep(3.00)
        for i in range(30):
            servo.setServoAngle(15, 90+i)
            time.sleep(0.01)
        time.sleep(3.00)
        for i in range(40):
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(11,90+i)
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)
            time.sleep(0.01)
        time.sleep(2.00)
        for i in range(45):
            servo.setServoAngle(6,30+i)
            servo.setServoAngle(9,150-i)
            time.sleep(0.01)
        time.sleep(1.00)
        for i in range(25):
            servo.setServoAngle(5,30+i)
            servo.setServoAngle(10,150-i)
            time.sleep(0.01)
        time.sleep(5)

        servo.setServoAngle(15,90)
        servo.setServoAngle(5,90)
        servo.setServoAngle(6,90)
        servo.setServoAngle(13,90)
        servo.setServoAngle(12,90)
        servo.setServoAngle(10,90)
        servo.setServoAngle(9,90)
        servo.setServoAngle(2,90)
        servo.setServoAngle(3,90)

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

