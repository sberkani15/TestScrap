#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ScrapForm(Form):
   url = TextField("Site Web",[validators.Required("Please enter a web site url.")])
   mot_cle = TextAreaField("Mots cle")
   profondeur = IntegerField("Profoneurde recherche :")
   submit = SubmitField("Lancer le crawl")
