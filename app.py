# -*- coding: utf-8 -*-
import re
from flask import Flask, render_template, request, flash
from forms import ScrapForm
import sys
import requests
from result import Result

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/scrap', methods = ['GET', 'POST'])
def main():
   form = ScrapForm()
   
   
   if request.method == 'POST':
        _motcle=request.form['mot_cle']
        #_lismc=_motcle.split(" ")
       
        
        headers = {'user-agent': 'Mozilla/5.0'}
        _list=[]
        _links=[]
        #profondeur de recherche
        _profondeur=int(request.form['profondeur'])
        
        #parcourir les pages en fonction de la profondeur
        for start in range(0,_profondeur):
            find=None
            url = "http://www.google.fr/search?hl=fr&q="+str(_motcle)+"&start="+str(start*10)+"&filter=0"
            pge=requests.get(url,headers=headers)
            #utilisation de beautifulsoup pour le parsing
            soup = BeautifulSoup(pge.content)
            #recuperation des liens: tous les liens sont tagues par cite
            lien=soup.findAll('cite')
            position=0
            #variable find verifie si on a trouve un resultat ou pas initialement faux
            find=None
            #sauvegarde des liens retournes par google
            for li in lien:
              _links.append(li.text)
        
        #chercher notre site web parmi les liens resultat 
        for li in _links:
              position+=1
              if request.form['url'] in li and not find:
                res = Result(request.form['url'],li,position)
                res.mot_cle=_motcle
                res.url=li
                res.position=position
                _list.append(res)
                find=True
                
        #si on a pas trouve de liens on assigne NA au resultat
        if not find:
                res = Result(_motcle,"NA","0")
                res.mot_cle=_motcle
                res.url="NA"
                res.position="NA"
                _list.append(res)		
  
        return render_template('scrap.html', pages=_list, form=form)
   else:
         return render_template('scrap.html', form = form)

if __name__ == '__main__':
   sys.path.append("./BeautifulSoup")
   from BeautifulSoup import BeautifulSoup
   app.run(debug = True)
