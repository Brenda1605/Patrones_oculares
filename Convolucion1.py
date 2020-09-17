def convolucion(a, nombreKernel):
import cv2
import numpy as np

ruta = 'ojo.jpg'
im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

kernel = np.asarray(a)

filtro = cv2.filter2D(im, -1, kernel)

nombreKernel = 'Convolucion ' + nombreKernel
cv2.imshow(nombreKernel ,filtro)
cv2.waitKey(0)
cv2.destroyAllWindows

convolucion([[1,2,1],[0,0,0],[-1,-2,-1]], "Sobel My")
