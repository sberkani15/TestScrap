# Remarques
Cette version permet de savoir la meilleure position d'un site donné dans "site web" parmi les resultats de google suite a un ensemble de requêtes saisies dans le champ mot cles, cela en recuperant le premier resultat google contenant notre adresse du domaine a surveiller

pour changer la profondeur, on itère autant de fois que la profondeur donnée, tout en changeant la valeur de "start" dans notre google URL

Pour le parsing des resultats google il faut ajouter BeautifulSoup avec "pip install BeautifulSoup".

il faut egalement installer flask et flask_wtf

une fois le dossier des sources télécharhé il faut y'aller au repertoire de sauvegarde (sur la console) et taper python app.py, l'application va se lancer en local

au navigateur taper: localhost:5000/

pour les mots clés il faut toujour faire "Entree" pour que le script comprenne qu'il faut passer au prochain mot clé

A faire encore:
  1. Sauvegarder les résultats dans une base de donées
  2. Telecharger les resultats sous forme de fichier csv
  3. Nettoyage du code
  
 Amelioration:
 1. Temps de réponse
 2. Verification des positions

Bugs
   1 fixer le bug des validators
   2 l'encodage ascii
