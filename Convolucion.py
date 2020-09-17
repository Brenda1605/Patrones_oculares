import cv2
import numpy as np
ruta = 'perro1.png'
im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

a = [[-1,0,1],
     [-1,0,1],
     [-1,0,1]]
kernel = np.asarray(a)
filtro = cv2.filter2D(im, -1, kernel)
cv2.imshow('Convolucion',filtro)
cv2.waitKey(0)
cv2.destroyAllWindows