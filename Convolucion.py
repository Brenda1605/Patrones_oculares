import cv2
import numpy as np


# This function called convolucion receives two parameters which are the kernel
# that the function is going to use and the name of the filter/kernel.  It uses
# functions from the cv2 and numpy libraries to convert the image into an array
# with the values of the image (BGR) and first we multiply the array of the image
# with a kernel to highlight the border of the image and then we multiply this
# new array with the kernel that the funtion received.  Then we show the resulting
# image after applying those kernels.

def convolution(kernel, kernelName):
    path = "ojo.jpg"
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    kernelBorders = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    prefilter = cv2.filter2D(im, -1, kernelBorders)

    filtro = cv2.filter2D(prefilter, -1, kernel)

    kernelName = "Convolution: " + kernelName
    cv2.namedWindow(kernelName, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(kernelName, filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows


# Variables hold the kernel for each corresponding filter
# Each kernel is assigned to the function convolution, with its corresponding name for use in display

cannyKernel = np.array([[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]]) / 159
convolution(cannyKernel, "Canny")

scharrKernelHorizontal = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
convolution(scharrKernelHorizontal, "Scharr horizontal")

scharrKernelVertical = np.array([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])
convolution(scharrKernelVertical, "Scharr vertical")

sobelMxKernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
convolution(sobelMxKernel, "Sobel Mx")

sobelMyKernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
convolution(sobelMyKernel, "Sobel My")

prewittKernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
convolution(prewittKernelX, "Prewitt X")

prewittKernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
convolution(prewittKernelY, "Prewitt Y")
