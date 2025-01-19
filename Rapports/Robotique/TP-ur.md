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

Avant de programmer les déplacements du cobot, il est nécéssaire de créer le plan sur lequel l'outil du robot va travailler. Cela permet de définir une origine autour de laquelle le robot va travailler.
Ainsi si les mouvements effectués avec l'outil se devaient de changer de psotion par rapport au robot mais en restant identique en terme mouvement que ceux originelement programmé (par exemple si le robot est déplacer), il sera uniquement nécéssaire changer les coordonnées de l'origine du plan. 
Les déplacements enregistré par rapport à ce plan s'addapteront automatiquement au nouveau plan généré évitant ainsi de devoir à nouveau programmer les déplacements de l'outil du cobot. 

## Création d'un repère outil

A la suite de cela, il est nécéssaire de créer le repère outil. 
Il permet au robot de connaitre la position et l'orientation de l'outil avec lequel il va travailler. Il pourra alors adapter ces mouvements en fonction de l'outil. 

[Tutoriel création plan/repère outil](instruction-ur.md)


## Programmation en point de passage

Un programme peut être créé via l'interface graphique afin de faire répéter des déplacements au cobot. 
Plusieurs points de passage peuvent ainsi être déterminés. Le cobot va alors déplacé l'outil de points en points afin de faire suivre la trajectoire souhaitée par l'utilisateur. 
On distingue trois catégories de déplacement possibles entre les points de passage :
  - *'Déplacement P'* correspond à un déplacement ou le robot va utiliser la trajectoire la plus rapide entre les deux points de passages.
  - *'Déplacement L'* correspond à un déplacement linéaire.  
  - *'Déplacement A'* correspond à un déplacement en arc. 

Chacun de ces déplacements est une catégorie de mouvements, les points de passage sont placés à l'intérieur des déplacements dans le programme.

Il est également possible de créer des déplacements en cercle dans la catégorie 'déplacement P' en indiquant le rayon correspondant dans les options de celui-ci. 

Pour ne pas endommager le cobot sur le long terme, il ne faut pas engendrer de secousse lors du déplacement de l'outil entre les points de passages. 
Pour cela, les points de passage doivent se situer dans le même type de déplacement. 
Dans notre cas, nous avons utilisé les déplacements P, ce qui permet de créer des mouvements circulaires, comme précédemment cité. 
En combinant les trajectoire circulaire et les deplacement en trajectoire classique il est possible de suivre convenablement une trajectoire souhaité par l'utilisateur.
En n'utilisant qu'un seul type de déplacement, il n'y a pas d'arrêt du robot et donc pas de secousse. Celle-ci apparaissent lors d'un changement de type de deplacement.


# Suivi d'un tracé sur une feuille

Le principe de ce TP est de faire suivre à la pointe de l'outil du robot le tracé d'une feuille de papier posée horizontalement sur un plan. 

Le chemin à suivre est le suivant :
![Texte alternatif](./photo/IMG20241105111948.jpg "Le titre de mon image")

## Programmation du cobot

Pour suivre le tracé, il faut d'abord créer le plan sur lequel le robot va travailler, puis le repère outil. 
Il faut ensuite créer un nouveau programme pouyr acceder aux déplacements. 
Une fois le robot débloqué pour le déplacer manuellement, il faut amener l'outil à son point de départ.
Enregistrer ce point, puis amener l'outil à son deuxième point de passage, enregistrer et répéter l'opération sur tous les points où le robot doit se rendre. 


Si l'outil doit suivre une trajectoire en cercle, un onglet permet de le faire en enregistrant trois points du cercle (le point de départ, l'arrivée et un point intermédiaire). 
À l'aide des trois points enregistrés, le robot déterminera le rayon du cercle et le reproduira comme sur la vidéo ci-dessous.

<video width="320" height="240" controls>
  <source src="./photo/VID20241022091631.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>

En combinant des trajectoires circulaires et standart, il est possible de suivre toutes les trajectoires de la feuille. 

<video width="320" height="240" controls>
  <source src="./photo/VID20241022101134.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>


Pour des projets plus complexes, il est possible de créer des sous-programmes afin d'éviter d'avoir à écrire plusieurs fois la même fonction. 
De même, il est possible de contrôler les actionneurs à l'aide de fonctions pré-enregistrés. 

# Suivi d'une barre métallique

Ce sujet est similaire aux précédents, à la différence près que le plan n'est plus perpendiculaire au sol et que les tracés sont différents. 

![Texte alternatif](./photo/IMG20241105115317.jpg "Le titre de mon image")


De la même manière que pour le suivi de ligne, il faut commencer par créer un nouveau plan en fonction de l'origine de la barre métallique, puis créer le repère outil. 
Les trajectoires que doit suivre le robot sont alors déterminées par les points de passage définis. 
Les types de déplacements restent identiques, avec des déplacements p et la fonction cercle lorsque cela est nécessaire.    



