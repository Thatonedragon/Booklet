---
layout: default
nav_order: 3
title: Presentation Fanuc
parent: Rapport robotique
has_children: true
---

# Fanuc M-10iA et M-710ic

## introduction
Ces 2 robot, construit par fanuc, sont utilisée dans la mini usine pour manipuler les boites rempli et de les ranger dans des cartons

## Fanuc M-10iA

Le Fanuc M-10iA est un robot industriel de petite taille, polyvalent et compact, utilisé principalement dans les applications de manutention et d’assemblage. Voici ses principales caractéristiques :

Charge utile : 10 kg
Portée maximale : 1 420 mm
Axes : 6 axes
Précision : ± 0,03 mm
Applications courantes : manutention de matériaux, assemblage, emballage, palettisation, test de qualité, etc.
Avantages : grande vitesse, répétabilité élevée, faible encombrement, ce qui en fait une solution idéale pour des tâches nécessitant une haute précision dans des espaces restreints.

![Texte alternatif](/Rapports/Robotique/photo/Fanuc%20M-10iA.jpg "Le titre de mon image")

## Fanuc M710ic

Le Fanuc M-710iC est un robot industriel polyvalent, capable de gérer des charges plus importantes, souvent utilisé dans des environnements de production diversifiés. Il existe en plusieurs variantes en fonction des besoins (longue portée, haute charge, etc.). Voici ses caractéristiques générales :

Charge utile : entre 20 et 70 kg (selon le modèle)
Portée maximale : 2 050 à 3 123 mm
Axes : 6 axes
Précision : ± 0,04 mm
Applications courantes : soudage, peinture, palettisation, enlèvement de matière, usinage, etc.
Avantages : structure compacte et rigide, idéale pour des opérations lourdes et complexes avec une portée longue et une grande capacité de charge.

![Texte alternatif](/Rapports/Robotique/photo/Fanuc%20M710ic.jpg "Le titre de mon image")

# Fanuc ER-4iA et Fanuc CRX-10iA

## Fanuc ER-4iA

Le Fanuc ER-4iA est un robot industriel compact conçu pour des applications de haute précision dans des environnements où l'espace est limité. C'est un robot léger et rapide, idéal pour les petites charges et les tâches minutieuses. Voici ses principales caractéristiques :

Charge utile : 4 kg
Portée maximale : 550 mm
Axes : 6 axes
Précision : ± 0,01 mm
Applications courantes : manipulation de petites pièces, assemblage, emballage, test de produits électroniques, etc.
Avantages : extrêmement compact et léger, avec une grande flexibilité pour les tâches de précision dans des espaces réduits. Il est souvent utilisé dans les secteurs de l'électronique et des biens de consommation.

![Texte alternatif](/Rapports/Robotique/photo/Fanuc%20ER-4iA.jpg "Le titre de mon image")

## Fanuc CRX-10iA

Le Fanuc CRX-10iA est un robot collaboratif (cobot) conçu pour travailler en toute sécurité aux côtés des humains. Il est parfait pour des applications où la collaboration homme-robot est essentielle. Ce modèle fait partie de la gamme de cobots de Fanuc, connue pour sa facilité d’utilisation et sa sécurité. Voici ses caractéristiques principales :

Charge utile : 10 kg
Portée maximale : 1 249 mm
Axes : 6 axes
Précision : ± 0,04 mm
Applications courantes : assemblage, emballage, chargement/déchargement de machines, palettisation, manipulation de matériaux, etc.
Avantages : le CRX-10iA est conçu pour être facile à programmer, même pour des utilisateurs novices, grâce à son interface intuitive. Il offre une sécurité avancée avec des capteurs qui permettent au robot de s'arrêter en cas de contact avec un humain. Il peut être intégré dans des environnements collaboratifs sans nécessiter de cages de sécurité.


Ces deux robots sont spécialisés pour des applications légères, avec l'ER-4iA se concentrant sur la précision dans les espaces restreints et le CRX-10iA permettant une collaboration sécurisée avec les opérateurs humains.

![Texte alternatif](/Rapports/Robotique/photo/Fanuc%20CRX-10iA.jpg "Le titre de mon image")


# Le teach pendant

Le teach pendant (ou pupitre de commande) est l'interface de contrôle principale d'un robot industriel Fanuc, permettant à l'opérateur de programmer, surveiller et contrôler les mouvements et les tâches du robot de manière intuitive. Ce dispositif portable se connecte directement au contrôleur du robot et offre diverses fonctionnalités pour manipuler et configurer le robot en fonction des besoins de production.

L'interface est organisée en plusieurs sections et onglets pour accéder facilement aux programmes, aux configurations de mouvement, aux diagnostics et aux paramètres d'E/S (entrées et sorties).

Le teach pendant Fanuc est équipé de boutons permettant de déplacer les axes du robot en mode manuel (ou mode jog). Ces boutons facilitent le positionnement du robot dans des repères spécifiques (joint, world, tool, user).
![Texte alternatif](/Rapports/Robotique/photo/teach-fanuc.png "Le titre de mon image")

Les boutons d’arrêt d’urgence, de sécurité et de validation sont aussi intégrés pour une utilisation sécurisée. Ils permettent d’arrêter le robot immédiatement en cas d’urgence.
![Texte alternatif](/Rapports/Robotique/photo/teach-fanuc2.png "Le titre de mon image")

## Mode "Teach" et "Playback" :

* En mode teach, l’opérateur peut déplacer manuellement le robot pour enregistrer une série de points (positions) et d'actions, formant ainsi un programme de mouvement. L’opérateur guide physiquement le robot d’une position à une autre et enregistre chaque point, qui sera ensuite suivi en mode automatisé.

* En mode playback, le robot exécute les mouvements programmés automatiquement selon les points définis en mode teach. Cela permet de vérifier la précision des déplacements avant de lancer le robot en production.


Le teach pendant permet d’accéder à l’interface de programmation en langage TP (Teach Pendant), propre à Fanuc. Ce langage de haut niveau permet d’écrire des programmes pour contrôler les mouvements, les interactions avec des capteurs, et d’autres actions complexes.
On peut y programmer des instructions de déplacement (MOVE, L MOVE pour les déplacements linéaires, J MOVE pour les déplacements en joint), des commandes conditionnelles (IF, THEN), des boucles (WHILE), et des instructions de manipulation des entrées/sorties (E/S) pour interagir avec d’autres dispositifs.

Donc le teach pendant Fanuc est un outil central pour la programmation et la manipulation de robots industriels. Grâce à sa capacité à permettre le teach mode (programmation manuelle) et à intégrer des fonctions avancées de diagnostic et de sécurité, il simplifie grandement le travail des opérateurs. Le teach pendant permet une programmation rapide et précise, essentielle pour les applications industrielles où la flexibilité et la sécurité sont cruciales.
