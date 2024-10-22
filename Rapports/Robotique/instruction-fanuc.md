---
layout: default
nav_order: 2
title: instruction utilisation Fanuc
parent: presentation fanuc
---




## Mise en route
En toute logique, quand un opérateur arrive en usine eteint, les robots sont éteint, il faut alors les alummer grace aux contacteurs de puissances.


## Manipulation
Pour utiliser le robot, nous avons une ordinateur mobile a notre disposition, donc grace a ça, nous pouvons configurer le robot.

L'opérateur place ca main dans la partie basse de la commande, appui a micourse l'ordinateur de bord, puis commence a faire ses reglages.

### Déplacement simple
l'opérateur appuie a mi course l'ordinateur de bord, et appui sur reset, cela d&éverouille le déplacement grace au bouton en répere prédefinie en haut a droite de l'écran.

Il doit appuyerr sur shift pour utiliser les boutons bleu, qui a l'occurence, sont les boutons de mouvement du robot.

### Déplacement programmée
Pour crée un programme il faudra ce rendre sur le menu select puis apuier sur F2[create]
un fois le programme crée et nommé il suffira de selectioner EDIT afin d'écrire notre programme ,Il faudra dans un premier temps inserer des ligne en appuiant sur F5(insert)
Pour ajouter une ligne il faudra simplement déplacer le robot ,une fois au bonne position il faudra faire next puis F1 (point) et choisir le mouvement ,ici on a le chois entre Joint ou Linear 



### Lancement du programme 

IL faut depuis le menu select sectionner notre programme et appuies sur step puis appuier sur shift et FWR en même temps 


### Utilisation du préhenseur ventouse
menu IO > et robot puis on evite de toucher à "découplage" car ela fait tomber la pince de FANUC 710.

Il y a 2 entrée sorties sur les IO par robot

* Sur le robot 710ic, il faut changer les deux etats pour que le pince change d'état
* Sur le robot 101iA, on peux controler les deux états des 2 groupes de ventouses, c'est a dire que les 2 groupes sont activable en même temps en ventouses

### exercice
Mettre la boite dans le carton



