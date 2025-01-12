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

## Code et explications


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
nous procédons ensuite au Découpe de la brique de lait qui se fait très simplement avec ces prochains lignes de code

```python 

Decoupage = img[Bordure_Gauche:Bordure_Droite, Bordure_Superieur:Bordure_Inferieur]

cv2.imshow('Decoup', Decoupage)


#decouper la date
Decoupage_date = Decoupage[303:303+95 , 57:57+41]

```

## Question 6

Tout depend de comment la photo est prise et si on peut toujours avoir la photo dans le même angle, même position sur l'image, cela implique impérativement d'avoir les briques de laits au même placement a chaque fois,
dans un endroit a faible tolérance, et de les arreter, prendre la photo, puis de les relancer, dans un contexte de production, cela est très inéfficace, donc on peut preferer de prendre la photo dans l'elan du brique de lait, risquant une décalage, c'est pourquoi on doit reprendre les quateres cotés de la brique.

Mais en plus, la methode otsu ne fonctionnera pas correctement, car il y aura beacoup de noir, qui nous retorunera un filtre otsu non adaptée.


## Question 7

La taille des images de 1 sont differentes, cela empeche une comparaison entre les 2 images, la méthodologie utilisée ici est un rajout du nombre de lignes manquant depuis l'image a analyser, une balayage sur quelques lignes serais encore plus fiables si jamais on a pris le mauvais décalage (le 1 décalée trop décalée au lieu de super posée).

## Question 8
Si on travaillerai avec l'intégralité de la date, il vaudrai mieux faire un etalon de cette date entiere, l'imprimante imprimera toujour le même ecart entre les caracteres, donc il est probablement plus facile de comparer un tel etalon face a la photo, que de comparer chaque caratérer.
et comme ennoncé dans la question précedente, on peux effectuer une legere balayage de quelques pixels pour s'assurer une bonne superposistion de l'etalon et l'image lors de la difference, on prendra la valeur la plus haute, et on devra definir une seuil de confiance plus faible en vue du nombre de pixel.

## Question 9
Un seul de décision nécésite de nombreuses test, avec 2 echantillions c'est completement absurde, cela pourrai introduire une seuil de confiance trop haute, alors qu'en réalité, nous pouvons avoir des imperfection sur l'étiquette
