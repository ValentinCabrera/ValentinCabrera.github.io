import cv2

# Ruta al archivo de video
video_path = 'v.mp4'

# Crea un objeto de captura de video
cap = cv2.VideoCapture(video_path)

# Verifica si el video se abrió correctamente
if not cap.isOpened():
    print("Error al abrir el archivo de video.")
    exit()

# Reproduce el video
while True:
    # Lee el siguiente cuadro de video
    ret, frame = cap.read()

    # Verifica si se ha alcanzado el final del video
    if not ret:
        break

    # Muestra el cuadro de video
    cv2.imshow('Video', frame)

    # Espera un breve período de tiempo (milisegundos) entre cada cuadro
    # y verifica si se presionó la tecla 'q' para salir
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra las ventanas de visualización
cap.release()
cv2.destroyAllWindows()
