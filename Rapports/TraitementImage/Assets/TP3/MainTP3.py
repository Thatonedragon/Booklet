import cv2
import numpy as np


Image_Bille = cv2.imread("boules.png")


cv2.imshow("Bonjour",Image_Bille)

taille_x, taille_y, nbr_canneaux = np.shape(Image_Bille)

print(f'Taille de x {taille_x}')
print(f'Taille de y {taille_y}')
print(f'Taille de canneaux {nbr_canneaux}')

Image_Bille_bleu, Image_Bille_vert, Image_Bille_rouge = cv2.split(Image_Bille) 

cv2.imshow("Rouge",Image_Bille_rouge)

#En faisant la methode des seuils, nos n'aurons jamais seulement le rouge, parceque on aura toujour des composant.
#Il faudrai faire un tri sur les trois variable RGB et afficher la abnde passante de la couleur rouge sur une image en couleur et non juste la variable R qui retourne une image en noir et blanc
#ce qui fait que sur le retour on aura toutes les couleurs qui ont une composante rouge, ce qui ne fait pas de tri.

##HSV

Image_Bille_HSV = cv2.cvtColor(Image_Bille,cv2.COLOR_BGR2HSV)
Image_Bille_Hue, Image_Bille_Saturation, Image_Bille_lightness = cv2.split(Image_Bille_HSV) 

I = 10
Masque_1 = cv2.inRange(Image_Bille_Hue,0,I)
Masque_2 = cv2.inRange(Image_Bille_Hue,179-I,179)
Masque_final = cv2.bitwise_or(Masque_1,Masque_2)
cv2.imshow('Rouge',Masque_final)
#ici le problème c'est qu'on a toujours la bille blanche qui est affiché
##Question 13
rouge_inferieur = np.array([0,50,50])
rouge_superieur = np.array([I,255,255])

rouge_inferieur_2 = np.array([180-I,50,50])
rouge_superieur_2 = np.array([180,255,255])


Masque_1 = cv2.inRange(Image_Bille_HSV,rouge_inferieur,rouge_superieur)
Masque_2 = cv2.inRange(Image_Bille_HSV,rouge_inferieur_2,rouge_superieur_2)

Masque_totale = cv2.bitwise_or(Masque_1,Masque_2)

cv2.imshow('Rouge nouveau',Masque_totale)

##le résultat n'est pas satisfaisant car on a toujours les contours des billes bleues qui s'affichent mais on a plus la bille blanche

el_struct = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))

Ouverture = cv2.morphologyEx(Masque_totale,cv2.MORPH_OPEN,el_struct)

cv2.imshow('Ouverture',Ouverture)

Fermeture = cv2.morphologyEx(Ouverture,cv2.MORPH_CLOSE, el_struct)

cv2.imshow('Fermeture',Fermeture)

Countours, _ = cv2.findContours(Fermeture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

Img_Contours =cv2.drawContours(Fermeture, Countours, -1, 125, 2)

cv2.imshow('Countours',Img_Contours)

for contour in Countours:
    (x,y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x),int(y))
    radius = int(radius)
#print(center)
    cv2.circle(Image_Bille, center, radius, (0,255,0),2)
    cv2.imshow('image avec cercle', Image_Bille)


cv2.waitKey(0)

cv2.destroyAllWindows()