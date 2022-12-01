import time
from Servo import *
from Led import *
servo=Servo()
led=Led()

# Sentado y dar la pata
def rutina1():
    print("[1] Sientate; Da la pata!")
    try:
        led.colorWipe(led.strip, Color(180, 0, 0),20) 
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

        #Regresar a 90°
        led.colorWipe(led.strip, Color(255, 255, 255),20) 
        for i in range(35):
            servo.setServoAngle(10,55+i)
            servo.setServoAngle(13,160-i)
            servo.setServoAngle(3,45+i)
            servo.setServoAngle(6,145-i)
            servo.setServoAngle(9,35+i)

            time.sleep(0.01)
        for i in range(20):
            servo.setServoAngle(13,125-i)
            servo.setServoAngle(5,110-i)
            servo.setServoAngle(12,70+i)
            servo.setServoAngle(6,110-i)
            servo.setServoAngle(9,70+i)

            time.sleep(0.01)
        for i in range(10):
            servo.setServoAngle(2,80+i)
            servo.setServoAngle(13,100-i)
            servo.setServoAngle(3,80+i)

            time.sleep(0.01)
        led.colorWipe(led.strip, Color(0, 0, 0))
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

#posicion de jugar
def rutina2():
    print("[2] Posicion de Juego")
    try:
        led.colorWipe(led.strip, Color(180, 0, 0),20) 
        for i in range(60):
        # Estirar hacia delante
            # Muslo
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            # Corvejón
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)

            time.sleep(0.01)
        time.sleep(5.00)
        for i in range(90):
        # Estirar hacia delante
            # Brazo
            servo.setServoAngle(3,90-i)
            servo.setServoAngle(12,90+i)
            # Codo
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(13,90+i)

            time.sleep(0.01)
        time.sleep(3.00)
        for i in range(30):
            # Subir cabeza
            servo.setServoAngle(15, 90+i)

            time.sleep(0.01)
        time.sleep(3.00)
        for i in range(20):
        # Abrir patitas
            # Ingle
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(11,90+i)
            # Hombro
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)

            time.sleep(0.01)
        time.sleep(2.00)
        for i in range(10):
        # Estirar codos
            servo.setServoAngle(2,0-i)
            servo.setServoAngle(13,180+i)
            servo.setServoAngle(5,30-i)
            servo.setServoAngle(10,150+i)

            time.sleep(0.01)
        for i in range(45):
        # Doblar muslos
            servo.setServoAngle(6,30+i)
            servo.setServoAngle(9,150-i)
            time.sleep(0.01)
      
        time.sleep(5)
        # Regresar a 90°
        led.colorWipe(led.strip, Color(255, 255, 255),20)
        for i in range(70):
            servo.setServoAngle(2,-10+i)
            servo.setServoAngle(13,190-i)
            servo.setServoAngle(5,20+i)
            servo.setServoAngle(10,160-i)
            servo.setServoAngle(3,0+i)
            servo.setServoAngle(12,180-i)

            time.sleep(0.01)
        for i in range(30):
            servo.setServoAngle(2,60+i)
            servo.setServoAngle(13,120-i)
            servo.setServoAngle(15,120-i)

            time.sleep(0.01)
        for i in range(20):
            servo.setServoAngle(3,70+i)
            servo.setServoAngle(12,110-i)
            servo.setServoAngle(4,70+i)
            servo.setServoAngle(11,110-i)
            servo.setServoAngle(7,74+i)
            servo.setServoAngle(8,114-i)
        
            time.sleep(0.01)
        led.colorWipe(led.strip, Color(0, 0, 0))
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
#perro
def rutina3():
    print("Hola soy la rutina 3")
    try:
        led.colorWipe(led.strip, Color(180, 0, 0),20) 
        for i in range(30):
            
            servo.setServoAngle(7,90-i)#Estirar hacia adelante pata izquierda con el hombro (trasera)
            servo.setServoAngle(8,90+i)#Estirar hacia adelante pata derecha con el homobro (Trasera)
            
            time.sleep(0.001)
        for i in range(30):
            
            servo.setServoAngle(6,90-i)#Estirar hacia adelante pata izquierda con el hombro (trasera)
            servo.setServoAngle(9,90+i)#Estirar hacia adelante pata derecha con el homobro (Trasera)
            
            time.sleep(0.01)
        for i in range(90):
            
            servo.setServoAngle(5,90-i)#Estirar rodilla izquierda (trasera)
            servo.setServoAngle(10,90+i)#Estirar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(90):
            
            servo.setServoAngle(5,0+i)#cerrar rodilla izquierda (trasera)
            servo.setServoAngle(10,180-i)#cerrar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(90):
            
            servo.setServoAngle(5,90-i)#Estirar rodilla izquierda (trasera)
            servo.setServoAngle(10,90+i)#Estirar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(90):
            
            servo.setServoAngle(5,0+i)#cerrar rodilla izquierda (trasera)
            servo.setServoAngle(10,180-i)#cerrar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(90):
            
            servo.setServoAngle(5,90-i)#Estirar rodilla izquierda (trasera)
            servo.setServoAngle(10,90+i)#Estirar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(90):
            
            servo.setServoAngle(5,0+i)#cerrar rodilla izquierda (trasera)
            servo.setServoAngle(10,180-i)#cerrar rodilla deracha (trasera)
            
            time.sleep(0.09)
        for i in range(30):
            
            servo.setServoAngle(7,60+i)#Estirar hacia adelante pata izquierda con el hombro (trasera)
            servo.setServoAngle(8,120-i)#Estirar hacia adelante pata derecha con el homobro (Trasera)
            
            time.sleep(0.10)

        led.colorWipe(led.strip, Color(0, 0, 0))
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

    
    
 