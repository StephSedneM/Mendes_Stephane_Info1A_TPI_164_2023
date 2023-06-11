"""
    Fichier : gestion_personne_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjouterThemeSujet(FlaskForm):
    """
        Dans le formulaire "personne_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_sujet_regex = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ\s]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"
    nom_sujet_wtf = StringField("Inserez le sujet", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_sujet_regex,
                                                                    message="Bien Essayé, mais juste des lettres stp")
                                         ])
    nom_theme_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ\s]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"
    nom_theme_wtf = StringField("Inserez le thème", validators=[Length(min=2, max=30, message="min 2 max 20"),
                                                                 Regexp(nom_theme_regexp,
                                                                        message="J'ai dit...que des lettres")


                                                        ])
    submit = SubmitField("Valider")

class FormWTFUpdateThemeSujet(FlaskForm):

    nom_sujet_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_sujet_update_wtf = StringField("Insérer le Sujet", validators=[
        Length(min=2, max=50, message=""),
        Regexp(nom_sujet_update_regexp, message="Essaye Encore mais que avec des lettres")
    ])

    nom_theme_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_theme_update_wtf = StringField("Insérer le Thème", validators=[
        Length(min=1, max=20, message="Min 1 max 20"),
        Regexp(nom_theme_regexp, message="Chiffre et lettre uniquement (pas de caractères spéciaux)")
    ])

    submit = SubmitField("Valider")


class FormWTFDeleteThemeSujet(FlaskForm):
    """
        Dans le formulaire "personne_delete_wtf.html"

        nom_personne_delete_wtf : Champ qui reçoit la valeur du personne, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "personne".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_personne".
    """
    nom_personne_delete_wtf = StringField("Nom de l'Alien")
    submit_btn_del = SubmitField("Effacer l'Alien")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ? Sinon click la == >>")
    submit_btn_annuler = SubmitField("Annuler")
