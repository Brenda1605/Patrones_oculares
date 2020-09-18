import cv2
import numpy as np

# This function called convolucion receives two parameters which are the kernel
# that the function is going to use and the name of the filter/kernel.  It uses
# functions from the cv2 and numpy libraries to convert the image into an array
# with the values of the image (BGR) and first we multiply the array of the image
# with a kernel to highlight the border of the image and then we multiply this
# new array with the kernel that the funtion received.  Then we show the resulting
# image after applying those kernels.

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
