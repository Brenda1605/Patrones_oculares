def convolucion(a, nombreKernel):
     import cv2
     import numpy as np
     
     ruta = 'perro1.png'
     im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
     
     kernel = np.asarray(a)
     
     filtro = cv2.filter2D(im, -1, kernel)
     
     nombreKernel = 'Convolución ' + nombreKernel
     cv2.imshow(nombreKernel ,filtro)
     cv2.waitKey(0)
     cv2.destroyAllWindows