import cv2
import numpy as np

def convolucion(kernel, nombreKernel):

     ruta = 'ojo.jpg'
     im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

     kernelBordes = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
     prefiltro = cv2.filter2D(im, -1, kernelBordes)

     filtro = cv2.filter2D(im, -1, kernel)

     nombreKernel = 'Convolucion ' + nombreKernel
     cv2.namedWindow(nombreKernel, cv2.WINDOW_KEEPRATIO)
     cv2.imshow(nombreKernel, filtro)
     cv2.waitKey(0)
     cv2.destroyAllWindows

prewittKernelX = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
convolucion(prewittKernelX, "Prewitt X")

prewittKernelY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
convolucion(prewittKernelY, "Prewitt Y")
