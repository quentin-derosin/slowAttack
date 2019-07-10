# Python pour la securite
  - ### [1. Introduction](#1-Introduction)
  - ### [2. Fonctionnement](#2-Fonctionnement)
  - ### [3. Difficultees rencontrees](#3-Difficultees-rencontrees)
  - ### [4. Ameliorations](#4-Ameliorations)

## 1. Introduction
> Slow loris attack
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


## 3. Difficultees rencontrees


## 4. Ameliorations
