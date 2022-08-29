import cv2

img = cv2.imread('C:/Users/claud/PycharmProjects/CursoOpenCV/data/igreja.jpg',cv2.IMREAD_GRAYSCALE)


tresholdMin = 100
tresholdMax = 200


kernelSize = (5,5)

filtro = cv2.GaussianBlur(img,kernelSize,0)

edges = cv2.Canny(filtro,tresholdMin,tresholdMax)

cv2.imshow('Original', img)
cv2.imshow('Canny',edges)

cv2.waitKey()

cv2.destroyAllWindows()