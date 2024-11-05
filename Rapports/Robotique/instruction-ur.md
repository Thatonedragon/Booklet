---
layout: default
nav_order: 1
title: instruction utilisation UR-10
parent: Presentation UR-10
grand_parent: Rapport robotique
---


## Creation de repère outil

### Objectif du réglage outil

Le but est de définir le TCP (Tool Center Point), c'est-à-dire le point précis de l'outil qui interagit avec l'environnement (par exemple, la pointe d'un stylo ou l'extrémité d'un pistolet à souder). Le réglage en 3 points aide à déterminer la position du TCP par rapport au poignet du robot (flange), en tenant compte des décalages et de l'orientation de l'outil.

Le réglage outil en 3 points est une méthode couramment utilisée en robotique pour définir avec précision la position et l'orientation d'un outil monté sur le bout du bras robotique (la bride d'outil). Cette méthode permet au robot de connaître la position exacte de l'outil dans son espace de travail, ce qui est essentiel pour des tâches précises comme l'assemblage, la soudure ou la manipulation d'objets.

### Étapes du réglage outil en 3 points
#### Point 1 – Position initiale :

Le robot est déplacé manuellement pour amener l'extrémité de l'outil (le TCP) à une position spécifique sur un objet fixe. Le robot enregistre cette position comme référence initiale.
#### Point 2 – Rotation sur un axe (généralement Z) :

Le robot est ensuite déplacé autour de l'axe Z (ou un autre axe choisi), tout en gardant l'extrémité de l'outil (TCP) au même endroit. Cette rotation permet de définir l'orientation de l'outil par rapport à l'axe principal. Le robot enregistre cette deuxième position.
#### Point 3 – Rotation sur un autre axe :

Enfin, une rotation autour d'un second axe (souvent X ou Y) est effectuée, toujours en maintenant le TCP en place. Cela permet de finaliser la définition des décalages et des rotations de l'outil. Le robot enregistre la troisième position.

![Texte alternatif](/Rapports/Robotique/photo/repère%203%20points.png "Le titre de mon image")

### Comment cela fonctionne
En déplaçant l'outil et en le faisant tourner autour de points fixes (TCP), le robot peut calculer les décalages (translations) et les rotations nécessaires pour définir la position exacte du TCP et de l'orientation de l'outil par rapport à la bride du robot.
Les trois points de référence permettent de créer un modèle précis de l'outil dans l'espace du robot, en tenant compte de la géométrie spécifique de cet outil.
### Avantages du réglage outil en 3 points
Précision : Cette méthode permet d'obtenir une précision élevée dans la localisation de l'outil, garantissant des opérations fiables et exactes.
Simplicité : Comparée à d'autres méthodes plus complexes comme le réglage en 6 points (TCP plus orientation complète), le réglage en 3 points est relativement simple et rapide à mettre en œuvre.
Flexibilité : Cette méthode peut être utilisée avec divers types d'outils, qu'ils soient de forme complexe ou simple.
En résumé, le réglage en 3 points est une technique fondamentale pour garantir que le robot connaît parfaitement la position et l'orientation de l'outil qu'il manipule, assurant ainsi des opérations précises et répétables.

Afin de commencer le réglage, nous entrons dans l’onglet installation, général puis sélectionner PCO(TCP en anglais)
En premier lieu, nous allons sur position puis mesurer ( Réglage coordonnées de l’outil grâce à 3 points espacé de 120° autour du point de réglage)
En second temps, nous nous portons sur orientation pour son orientation de l’axe Z de l’outil
Après réglage de l’axe Z par rapport au plan de base(pointe de l’outil situé vers le haut), nous lançons une vérification des déplacements.

![Texte alternatif](/Rapports/Robotique/photo/ExtraitDocUR.jpg "Le titre de mon image")

## création du plan 

Explication II :
Installation -> fonction -> plan -> prendre un plan a modifier puis l’éditer, on place le plan selon les besoins avec le repère 3D, après validation nous pouvons le tester en sélectionnant déplacement -> fonction -> nom du plan modifiée.


## Creation de plan utilisateur 



Nous allons créer un plan d'utilisateur sur un chemin de test, ce plan aura pour but de définir les point de passage d'un outil attachée au robot.

pour ce faire, nous allons dans la rubrique xxxx, puis on fait les manipulation suivantes:
