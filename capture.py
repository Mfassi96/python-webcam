import cv2 # biblioteca para capturar y procesar imagenes
import time


video=cv2.VideoCapture(0)# metodo para usar videos, puede recibir 2 tipos de parametros
                        # La ruta del archivo de video
                        # 0 para usar la camara del sistema 1 para usar la segunda camara, 2 para la tercera camara, etc    

a=1#Variable para contar el numero de frames generados

while True:
    a=a+1
    check,frame=video.read()
    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("capturing",gray)# crea una ventana con el titulo capturing y muestra el contenido del primer frame

    key=cv2.waitKey(1)

    if key==ord('q'): # si se presiona la tecla q se sale del programa
        break
print("Se han generado :" + str(a) +" Frames en total")
video.release()
cv2.destroyAllWindows()

