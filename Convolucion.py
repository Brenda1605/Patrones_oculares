# This function called convolucion receives two parameters which are the kernel
# that the function is going to use and the name of the filter/kernel.  It uses
# functions from the cv2 and numpy libraries to convert the image into an array
# with the values of the image (BGR) and first we multiply the array of the image
# with a kernel to highlight the border of the image and then we multiply this
# new array with the kernel that the funtion received.  Then we show the resulting
# image after applying those kernels.

import cv2
import numpy as np

def convolucion(kernel, nombreKernel):
    ruta = 'ojo.jpg'
    im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

    kernelBordes = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    prefiltro = cv2.filter2D(im, -1, kernelBordes)

    filtro = cv2.filter2D(prefiltro, -1, kernel)

    nombreKernel = 'Convolucion: ' + nombreKernel
    cv2.namedWindow(nombreKernel, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(nombreKernel, filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows


scharrKernelHorizontal = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
convolucion(scharrKernelHorizontal, "Scharr")

scharrKernelVertical = np.array([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])
convolucion(scharrKernelVertical, "Scharr")

cannyKernel = np.array([[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]])/159
convolucion(cannyKernel, "Canny")

sobelMxKernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
convolucion(sobelMxKernel,"Sobel Mx")

sobelMyKernel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
convolucion(sobelMyKernel, "Sobel My")

prewittKernelX = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
convolucion(prewittKernelX, "Prewitt X")

prewittKernelY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
convolucion(prewittKernelY, "Prewitt Y")

laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])
convolucion(laplacian, "Laplacian")
