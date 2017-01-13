# Remarques
Cette version permet de savoir la meilleure position d'un site donnée dans "site web" parmi les resultats de google suite a une reqûte saisie dans le champ mot cles ("1 mot clé"), cela en recuperant le premier resultat contenant notre adresse du domaine a surveiller

pour changer la profondeur, on itère autant de fois que la profondeur donnée, tout en changeant la valeur de "start" dans notre google URL

Pour le parsing des resultats google il faut ajouter BeautifulSoup avec "pip install BeautifulSoup".

il faut egalement installer flask et flask_wtf

une fois le dossier des sources télécharhé il faut y'aller au repertoire de sauvegarde et taper python app.py, l'application va se lancer en local

au navigateur taper: localhost:5000/

Les améliorations:
  1. recherche avec plusieurs mots clés
  2. Sauvegarder les résultats dans une base de donées
  3.Telecharger les resultats sous forme de ficheir csv

Bugs
   1 fixer le bug des validators
