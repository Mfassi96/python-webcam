# Captura de videos con Python 📽️

Este script utiliza la biblioteca OpenCV (`cv2`) para capturar video desde la cámara del sistema y mostrarlo en escala de grises. También cuenta el número de fotogramas (frames) capturados y permite salir del programa presionando la tecla 'q'.

## Variables Utilizadas y su Función

1.  **`video`:**
    * **Función:** Se utiliza para inicializar la captura de video desde la cámara y almacena el objeto de captura de video, que contiene información sobre la fuente de video (en este caso, la cámara del sistema) y métodos para leer fotogramas.
    * **Inicialización:** `video = cv2.VideoCapture(0)`: Inicializa la captura de video desde la cámara predeterminada (0).
2.  **`a`:**
    * **Función:** Contador de fotogramas (frames) capturados.
3.  **`check`:**
    * **Función:** Indica si la lectura de un fotograma fue exitosa.
    * **Actualización:** `check, frame = video.read()`: Se actualiza con el resultado de la lectura de cada fotograma.
4.  **`frame`:**
    * **Función:** Almacena la imagen del fotograma capturado.
    * **Almacenamiento:** Contiene los datos de la imagen en formato BGR (azul, verde, rojo). Se actualiza con la imagen de cada fotograma leído.
5.  **`gray`:**
    * **Función:** Almacena la imagen del fotograma convertida a escala de grises.
    * **Almacenamiento:** Contiene los datos de la imagen en escala de grises.
    * **Actualización:** `gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`: Se actualiza con la imagen convertida a escala de grises.
6.  **`key`:**
    * **Tipo:** Entero (`int`).
    * **Función:** Almacena el código de la tecla presionada por el usuario.

## Flujo del Programa

1.  **Inicialización:**
    * Se importa la biblioteca cv2 para el procesamiento de imagenes.
    * Se inicializa la captura de video desde la cámara.
    * Se inicializa el contador de fotogramas `a`.
2.  **Bucle Principal (`while True`):**
    * Se incrementa el contador de fotogramas `a`.
    * Se lee un fotograma de la cámara.
    * Se verifica si la lectura fue exitosa (`check`).
    * Se convierte el fotograma a escala de grises (`gray`).
    * Se muestra el fotograma en una ventana.
    * Se espera a que el usuario presione una tecla.
    * Si la tecla presionada es 'q', se sale del bucle.
3.  **Finalización:**
    * Se imprime el número total de fotogramas capturados.
    * Se libera el objeto de captura de video.
    * Se cierran todas las ventanas.
.
