# ABRIR WEBCAM
import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("WEBCAM", frame)
        key = cv2.waitKey(3)

        if key == 27: # TECLA ESC
            break
    cv2.imwrite("FotoWebcam.jpg", frame) 

webcam.release()
cv2.destroyAllWindows