Prev () | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | () Next
- - -

***Table des matières***

    * [Démarrage rapide](#Démarrage)
    * [Caractéristiques importantes de QMS](#Caractéristiques-importantes-de-QMS)
    * Télécharger des fichiers depuis Internet
    * Installation
    * Étapes après le premier démarrage
    * Quelques étapes de travail typiques
            * Déplacer et agrandir la carte
            * Charger le fichier GPX et afficher les données
            * Créer une base de données
            * Organisation des données dans la base de données
            * Créer une trace
            * Afficher les informations de piste
            * Créer une trace (route) à l'aide de waypoints
            * Trouver un waypoint

* * * * * * * * * *
			 
# Démarrage rapide
___(Instructions en français pour les utilisateurs de Windows)___

_valide à partir du commit QMapShack 8ddec3217899 (mercredi 04 avril 17:38:39 2018 +0200)_

_À l'exception des parties liées à l'installation de QMapShack lui-même, ces instructions s'appliquent également aux systèmes d'exploitation non Windows._

QMapShack (QMS en abrégé) pour Windows est une application 64 bits et nécessite donc un système d'exploitation Windows 64 bits.

Ces instructions sont aussi courtes que possible afin d'initier rapidement l'utilisateur au travail avec QMS. De nombreuses actions décrites peuvent également être exécutées sous d'autres formes. Il n'y a pas de discussion à ce sujet.

Des informations détaillées sur QMS peuvent être trouvées dans le wiki en anglais.

Les utilisateurs qui disposent d'un QMS déjà installé trouveront une page d'accueil lorsqu'ils démarreront le système pour la première fois et pourront directement effectuer les différentes étapes d'installation décrites sur cette page à partir de là.

## Caractéristiques importantes de QMS

* Utilisation simple et flexible des cartes vectorielles, matricielles et en ligne
* Utilisation des données d'altitude (hors ligne et en ligne)
* Génération / planification d'itinéraires et de pistes avec différents routeurs
* Évaluation des données enregistrées (traces) de divers appareils de navigation et de fitness
* Modification des itinéraires et des tracés planifiés
* Stockage structuré des données dans des bases de données ou des fichiers
* Connexion directe en lecture et en écriture à des équipements de navigation et de fitness modernes
	 
## Télécharger des données depuis Internet

_Conseils:_

* Les numéros de version mentionnés sont susceptibles d'être modifiés. La dernière version disponible doit être sélectionnée.  
* Souvent, des fichiers pour des régions spécifiques peuvent être sélectionnés sur les pages spécifiées. L'utilisateur doit sélectionner la région qui l'intéresse.
* Les recommandations faites ici sont des exemples. Il y a beaucoup plus de choix!

Les liens suivants sont des recommandations pour les données qui facilitent l'utilisation de QMS et qui peuvent être téléchargées à partir d'Internet.

* _QMapShack:_

   * [Chargez le fichier d'installation de QMS à partir du serveur](https://github.com/Maproom/qmapshack/releases "QMS Installationsdatei laden"). Chargez le fichier QMapShack_Win64bit_1.14.0.exe à partir de cette page (environ 100 Mo, le numéro de version peut être différent).

* _Prise en charge de la carte (recommandée)_ :

     * [Chargez la carte vectorielle de l'Allemagne (Freizeitkarte)](http://download.freizeitkarte-osm.de/garmin/latest/DEU_de_gmapsupp.img.zip "Freizeitkarte Deutschland"). (Lien direct vers un fichier, environ 1,4 Go! Si un appareil de navigation Garmin est utilisé, un fichier `gmapsupp*.img` approprié peut déjà être disponible et peut être utilisé pour cette étape).
     * _Facultatif:_ [Chargez les liens cartographiques en ligne](http://www.mtb-touring.net/qms/onlinekarten-einbinden/ "Online-Karten"). Remarque: cliquez sur le champ Télécharger les cartes en ligne! Fournit le fichier `Onlinemaps.zip`.

* _Prise en charge du routage (recommandé pour créer de nouvelles routes)_:
     * [Chargez les données Routino](http://download.geofabrik.de/europe/germany.html "Routino-Daten laden"). Sur cette page, par ex. allez à la ligne `Berlin` et cliquez sur `.osm.pbf` dans cette ligne. Fournit le fichier `berlin-latest.osm.pbf`.

* _Données d'altitude (recommandées si des informations d'altitude sont requises pour de nouveaux itinéraires)_:
 
     * [Chargez les tuiles pour les données d'altitude](https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/ "Einzelne Kacheln"). Sélectionnez le(s) fichier(s) approprié(s) en utilisant les coordonnées, par ex. `N51E012.hgt.zip`. Les coordonnées données décrivent le coin sud-ouest d'une tuile.

        Ou:

     * [Chargez les données d'altitude pour les régions](http://www.viewfinderpanoramas.org/Coverage%20map%20viewfinderpanoramas_org3.htm "DEM Höhendaten für Regionen"). Sélectionnez la région appropriée sur la carte affichée et cliquez dessus. Par exemple un fichier `N32.zip` sera téléchargé. `N32` est le nom de la zone nommée UTM.

    _Remarque:_ tous les fichiers requis pour la région sélectionnée doivent être téléchargés !

## Installation

* Tous les fichiers téléchargés se trouvent généralement dans le répertoire Téléchargements de l'utilisateur.
* Recherchez le fichier QMapShack_Install_Windows64bit__1.14.0.exe dans le répertoire de téléchargement.
* Démarrez ce fichier d'installation en double-cliquant sur le nom du fichier.
* Confirmez les informations dans les premières fenêtres d'installation.
* Dans la fenêtre `Sélectionner les composants`, l'élément d'exécution `MSVC ++ 2013 SP1 runtime` doit être sélectionné (cela peut être omis si cet environnement d'exécution est déjà installé sur l'ordinateur utilisé).
* Confirmez le début de l'installation de l'environnement d'exécution. Remarque: l'installation peut prendre quelques minutes !
* À la fin de l'installation de l'environnement d'exécution, cette installation doit se terminer par `Close`. L'installation de QMS se poursuivra alors et QMS sera entièrement installé.
* **Attention:** *Les caractères non ASCII ne peuvent pas être utilisés dans les noms des répertoires d'installation !*
* QMS peut déjà être démarré via le menu Démarrer. Cependant, il est recommandé d'effectuer les étapes suivantes au préalable.
* Créez un répertoire dans lequel l'utilisateur a un accès en écriture. Dans la suite de ce mode d'emploi, ce répertoire est appelé `QMS`. _Remarque:_ L'utilisateur ne dispose pas des droits d'écriture complets pour le répertoire d'installation standard, donc un répertoire distinct pour les données doit être créé à cette étape.
* Créez les sous-répertoires suivants dans le répertoire QMS:
        * `Maps`,
        * `Routino`,
        * `BRouter`,
        * `DEM`,
        * `Databases`,
        * `GPX`.
* Ouvrez le fichier `DEU_de_gmapsupp.img.zip` avec la carte des loisirs de l'Allemagne et copiez le fichier `gmapsupp.img` qu'il contient dans le répertoire `Maps`.
* Renommez le fichier `gmapsupp.img` en `Freizeitkarte_DE.img`.
* _Facultatif:_ Ouvrez le fichier `Onlinemaps.zip` et copiez les fichiers qu'il contient dans le répertoire `Maps`.
* _Facultatif:_ Déplacez le fichier `berlin-latest.osm.pbf` dans le répertoire `Routino`.
* _Facultatif:_ Ouvrez le fichier `N51E012.hgt.zip` ou `N32.zip` et copiez les fichiers qu'il contient dans le répertoire `DEM`.
