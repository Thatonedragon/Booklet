---
layout: default
nav_order: 1
title: Recherche operationel
has_children: true
---


# Cours recherche opérationelle


{: .note }
Premier cours en markdown

Recherche des solution des problèmes graces a l'informatique, en trouvant la solution optimale.

Donc il faut des algorithmes de selection de solution.


1) G doit etre connexe (Diap 20)

2) hbve de sommets de degreé impair doit être egale à 0 ou 2
  * a ->3
  * b ->3
  * c ->3
  * d ->5

sont les nombres de sommet de degré impair = 4

* a' ->4
* b' ->3
* c' ->4
* d'-> 5





## définitions:

{: .def-title}
>graphe complet
>
>un graphe est complet si quelsque soient deux sommets distincts, il existe un arc (ou une arête) les reliant dans un sens ou dans l'autre (lorsqu’on a un graphe orienté), ne contient pas de boucle.


{: .def-title}
>distance
>On appelle distance entre deux sommets la longeur de la plus petite chaïne les reliant

{: .def-title}
>diamètre
>
>On appelle diamètre d'un graphe la plus longue des distances entre deux sommets

{: .def-title}
>sous graphe
>
>le graphe G' est une sous grpahe de G si l'ensemble des sommets de G' est inclus dans l'ensemble des sommets de G, et si l'ensemble des arcs de G' est égal au sous-ensemble des arcs de G reliant entre 
eux tous les sommets de G'; on a donc retiré de G certains sommets, et tous les arcs adjacents à ces sommets.

{: .def-title}
>Chemin
>
>Suite d'arcs telle que l'extrémité terminale d'un arc coïncide avec l'extremité intiale de l'arc suivant


Lorsque le graphe est non orienté, la mtircie associée est symétrique par rappot à la diagonale.

Lorsqu'il n'y a pas de boucle, il n'y a que des zéros sur la diagonale.

graphe non orientée: Arrête- chaine(chaine eulerienne) cycle
graphe orientée: Arc -chemin - circuit, (Chemin Hamiltoninien)(somment )

diapo 36
Pour décrire des phénomènes aléatoires se répétant, on peu tutiliser un grpahe et la matirce qui lui est associéee On parle alors de graphe probabiliste ( car en lien avec des calculs de probabilités )

## l'algorithme de dijkstra

Le porblème consite à chercher le plus court chemin entre 
1) un sommet de départ donné et un sommet d'arrivée donné
2) un sommet et tous les autres
3) n sommmets de départ et m sommmets d'arrivée
  
Méthode de Dijkstra

```psoeudo
Un graphe G
un Sommet de départ s
    x-> poid(x)
    x-> y(x,y)
    S = l'ensemble des sommmets du graphe
    π <- ∅

début 
    tant que π =/ S
      choisir un sommet n'appartenent pas a π de poids minimum
      π <- π u {x}
      pour tout voisin y de x n'appartenant pas à π
          si poids(x)+ valeur(x y)< poids (y)
          alors     poids (y)<- poids (x)+valeur (x y)
                    mémoriser en y que l'on vient de x
          fin si
      fin pour tout
    fin tant que
```

On part de S vers b

| sommets | s | a    | b    | c    | d    | ou fixe sommet |
|---------|---|------|------|------|------|----------------|
| debut   | 0 | \inf | \inf | \inf | \inf | on garde S     |
| étape 1 | / | 8(s) | \inf | \inf | 2(s) | on garde d     |
| étape 2 | / | 6(d) | \inf | 4(d) | /    | on garde c     |
| étape 3 | / | 5(c) | 6(c) | /    | /    | on garde a     |
| étape 4 | / | /    | 6(c) | /    | /    | on garde b     |

d'ou les chemins:
- de s vers d; direct de coût 2
- de s vers c; de s vers d puis de d vers c (total 4)
- de s vers b; de s vers d puis de d veers c puis de c vers b (total 6)
- de s vers a; de s vers d puis de d vers c puis de c vers a (total 5) 