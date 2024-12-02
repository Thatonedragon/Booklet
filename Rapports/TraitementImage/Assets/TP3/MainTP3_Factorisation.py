import cv2
import numpy as np


def findCercleRouge(Image):
    Image_HSV  = cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)
    I = 8
    rouge_inferieur = np.array([0,50,50])
    rouge_superieur = np.array([I,255,255])
    rouge_inferieur_2 = np.array([180-I,50,50])
    rouge_superieur_2 = np.array([180,255,255])
    Masque_1 = cv2.inRange(Image_HSV,rouge_inferieur,rouge_superieur)
    Masque_2 = cv2.inRange(Image_HSV,rouge_inferieur_2,rouge_superieur_2)
    Masque_totale = cv2.bitwise_or(Masque_1,Masque_2)
    el_struct = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
    Ouverture = cv2.morphologyEx(Masque_totale,cv2.MORPH_OPEN,el_struct)
    Fermeture = cv2.morphologyEx(Ouverture,cv2.MORPH_CLOSE, el_struct)
    Countours, _ = cv2.findContours(Fermeture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in Countours:
        (x,y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x),int(y))
        radius = int(radius)
        #print(center)
        cv2.circle(Image, center, radius, (0,255,0),2)
    cv2.imshow('TP3', Image)
    
    
Image_Bille = cv2.imread("boules.png",)

findCercleRouge(Image_Bille)

cap = cv2.VideoCapture('billes.mp4')
    # Vérifier si succès
if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la vidéo.")
    exit()

while True:
    # Lire une frame de la vidéo
    ret, frame = cap.read()
    # Vérifier si la fin de la vidéo n'est pas atteinte
    if not ret:
        break
    
    # Afficher la frame
    findCercleRouge(frame)
    
    # Attendre 100 millisecondes avant de passer à la frame suivante
    cv2.waitKey(100)
    # Libérer les ressources de la vidéo et fermer la fenêtre d'affichage

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()