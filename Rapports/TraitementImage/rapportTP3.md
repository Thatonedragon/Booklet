---
layout: default
nav_order: 2
title: TP3
parent: Rapport Traitement Images
---

# TP3 

## Introduction

OpenCV ne permet pas seulement de traiter des images fixe, mais aussi une suite d'images, c'est a dire une vidéo, et c'est le sujet de ce TP3.
Nous avons 2 fichiers, un image, et un video, et en construisant l'alorgithme de traitement sur un image fixe
nous pouvons en faire une simple fonction pour traiter les images de la video un a un.

## Travail sur l'image fixe

Comme dans les 2 TP précedents, nous allons recuperer l'image avec 

```python
Image_Bille = cv2.imread("boules.png")
```
### Question 10

L'attribut shape de Numpy permet de recuperer les dimension de l'images, ainsi que le nombre de caneaux qui definisent le couleur


```python
taille_x, taille_y, nbr_canneaux = np.shape(Image_Bille)

print(f'Taille de x {taille_x}')
print(f'Taille de y {taille_y}')
print(f'Taille de canneaux {nbr_canneaux}')

```
output:
```
Taille de x 
Taille de y 
Taille de canneaux 3
```