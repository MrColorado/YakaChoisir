# Front-end, le site web

* Squelette
  * Contenu du site en HTML
* Respect de la charte graphique du client
  * CSS
  * Bootstrap
* Communication avec les data en back-end
  * Liste des events
  * Liste des participants
  * Liste des utilisateurs et de leurs droits
* Portail des events en cours
* Possibilite pour les utilisateurs de gérer leur compte
* Possibilite pour les utilisateurs ayant les droits suffisants de gérer les
  events
  * Création d'event
  * Importation et exportation des listes des participants

# Système de gestion de la base de données

* Import/Export de BDD postgresql
  * Permettra de faire des tests et d'avoir des copies
* Entités
  * Event, utilisateurs, etc.
* "Interface"
  * Vues SQL, Fonctions pour Django

# Back-end, Django

* Communication avec la BDD

# Fichiers XLS

* Importation de fichiers au format XLS
  * Les associations doivent pouvoir utiliser leurs propres billeteries en ligne
    et gerer leurs evenements sur le site
  * Lors de l'event, les achats de billets sur place doivent pouvoir etre
    rajoute a la liste en ligne afin d'obtenir la liste des participants par la
    suite
* Exportation de fichiers au format XLS

# Ce que le client doit fournir

* Liste des membres des associations avec leur ROLE.

# Billeterie

* Paiement sécurisé
  * API PayPal
* Generation du billet avec QR code
  * Respect de la CG de l'ecole

# Envoi de courriel automatisé utilisateurs

* Génération de courriel avec
  * billet électronique
  * informations sur l'event

# Gestion des comptes utilisateurs

* Compte EPITA (OpenID Connect)
  * Les utilisateurs sans adresse EPITA mais avec un compte IONIS peuvent-ils
    utiliser OpenID Connect?
* Compte externe (sans adresse EPITA/IONIS)

# Vérification pendant les events

* Application mobile pour scanner les billets
* Possibilite pour la billeterie physique d'ajouter les nouveaux participants a
  la liste du site
  * Utilisation d'une fonction d'import d'une liste XLS a la liste deja
    existante (fusion)
