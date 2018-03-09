# Front-end, le site web

* Squelette
  * Contenu du site en HTML
* Respect de la charte graphique du client
  * CSS
  * Bootstrap
* Communication avec les data en back-end
  * Liste des évènements
  * Liste des participants
  * Liste des utilisateurs et de leurs droits
* Portail des évènements en cours
* Possibilité pour les utilisateurs de gérer leur compte
* Possibilité pour les utilisateurs ayant les droits suffisants de gérer les
  évènements
  * Création d'évènements
  * Importation et exportation des listes des participants

# Système de gestion de la base de données

* Import/Export de BDD postgresql
  * Permettra de faire des tests et d'avoir des copies
* Entités
  * évènement, utilisateurs, etc.
* "Interface"
  * Vues SQL, Fonctions pour Django

# Back-end, Django

* Communication avec la BDD

# Fichiers XLS

* Importation de fichiers au format XLS
  * Les associations doivent pouvoir utiliser leurs propres billetteries en ligne
    et gérer leurs évènements sur le site
  * Lors de l'évènement, les achats de billets sur place doivent pouvoir être
    rajoutés à la liste en ligne afin d'obtenir la liste des participants par la
    suite
* Exportation de fichiers au format XLS

# Ce que le client doit fournir

* Liste des membres des associations avec leur RÔLE.

# billetterie

* Paiement sécurisé
  * API PayPal
* génération du billet avec QR code
  * Respect de la charte graphique de l'école

# Envoi de courriel automatisé utilisateur

* Génération de courriel avec
  * billet électronique
  * informations sur l'évènement

# Gestion des comptes utilisateurs

* Compte EPITA (OpenID Connect)
  * Les utilisateurs sans adresse EPITA, mais avec un compte IONIS peuvent-ils
    utiliser OpenID Connect?
* Compte externe (sans adresse EPITA/IONIS)

# Vérification pendant les évènements

* Application mobile pour scanner les billets
* possibilité pour la billetterie physique d'ajouter les nouveaux participants à
  la liste du site
  * Utilisation d'une fonction d'import d'une liste XLS à la liste déjà
    existante (fusion)
