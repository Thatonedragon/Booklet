---
layout: default
nav_order: 2
title: TP2
parent: Rapport Traitement Images
---

# TP2 - Etude de la date de péremption d'un brique de lait

## Introduction

Le traitement d'image a son utilité dans la reconnaisance de charactére automatisée, cela implique de comparer une image d'un caractere a une image Etalon.
Dans ce TP, nous avons une image d'une étiquette de brique de lait, et nous allons extraire la premiere chiffre de cette image. La question finale est de savoir si c'est une
date qui commence avec un chiffre 1 ou pas.

## Le calcul des projections 


```python
#lire l'image
img = cv2.imread('LAIT_OK.bmp',cv2.IMREAD_GRAYSCALE)

#Prendre la somme en ligne des valeurs de pixels
projection_ligne = np.sum(img,axis = 0)

#valeur max de cette ligne
valeur_max_ligne = np.max(projection_ligne)

#procédée idem
projection_colonne = np.sum(img,axis = 1)
valeur_max_colonne = np.max(projection_colonne)
print(f"Valeur Max ligne {valeur_max_ligne}")
print(f"Valeur Max colonne {valeur_max_colonne}")
```

On commence par lire l'image et de directement l'avoir en nuance de gris.
Grace au fonction de numpy, nous pouvons avoir les projections de l'image, que nous tracons dans des courbes grace a la libraire matplotlib


```python
plt.plot(projection_ligne)
plt.plot(projection_colonne)
plt.show()
``` 
Pour ensuite tourver l'emplacement de l'étiquette sur l'image, nous allons définir des seuils, nous allons considerer que le seuil est une division par 2 du maximum.
Puis nous allons extraire les premiere et dernieres valeurs pour définir nos bordures.

```python
valeur_seuil_front_colonne = valeur_max_colonne/2
valeur_seuil_front_ligne = valeur_max_ligne/2

Bordure_Superieur = np.where(projection_ligne> valeur_seuil_front_ligne)[0][0] #Tu n'a que la premiere valeur du tableau
Bordure_Inferieur = np.where(projection_ligne> valeur_seuil_front_ligne)[0][-1] #Tu a la derniere valeur du tableau 
Bordure_Gauche = np.where(projection_colonne > valeur_seuil_front_colonne)[0][0] 
Bordure_Droite = np.where(projection_colonne > valeur_seuil_front_colonne)[0][-1]
#En ayant ces 4 valeurs, on peux retrouver les 4 coins du rectangle
#Peut etre faire mieux plus tard quand l'image n'est pas réelement droit
``` 




