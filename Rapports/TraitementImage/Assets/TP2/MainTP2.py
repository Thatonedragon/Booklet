import numpy as np
import cv2
import matplotlib.pyplot as plt


#entrainement partie 2
# ecole = 'unilasalle'
# print(ecole[3:7]) # s'affiche: lasa
# print(ecole[5:]) # s'affiche: salle
# print(ecole[:3]) # s'affiche: uni

# Déclaration en dur d'un tableau T à 2 lignes et 3 colonnes

# T = np.array([[1, 2, 3], [4, 5, 6]])
# T2 = T[:, 0:2]
# print(T)
# print(T2)

#-> extraction de toutes les lignes et des 2 premières colonnes de T

#lire l'image
img = cv2.imread('LAIT_KO.bmp',cv2.IMREAD_GRAYSCALE)

#Prendre la somme en ligne des valeurs de pixels
projection_ligne = np.sum(img,axis = 0)

#valeur max de cette ligne
valeur_max_ligne = np.max(projection_ligne)

#procédée idem
projection_colonne = np.sum(img,axis = 1)
valeur_max_colonne = np.max(projection_colonne)


#à decommenter si on veut voir les tracées
# plt.plot(projection_ligne)
# plt.plot(projection_colonne)
# plt.show()

print(f"Valeur Max ligne {valeur_max_ligne}")
print(f"Valeur Max colonne {valeur_max_colonne}")

valeur_seuil_front_colonne = valeur_max_colonne/2
valeur_seuil_front_ligne = valeur_max_ligne/2

Bordure_Superieur = np.where(projection_ligne> valeur_seuil_front_ligne)[0][0] #Tu n'a que la premiere valeur du tableau
Bordure_Inferieur = np.where(projection_ligne> valeur_seuil_front_ligne)[0][-1] #Tu a la derniere valeur du tableau 
Bordure_Gauche = np.where(projection_colonne > valeur_seuil_front_colonne)[0][0] 
Bordure_Droite = np.where(projection_colonne > valeur_seuil_front_colonne)[0][-1]
#En ayant ces 4 valeurs, on peux retrouver les 4 coins du rectangle
#Peut etre faire mieux plus tard quand l'image n'est pas réelement droit

# print(Bordure_Droite)
# print(Bordure_Gauche)
# print(Bordure_Superieur)
# print(Bordure_Inferieur)

plt.show()

#cv2.rectangle(img,(Bordure_Inferieur,Bordure_Droite),(Bordure_Superieur,Bordure_Gauche),125,5)
#cv2.imshow('image', img)


#3.2 Découpage de la brique de lait

Decoupage = img[Bordure_Gauche:Bordure_Droite, Bordure_Superieur:Bordure_Inferieur]

cv2.imshow('Decoup', Decoupage)


#decouper la date
Decoupage_date = Decoupage[303:303+95 , 57:57+41]

# Question 4   6

#A l’étape précédente, était-il nécessaire de détecter les quatre cotés de la brique de lait pour pouvoir extraire la date
#Tout depend de comment la photo est prise et si on peut avoir la photo toujour dans le même angle, même position dans l'image, cela implique de caller les brique de lait dans le systeme
#dans un endroit a faible tolérance, et de les arreter, prendre la photo, puis de les relancer, dans un contexte de production, cela est très inéfficace, donc on peut prefere de prendre le
#photo dans l'elan du brique de lait, risquant une décalage, c'est pourquoi on doit reprendre la.
#
#Mais en plus, la methode otsu ne fonctionnera pas correctement, car il y aura beacoup de noir, qui nous rendra le filtre otsu non voulu
#

#binarisation


_, Decoupage_binarized = cv2.threshold(Decoupage_date,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('binarized', Decoupage_binarized)

Decoupe_Copy= np.copy(Decoupage_binarized)


# 5 Extraction du premier Caractère de la date

Contours, _ = cv2.findContours(Decoupage_binarized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
nb_Contours = len(Contours)
print(f"Nombre de Caratéres :{nb_Contours}")



Decoupage_binarized_Contours =cv2.drawContours(Decoupage_binarized, Contours, -1, 125, 3)
cv2.imshow("Contours",Decoupage_binarized_Contours)


img_Extraction = cv2.cvtColor(Decoupage_binarized_Contours,cv2.COLOR_GRAY2BGR)
air_total = 0
for i, contour in enumerate(Contours):
    air = cv2.contourArea(contour)
    air_total += air
    #rectangle englobant chaque Granulats
    x,y,w,h = cv2.boundingRect(contour)
    #position du texte
    text_x = x+w // 2
    text_y = y+h // 2
    #ecriture du numéro
    cv2.putText(img_Extraction,str(i+1), (text_x,text_y),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,255))

        
cv2.imshow("Extrait",img_Extraction)


#Initialisation de l'etalon
Etalon = cv2.imread('1.BMP',cv2.IMREAD_GRAYSCALE)
_,Etalon_Binarisee = cv2.threshold(Etalon,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

height, width = np.shape(Etalon)

print(height)
print(width)

x,y,w,h = cv2.boundingRect(Contours[0])
img_cara_Extraction = Decoupe_Copy[y:y+height,x:x+width] #attention, j'ai rajoutée une ligne de comparaison pour que la dimension correspond

cv2.imshow("Caractere",img_cara_Extraction)
#6
#Q7



# print(np.size(Etalon_Binarisee,axis = 0))
# print(np.size(img_cara_Extraction,axis = 0))

cv2.imshow('Bonjou',Etalon_Binarisee)

difference = cv2.absdiff(img_cara_Extraction,Etalon_Binarisee)
Nb_Pixel_diff= np.count_nonzero(difference)

Pourcentage = Nb_Pixel_diff/np.size(Etalon)*100


print(f"Nombres de pixels different {Nb_Pixel_diff}")
print(f"Nombre de pixel dans l'image etalon {np.size(Etalon)}")
print(f"Pourcentage de difference {Pourcentage} %")


if Pourcentage <20 :
    print("caractére correct")
else:
    print("caractére incorrect")
    
    

cv2.waitKey(0)
# Fermeture de toutes les fenêtres ouvertes
cv2.destroyAllWindows()