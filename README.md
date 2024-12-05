# Contraction des longueurs

## Introduction

Dans la vidéo [Voyage relativiste](https://www.youtube.com/watch?v=1jKPtu5m3DQ), un aperçu de ce qu'on peut appeler la **dilatation du temps** était présenté. Dans cette vidéo, la représentation du **temps propre** le long de la **ligne d'univers** illustre bien ce phénomène.

La notion de **contraction des longueurs** est un peu plus compliquée à illustrer. Préalablement, on peut regarder la vidéo [Simultaneïté](https://www.youtube.com/watch?v=jib6EababqA) qui expose une façon simple de représenter des **évènements** dans l'espace-temps, grâce à des coordonnées $(x,t)$ réduites. Pour simplifier, on envisage toujours une position le long d'une droite, avec une distance $x$ et un temps $t$.

## Description

Un vaisseau se déplace le long d'un axe à la vitesse $v$ dans le référentiel fixe. On place un **point d'observation fixe** à la distance $x$. En ce point, on mesure l'intervalle de temps $\Delta t$ entre le passage de l'avant du vaisseau à l'instant $t$ et le passage de l'arrière.

Il faut donc considérer les deux évènements $(x,t)$ et $(x,t+\Delta t)$ pour étudier ce qui se passe dans le référentiel du vaisseau.

Si on considère des écarts $\Delta x$ et $\Delta t$ entre deux évènements dans le référentiel fixe, les écarts correspondants $\Delta x'$ et $\Delta t'$ dans le référentiel du vaisseau sont :

$$\Delta x'= \gamma\left(\Delta x-v\Delta t\right)$$
$$\Delta t'= \gamma\left(\Delta t-v\Delta x\right)$$

avec

$$\gamma=\dfrac{1}{\sqrt{1-v^2}}$$

Pour le point d'observation fixe, $\Delta x=0$, de sorte que :

$$\Delta x'= -\gamma v\Delta t$$
$$\Delta t'= \gamma\Delta t$$

Dans le référentiel fixe, on peut évaluer la **longueur apparente** $L$ du vaisseau à partir de la vitesse $v$ et de l'intervalle de temps $\Delta t$ mesuré :

$$L=v\Delta t$$

Dans le référentiel du vaisseau, le point de mesure se déplace à la vitesse $-v$ et parcours une distance $\Delta x'$ pendant un temps $\Delta t'$. On accède ainsi à la **longueur vraie** $L'$ du vaisseau :

$$\Delta x'= -L'=-v\Delta t'=-\gamma v\Delta t=-\gamma L$$

Avec $\gamma > 1$, on obtient ainsi une longueur apparente $L$ plus petite que la longueur vraie $L'$ :

$$L=\dfrac{L'}{\gamma}$$

Dans la représentation graphique proposée, on représente un quadrillage avec des mailles de côté $1$ pour les évènements $(x,t)$ dans le référentiel fixe et pour les évènements $(x',t')$ dans le référentiel du vaisseau. L'unité de temps est celle que l'on souhaite et elle impose l'unité de longueur qui est la distance parcourue par la lumière pendant cette unité de temps. On choisit la position $x$ du point de mesure et les deux instants $t_d$ et $t_f$ où on voit passer l'avant puis l'arrière du vaisseau.

## Les programmes

Le programme Python : [cdl.py](cdl.py)

Le notebook : [contraction_des_longueurs.ipynb](contraction_des_longueurs.ipynb)

## Les tracés

```
>>>import cdl
>>>cdl.trace_lu(v=0.6,x=9,td=7,tf=11)

***Résultats***
L =2.4000
L'=3.0000

***Tracé***
```
![cdl06](https://github.com/user-attachments/assets/2229188d-d16e-480c-8e99-229307e969ee)

```
>>>import cdl
>>>cdl.trace_lu(v=0.8,x=16,td=14,tf=17)

***Résultats***
L =2.4000
L'=4.0000

***Tracé***
```
![cdl08](https://github.com/user-attachments/assets/817652d7-1a7c-453b-8b26-d603b52e02b9)


```
>>>import cdl
>>>cdl.trace_lu(v=0.4,x=8,td=6,tf=11)

***Résultats***
L =2.0000
L'=2.1822

***Tracé***
```
![cdl04](https://github.com/user-attachments/assets/129a5bb3-323d-470e-a46a-073ef3043d15)
