"""
    Fichier : gestion_sujet_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp



class FormWTFAjoutersujet(FlaskForm):
    """
        Dans le formulaire "sujet_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_sujet_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_sujet_wtf = StringField("Inserez le Titre du Sujet", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_sujet_regexp,
                                                                    message="Bien Essayé, mais juste des lettres stp")
                                         ])

    submit = SubmitField("Valider")

class FormWTFUpdatesujet(FlaskForm):
    nom_sujet_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_sujet_update_wtf = StringField("Inserer le Nom", validators=[Length(min=2, max=50, message=""),
                                                                       Regexp(nom_sujet_update_regexp,
                                                                              message="Essaye Encore mais que avec des lettres")
                                                                       ])


    date_sujet_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                                 DataRequired("Date non valide")])

    submit = SubmitField("Valider")

class FormWTFDeletesujet(FlaskForm):
    """
        Dans le formulaire "sujet_delete_wtf.html"

        nom_sujet_delete_wtf : Champ qui reçoit la valeur du sujet, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "sujet".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_sujet".
    """
    nom_sujet_delete_wtf = StringField("Titre du Sujet")
    submit_btn_del = SubmitField("Effacer")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ? Sinon click la == >>")
    submit_btn_annuler = SubmitField("Annuler")
