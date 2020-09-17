def convolucion(a, nombreKernel):
     import cv2
     import numpy as np
     
     ruta = 'ojo.jpg'
     im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
     
     kernel = np.asarray(a)
     
     filtro = cv2.filter2D(im, -2, kernel)
     
     nombreKernel = 'Convolucion ' + nombreKernel
     print(filtro)
     cv2.imshow(nombreKernel ,filtro)
     cv2.waitKey(0)
     cv2.destroyAllWindows

cannyKernel = [[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]]
for i in cannyKernel:
     for j in i:
          j /= 159
convolucion(cannyKernel, "Canny")

