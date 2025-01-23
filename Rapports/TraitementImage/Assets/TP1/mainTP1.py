import numpy as np
import cv2

#question 1
def soldes(prix):
    a = prix * 0.8
    b = prix * 0.6 
    c = prix * 0.5
    return a,b,c

retour = soldes(130)
print(f"les prix soldés sont de {retour}")


#Q2
tableau = np.array(np.random.randint(0,10,size=(3,4)))

print(tableau)
print("Collone:")
print(np.sum(tableau,axis=0)) #0 est en collone, 1 ou -1 est en ligne
print("Ligne:")
print(np.sum(tableau,axis=-1)) #0 est en collone, 1 ou -1 est en ligne

#Q3
#Wait key est une fonction bloquante qui attend le frappe d'une touche de clavier

img = cv2.imread('GE141002.bmp',cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy

cv2.imshow("Beton", img)
# Mise en pause du programme jusqu'à ce que l'utilisateur appuie sur une touche
x,y = img.shape[:2]
print(f" taille de l'image x:{x} y:{y}")



#Q4
print(img)
#l'image est un tableau de 2 dimension, avec les valeurs de niveau de gris dans les pixels respective au coordonées x y
#le cas où l'image est stockée dans un tableau a 3 dimensions, c'est le cas ou l'image traitée est en couleur.

#q5
#1: Opération de
#2: Opération de
#3: Opération de 



#Q3.1

rest, img2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print(f"seuil:{rest}")

cv2.imshow("Traitee", img2)
#cv2.imwrite("Q3.1.png", img2) sauvegardage Image




#Q3.2

el_struct = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))


img3 = cv2.morphologyEx(img2,cv2.MORPH_OPEN,el_struct)

cv2.imshow("Apres Ouverture", img3)
#cv2.imwrite("Q3.2.png", img3) sauvegardage Image


img4 = cv2.morphologyEx(img3,cv2.MORPH_CLOSE,el_struct)

cv2.imshow("Apres Fermeture", img4)
#cv2.imwrite("Q3.2.bis.png", img4) sauvegardage Image

#Q3.4

Granulats, _ = cv2.findContours(img4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
nb_granulats = len(Granulats)
print(f"Nombre de Granulats :{nb_granulats}")

#Q3.5
img5 =cv2.drawContours(img4, Granulats, -1, 125, 3)

cv2.imshow("Contours",img5)
# cv2.imwrite("Q3.5.png", img5) sauvegardage Image

#Q3.6 et Q.7
img6 = cv2.cvtColor(img5,cv2.COLOR_GRAY2BGR)
air_total = 0
for i, contour in enumerate(Granulats):
    air = cv2.contourArea(contour)
    air_total += air
    print(f"Granulat {i+1}: Air en Pixel = {air}")
    #rectangle englobant chaque Granulats
    x,y,w,h = cv2.boundingRect(contour)

    #position du texte
    text_x = x+w // 2
    text_y = y+h // 2
    #ecriture du numéro
    cv2.putText(img6,str(i+1), (text_x,text_y),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,255))

        
air_moyen = air_total / len(Granulats)
print(f"Air moyen des granulats:{air_moyen} pixels")

cv2.imshow("Contours",img6)
#cv2.imwrite("Q3.7.png", img6) sauvegardage Image

cv2.waitKey(0)
# Fermeture de toutes les fenêtres ouvertes
cv2.destroyAllWindows()





