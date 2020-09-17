import cv2
import numpy as np


def convolucion(kernel, nombreKernel):
    ruta = 'ojo.jpg'
    im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

    filtro = cv2.filter2D(im, -1, kernel)

    nombreKernel = 'Convolucion: ' + nombreKernel
    cv2.namedWindow(nombreKernel, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(nombreKernel, filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows

scharrKernelVertical = [[-3, -10, -3], [0, 0, 0], [3, 10, 3]]
convolucion(scharrKernelVertical, "Scharr")
