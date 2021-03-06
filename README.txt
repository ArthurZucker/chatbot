Chatbot Game of Thrones

Ce dossier regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.

Version de python nécessaire :

Ce programme a été testé avec Python 3.7.3. Il necessite Python 3 pour fonctionner.

Paquets nécessaires :

Pour utiliser ce programme, il est nécessaire de posséder les packets suivants inscrits dans le fichier requirements.txt


Exécution :

Pour exécuter ce programme, il faut décomprésser le fichier chatbot.zip.
Installer les paquets nécessaires grâce à la commande :
make install
et exécuter le fichier principal grâce à la commande :
make
ou, si une erreur est renvoyée :
make run


Documentation :

La documentation du programme est accessible en ouvrant le fichier doc.html.

Ontologie :

L'ontologie a été créée avec protégé (https://protege.stanford.edu/). Le fichier ontology_graphe.png est un graphe des classes de l'ontologie. Le fichier ontologyGoT.pdf est un graphe des classes et des instances de l'ontologie.

Liste des instances présentes dans l'ontologie :

Arryn
Arya_Stark
Baratheon
Benjen_Stark
Beyond_The_Wall
Bolton
Brandon_Stark
Cersei_Lannister
Daenerys_Targaryen
Dorne
Drowned_God
Eddard_Stark
Faith_Of_The_Seven
Frey
Great_Stallion
Greyjoy
Jaqen_h_ghar
Jon_Snow
Lannister
Lord_Of_Light
Lyanna_Stark
Many_Faced_God
Martell
Oberyn_Martell
Old_Gods
Rhaegar_Targaryen
Rickard_Stark
Rickon_Stark
Robb_Stark
Sansa_Stark
Stark
Targaryen
The_Crownlands
The_Iron_Islands
The_North
The_Reach
The_Riverlands
The_Stormlands
The_Vale
The_Westerlands
Theon_Greyjoy
Tully
Tyrell
Tyrion_Lannister
Tywin_Lannister

Modes de saisie :

Il y a 3 modes de saisie :
- un mode sur une seule ligne avec la syntaxe suivante :
`instance1,propriete,instance2?`

- un mode sur 3 lignes pour chacune des entrees

- un mode où la question est posée librement

Le chatbot est capable de corriger la requête s'il y figure des fautes légères.

Pour les deux premiers modes de saisie, la réponse est cherchée dans l'ontologie. Pour le dernier, la réponse est cherchée dans une base de donnée.

Interface graphique :

Toute l'interface graphique est regroupée dans le fichier source/ui.py. Elle a été réalisée grâce au module easygui.
