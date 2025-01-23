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

Avant de programmer les déplacements du cobot, il est nécessaire de créer le plan sur lequel l'outil du robot va travailler. Cela permet de définir une origine autour de laquelle le robot va travailler.
Ainsi, si les mouvements effectués avec l'outil doivent changer de position par rapport au robot sans que les mouvements ne diffèrent de ceux qui étaient originellement programmés (par exemple, si le robot est déplacé), il suffira de modifier les coordonnées de l'origine du plan. 
Les déplacements enregistrés par rapport à ce plan s'adapteront automatiquement au nouveau plan généré, évitant ainsi d'avoir à nouveau programmer les déplacements de l'outil du cobot. 

## Création d'un repère outil

Il est nécessaire de créer un repère outil pour chaqu'un des outils que le cobot pourrait être amener à manipuler.  
Celui-ci permet au robot de connaître la position et l'orientation de l'outil qu'il va utiliser. Il pourra alors adapter ses mouvements en fonction de l'outil. 

[Tutoriel création plan/repère outil](instruction-ur.md)


## Programmation en points de passage

Un programme peut être créé via l'interface graphique afin de faire répéter des déplacements au cobot. 
Plusieurs points de passage peuvent ainsi être définis. Le cobot se déplace alors de point en point avec l'outil afin de suivre la trajectoire souhaitée par l'utilisateur. 
On distingue trois catégories de déplacement possibles entre deux points de passage :
  - *'Déplacement P'* correspond à un déplacement ou le robot va utiliser la trajectoire la plus rapide entre les deux points de passages.
  - *'Déplacement L'* correspond à un déplacement linéaire.  
  - *'Déplacement A'* correspond à un déplacement en arc. 

Chacun de ces déplacements constitue une catégorie de mouvements, et les points de passage sont placés à l'intérieur de ces déplacements dans le programme.

Il est également possible de créer des déplacements en cercle dans la catégorie « déplacement P » en indiquant le rayon correspondant dans les options de cette catégorie. 

Pour éviter d'endommager le cobot sur le long terme, il ne faut pas provoquer de secousse lors du déplacement de l'outil entre les points de passage. 
Pour cela, les points de passage doivent se situer dans le même type de déplacement. 
Dans notre cas, nous avons utilisé les déplacements P, ce qui permet de créer des mouvements circulaires, comme nous l'avons précédemment indiqué en plus des déplacements standard. 
En combinant des trajectoires circulaires et des déplacements en trajectoire classique, il est possible de suivre convenablement une trajectoire souhaitée par l'utilisateur.
En n'utilisant qu'un seul type de déplacement, le robot ne s'arrête pas et ne provoque donc aucune secousse. Celles-ci apparaissent lors d'un changement de type de déplacement.

# Suivi d'un tracé sur une feuille

L'objectif de ce TP est d'amener l'outil du robot à suivre le tracé d'une feuille de papier posée horizontalement sur un plan. 

Le chemin à suivre est le suivant :
![Texte alternatif](./photo/IMG20241105111948.jpg "Le titre de mon image")

## Programmation du cobot

Pour suivre le tracé, il faut d'abord créer le plan sur lequel le robot va travailler, puis le repère outil. 
Il faut ensuite créer un nouveau programme pour accéder aux déplacements. 
Une fois le robot débloqué pour le déplacer manuellement, il faut amener l'outil à son point de départ.
Enregistrer ce point, puis amener l'outil au deuxième point de passage, enregistrer et répéter l'opération sur tous les points où le robot doit se rendre. 


Si l'outil doit suivre une trajectoire en cercle, un onglet permet de le faire en enregistrant trois points du cercle (le point de départ, l'arrivée et un point intermédiaire). 
À l'aide des trois points enregistrés, le robot déterminera le rayon du cercle et le reproduira comme l'illustre la vidéo ci-dessous.

<video width="320" height="240" controls>
  <source src="./photo/VID20241022091631.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>

En combinant des trajectoires circulaires et standard, il est possible de suivre toutes les trajectoires de la feuille. 

<video width="320" height="240" controls>
  <source src="./photo/VID20241022101134.mp4" type="video/mp4">
  Votre navigateur ne supporte pas les vidéos HTML5.
</video>


Pour des projets plus complexes, il est possible de créer des sous-programmes afin d'éviter d'avoir à réécrire plusieurs fois la même fonction. 
Il est également possible de contrôler les actionneurs à l'aide de fonctions préenregistrées. 

# Suivi d'une barre métallique

Ce sujet est similaire aux précédents, à la différence près que le plan n'est plus perpendiculaire au sol et que les tracés sont différents. 

![Texte alternatif](./photo/IMG20241105115317.jpg "Le titre de mon image")


De la même manière que pour le suivi de ligne, il faut commencer par créer un nouveau plan en fonction de l'origine de la barre métallique, puis créer le repère outil. 
Les trajectoires que doit suivre le robot sont alors déterminées par les points de passage définis. 
Les types de déplacements restent identiques, avec des déplacements p et la fonction cercle lorsque cela est nécessaire.    



