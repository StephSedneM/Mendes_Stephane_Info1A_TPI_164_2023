"""
    Fichier : gestion_personne_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterPersonne(FlaskForm):
    """
        Dans le formulaire "personne_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_personne_wtf = StringField("Inserez le Nom", validators=[Length(min=2, max=30, message="min 2 max 30"),
                                                                   Regexp(nom_personne_regexp,
                                                                    message="Bien Essayé, mais juste des lettres stp")
                                         ])
    prenom_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_personne_wtf = StringField("Inserez le Prenom", validators=[Length(min=2, max=30, message="min 2 max 20"),
                                                                 Regexp(prenom_personne_regexp,
                                                                        message="J'ai dit...que des lettres")


                                                        ])
    submit = SubmitField("Valider")

class FormWTFUpdatePersonne(FlaskForm):
    nom_personne_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_personne_update_wtf = StringField("Inserer le Nom", validators=[Length(min=2, max=20, message=""),
                                                                       Regexp(nom_personne_update_regexp,
                                                                              message="Essaye Encore mais que avec des lettres")
                                                                       ])
    prenom_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_personne_wtf_essai = StringField("Insérer le Prénom", validators=[
        Length(min=1, max=20, message="Min 1 max 20"),
        Regexp(prenom_personne_regexp, message="Chiffre et lettre uniquement (pas de caractères spéciaux)")])

    date_personne_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                                 DataRequired("Date non valide")])

    submit = SubmitField("Valider")

class FormWTFDeletePersonne(FlaskForm):
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
