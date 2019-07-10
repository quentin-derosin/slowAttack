# Python pour la securite
  - ### [1. Introduction](#1-Introduction)
  - ### [2. Fonctionnement](#2-Fonctionnement)
  - ### [3. Difficultees rencontrees](#3-Difficultees-rencontrees)
  - ### [4. Ameliorations](#4-Ameliorations)

## 1. Introduction

 L'attaque slow loris permet de faire un ddos sur un serveur en se servant que d'une seule machine. 
 Slowloris essaie de garder le maximum de connexions ouvertes avec le webserver cible et essaie de les garder ouvertes aussi longtemps que possible. 
 Dès que le slowloris a ouvert une connection il va garder la garder ouverte en envoyant des requêtes incomplètes qu'il va compléter lentement au fur et à mesure mais ne les finira jamais. 
 Les serveurs affectés verront leur nombre maximum de connections atteint et peuvent refuser les nouvelles connections d'utilisateurs.
Les serveurs majoritairement touchés par l'attaque slowloris sont:
- Apache 1.x and 2.x
- dhttpd
- Flask

Il existe des modules pour apache qui permetent de réduire la chance d'une attaque slowloris tel que: 
- mod_limitipconn
- mod_qos, mod_evasive
- mod security
- mod_noloris
- mod_antiloris

Il existe d'autres méthodes pour se protéger tel qu'installer un:
- reverse proxy
- firewall
- load balancer
- content switches

Si aucune de ces solutions n'est envisageable il est toujours possible de placer son webserver derrière un nginx ou lighthttpd qui ne sont pas affectés par cette attaque.
## 2. Fonctionnement
Afin de faire fonctionner ce programme, il est necessaire d'installer certaines dependances. Les commandes a executer pour avoir un environnement d'execution sont les suivantes :
 * `virtualenv env`
 * `source env/bin/activate`
 * `pip install -r requirements.txt`

 Dans un premier temps, il est necessaire de recuperer le type de serveur que l'on souhaite attaquer : 
 * Par exemple, un serveur apache 1.x/2.x permettra une attaque optimal.
 * A contrario, attaquer un WebServeur tournant avec le framework NodeJS a partir de la version 8 est inutile

 Pour recuper le type de serveur, on envoie une requete get : </br>
 * `sock.send("GET / HTTP/1.1\r\n\r\n".encode("ascii"))`</br>

Puis on analyse le retour </br>
*  `HTTP/1.1 400 Bad Request
Date: Wed, 10 Jul 2019 16:18:53 GMT
Server: Apache/2.4.29 (Ubuntu)
Content-Length: 301
Connection: close
Content-Type: text/html; charset=iso-8859-1
`


## 3. Difficultees rencontrees


## 4. Ameliorations
Les améliorations possibles sont nombreuses:
- Détection automatique du serveur et optimisation des paramètres.
- Détection automatique du timeout serveur pour les requêtes.
- Détection du nombre de connection maximum du serveur pour pouvoir choisir le niveau de ddos que l'on veut (un peu, beaucoup, moyen)
- Utilisation de proxy pour permettre d'ouvrir un plus grand nombre de connections quand il y a un nombre limité par utilisateur.
