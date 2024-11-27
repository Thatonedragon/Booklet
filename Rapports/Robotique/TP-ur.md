---
layout: default
nav_order: 2
title: TP ur
parent: Presentation UR-10
grand_parent: Rapport robotique
grand_grand_parent: Rapports
---

# Préparation du cobot

## Création d'un plan

Avant de programmer les déplacements du cobot, il est nécéssaire de créer le plan sur lequel l'outil va travailler. 
Ainsi si les mouvements effectués avec l'outil se devaient de rester identique mais à un autre endroit que celui originalement programmé, il sera uniquement nécéssaire changer les coordonnée de l'origine du plan. 
Les déplacements enregistré par rapport à ce plan s'addapteront automatiquement au nouveaux plan généré évitant ainsi de devoir à nouveau programmer les déplacements du cobot. 

## Création d'un repère outil

A la suite de cela, il est nécéssaire de créer le repère outil. 
Il permet au robot de connaitre la position et l'orientation de l'outil avec lequel il va travailler. 


## Explication des différents mode

Un programme peut être créé via l'interface graphique afin de faire répéter des déplacements au robot. 
Plusieurs points de passage stratégiques peuvent ainsi être déterminés afin de faire suivre la trajectoire souhaitée à l'outil. 
On distingue trois catégories de déplacement possibles entre les points de passage :
  - 'Déplacement P' correspond à un déplacement ou le robot va utiliser la trajectoire la plus courte en les deux points de passages  
  - 'Déplacement L' correspond à un déplacement linéaire  
  - 'Déplacement A' correspond à un déplacement en arc 

Chacun de ces déplacements est une catégorie de mouvements et les points de passage sont placés à l'intérieur des déplacements dans le programme.

Il est également possible de créer des déplacements en cercle en indiquant le rayon correspondant dans les options de déplacement P. 

Pour ne pas endommager le cobot sur le long terme, il ne faut pas engendrer de secousse lors du déplacement de l'outil. 
Pour cela, les différents points de passage doivent se situer dans le même type de déplacement. 
Dans notre cas, nous avons utilisé les déplacements P, ce qui permet de créer des mouvements circulaires, comme précédemment cité. 
Ceux-ci ne sont disponibles que dans les déplacements P. 
En n'utilisant qu'un seul type de déplacement, il n'y a pas d'arrêt du robot et donc pas de secousse. 
En effet, les secousses apparaissent notamment lors d'un changement de type de déplacement.



# Suivi d'un tracé sur une feuille

Le principe de ce TP est de faire suivre à la pointe de l'outil du robot le tracé d'une feuille de papier posée horizontalement sur un plan. 

Le chemin à suivre est le suivant :
![Texte alternatif](./photo/IMG20241105111948.jpg "Le titre de mon image")

## Programmation du cobot

Pour suivre le tracé, il faut d'abord créer le plan sur lequel le robot va travailler, puis le repère outil. 
Il faut ensuite créer un nouveau programme, puis un déplacement. 
Une fois le robot débloqué pour le déplacer manuellement, il faut amener l'outil à son point de départ.
Enregistrer ce point, puis amener l'outil à son deuxième point de passage, enregistrer et répéter l'opération sur tous les points où le robot doit se rendre. 
Si l'outil doit suivre une trajectoire en cercle, un onglet permet de le faire en enregistrant trois points du cercle (le point de départ, l'arrivée et un point intermédiaire). 
À l'aide des trois points enregistrés, le robot déterminera le rayon du cercle et le reproduira.  
Pour des projets plus complexes, il est possible de créer des sous-programmes afin d'éviter d'avoir à écrire plusieurs fois la même fonction. 
De même, il est possible de contrôler les actionneurs à l'aide de fonctions pré-enregistrés. 


<video width="320" height="240" controls>
  <source src="./photo/VID20241022091631.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>

En combinant des trajectoires circulaires et linéaires, il est possible de suivre toutes les trajectoires de la feuille. 

<video width="320" height="240" controls>
  <source src="./photo/VID20241022101134.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>

# Suivi d'une barre métallique

Ce sujet est similaire aux précédents, à la différence près que le plan n'est plus perpendiculaire au sol et que les tracés sont différents. 

![Texte alternatif](./photo/IMG20241105115317.jpg "Le titre de mon image")


De la même manière que pour le suivi de ligne, il faut commencer par créer un nouveau plan en fonction de l'origine de la barre métallique, puis créer le repère outil. 
Les trajectoires que doit suivre le robot sont alors déterminées par les points de passage définis. 
Les types de déplacements restent identiques, avec des déplacements p et la fonction cercle lorsque cela est nécessaire.    



