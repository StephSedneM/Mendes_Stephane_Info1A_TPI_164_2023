"""Gestion des "routes" FLASK et des données pour les personne.
Fichier : gestion_personne_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for


from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.themesujet.gestion_themesujet_wtf_forms import FormWTFAjouterThemeSujet
from APP_FILMS_164.themesujet.gestion_themesujet_wtf_forms import FormWTFDeleteThemeSujet
from APP_FILMS_164.themesujet.gestion_themesujet_wtf_forms import FormWTFUpdateThemeSujet

@app.route("/themesujet/<string:order_by>/<int:id_theme_avoir_sujet_sel>", methods=['GET', 'POST'])
def themesujet_afficher(order_by, id_theme_avoir_sujet_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_theme_avoir_sujet_sel == 0:
                    strsql_themesujet_afficher = """
                        SELECT theme_avoir_sujet.id_theme_avoir_sujet, t_sujet.Nom_sujet, t_theme.Nom_Theme
                        FROM theme_avoir_sujet
                        INNER JOIN t_sujet ON theme_avoir_sujet.Fk_theme = t_sujet.id_sujet
                        INNER JOIN t_theme ON theme_avoir_sujet.Fk_sujet = t_theme.id_theme
                        ORDER BY theme_avoir_sujet.id_theme_avoir_sujet ASC
                    """

                    mc_afficher.execute(strsql_themesujet_afficher)
                elif order_by == "ASC":

                    valeur_id_theme_avoir_sujet_selected_dictionnaire = {"value_id_theme_avoir_sujet_selected": id_theme_avoir_sujet_sel}
                    strsql_themesujet_afficher = """SELECT * FROM theme_avoir_sujet WHERE id_theme_avoir_sujet = %(value_id_theme_avoir_sujet_selected)s"""

                    mc_afficher.execute(strsql_themesujet_afficher, valeur_id_theme_avoir_sujet_selected_dictionnaire)
                else:
                    strsql_themesujet_afficher = """
                        SELECT theme_avoir_sujet.id_theme_avoir_sujet, t_sujet.Nom_sujet, t_theme.Nom_Theme
                        FROM theme_avoir_sujet
                        INNER JOIN t_sujet ON theme_avoir_sujet.Fk_theme = t_sujet.id_sujet
                        INNER JOIN t_theme ON theme_avoir_sujet.Fk_sujet = t_theme.id_theme
                        ORDER BY theme_avoir_sujet.id_theme_avoir_sujet DESC
                    """


                    mc_afficher.execute(strsql_themesujet_afficher)

                data_themesujet = mc_afficher.fetchall()

                print("data_themesujet ", data_themesujet, " Type : ", type(data_themesujet))

                # Différencier les messages si la table est vide.
                if not data_themesujet and id_theme_avoir_sujet_sel == 0:
                    flash("""La table "theme_avoir_sujet" est vide. !!""", "warning")
                elif not data_themesujet and id_theme_avoir_sujet_sel > 0:
                    flash(f"La personne demandé n'existe pas !!", "warning")
                else:
                    flash(f"Voici les thèmes liés aux sujets!!", "success")

        except Exception as Exception_themesujet_afficher:
            raise ExceptionpersonneAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{themesujet_afficher.__name__} ; "
                                          f"{Exception_themesujet_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("themesujet/themesujet_afficher.html", data=data_themesujet)


@app.route("/themesujet_ajouter", methods=['GET', 'POST'])
def themesujet_ajouter_wtf():
    form = FormWTFAjouterThemeSujet()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_theme = form.nom_theme_wtf.data.lower()
                nom_sujet = form.nom_sujet_wtf.data.lower()

                valeurs_insertion_dictionnaire = {
                    "value_nom_theme": nom_theme,
                    "value_nom_sujet": nom_sujet
                }
                print("valeurs_insertion_dictionnaire", valeurs_insertion_dictionnaire)

                strsql_insertheme_avoir_sujet = """
                    INSERT INTO theme_avoir_sujet (id_theme_avoir_sujet, fk_theme, fk_sujet)
                    VALUES (NULL, (SELECT id_theme FROM t_theme WHERE Nom_theme = %(value_nom_theme)s), 
                                 (SELECT id_sujet FROM t_sujet WHERE Nom_sujet = %(value_nom_sujet)s))
                """

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insertheme_avoir_sujet, valeurs_insertion_dictionnaire)

                flash("Données insérées !!", "success")
                print("Données insérées !!")

                return redirect(url_for('themesujet_afficher', order_by='DESC', id_theme_avoir_sujet_sel=0))

        except Exception as Exception_personne_ajouter_wtf:
            raise ExceptionpersonneAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                             f"{themesujet_ajouter_wtf.__name__} ; "
                                             f"{Exception_personne_ajouter_wtf}")

    return render_template("themesujet/themesujet_ajouter_wtf.html", form=form)






"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /personne_update
    
    Test : ex cliquer sur le menu "personne" puis cliquer sur le bouton "EDIT" d'un "personne"
    
    Paramètres : sans
    
    But : Editer(update) un personne qui a été sélectionné dans le formulaire "personne_afficher.html"
    
    Remarque :  Dans le champ "name_personne_update_wtf" du formulaire "personne/personne_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/themesujet_update", methods=['GET', 'POST'])
def themesujet_update_wtf():
    id_theme_avoir_sujet_update = request.values['id_theme_avoir_sujet_btn_edit_html']

    form_update = FormWTFUpdateThemeSujet()

    try:
        if request.method == "POST" and form_update.submit.data:
            nom_theme_update = form_update.nom_theme_update_wtf.data
            nom_sujet_update = form_update.nom_sujet_update_wtf.data

            valeur_update_dictionnaire = {
                "value_nom_theme": nom_theme_update,
                "value_nom_sujet": nom_sujet_update,
                "value_id_theme_avoir_sujet": id_theme_avoir_sujet_update
            }

            str_sql_update_id_theme_avoir_sujet = """
                UPDATE theme_avoir_sujet AS tas
                INNER JOIN t_sujet ON tas.Fk_theme = t_sujet.id_sujet
                INNER JOIN t_theme ON tas.Fk_sujet = t_theme.id_theme
                SET tas.nom_theme = %(value_nom_theme)s,
                    tas.value_nom_sujet = %(value_nom_sujet)s
                WHERE tas.id_theme_avoir_sujet = %(value_id_theme_avoir_sujet)s
            """

            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_id_theme_avoir_sujet, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")

            return redirect(
                url_for('themesujet_afficher', order_by="ASC", id_theme_avoir_sujet_sel=id_theme_avoir_sujet_update))

        elif request.method == "GET":
            str_sql_id_theme_avoir_sujet = """
                SELECT theme_avoir_sujet.id_theme_avoir_sujet, t_sujet.Nom_sujet, t_theme.Nom_Theme
                FROM theme_avoir_sujet
                INNER JOIN t_sujet ON theme_avoir_sujet.Fk_theme = t_sujet.id_sujet
                INNER JOIN t_theme ON theme_avoir_sujet.Fk_sujet = t_theme.id_theme
                ORDER BY theme_avoir_sujet.id_theme_avoir_sujet ASC
            """
            valeur_select_dictionnaire = {"value_id_theme_avoir_sujet": id_theme_avoir_sujet_update}

            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_theme_avoir_sujet, valeur_select_dictionnaire)

            data_themesujet = mybd_conn.fetchone()

            form_update.nom_theme_update_wtf.data = data_themesujet["Nom_theme"]
            form_update.nom_sujet_update_wtf.data = data_themesujet["Nom_sujet"]

    except Exception as Exception_personne_update_wtf:
        raise ExceptionpersonneUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                         f"{themesujet_update_wtf.__name__} ; "
                                         f"{Exception_personne_update_wtf}")

    return render_template("themesujet/themesujet_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /personne_delete
    
    Test : ex. cliquer sur le menu "personne" puis cliquer sur le bouton "DELETE" d'un "personne"
    
    Paramètres : sans
    
    But : Effacer(delete) un personne qui a été sélectionné dans le formulaire "personne_afficher.html"
    
    Remarque :  Dans le champ "name_personne_delete_wtf" du formulaire "personne/personne_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/themesujet_delete", methods=['GET', 'POST'])
def themesujet_delete_wtf():
    data_films_attribue_personne_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_theme_avoir_sujet"
    id_theme_avoir_sujet_delete = request.values['id_theme_avoir_sujet_btn_delete_html']

    # Objet formulaire pour effacer le personne sélectionné.
    form_delete = FormWTFDeleteThemeSujet()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("personne_afficher", order_by="ASC", id_theme_avoir_sujet_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "personne/personne_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_personne_delete = session['data_films_attribue_personne_delete']
                print("data_films_attribue_personne_delete ", data_films_attribue_personne_delete)

                flash(f"Effacer le personne de façon définitive de la BD !!!", "On s'en fou non?")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer personne" qui va irrémédiablement EFFACER le personne
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_theme_avoir_sujet": id_theme_avoir_sujet_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)


                str_sql_delete_idpersonne = """DELETE FROM theme_avoir_sujet WHERE id_theme_avoir_sujet = %(value_id_theme_avoir_sujet)s"""


                # Manière brutale d'effacer d'abord la "fk_personne", même si elle n'existe pas dans la "theme_avoir_sujet_film"
                # Ensuite on peut effacer le personne vu qu'il n'est plus "lié" (INNODB) dans la "theme_avoir_sujet_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_idpersonne, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idpersonne, valeur_delete_dictionnaire)

                flash(f"personne définitivement effacé !!", "success")
                print(f"personne définitivement effacé !!")

                # afficher les données
                return redirect(url_for('personne_afficher', order_by="ASC", id_theme_avoir_sujet_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_theme_avoir_sujet": id_theme_avoir_sujet_delete}
            print(id_theme_avoir_sujet_delete, type(id_theme_avoir_sujet_delete))

            # Requête qui affiche tous les films_personne qui ont le personne que l'utilisateur veut effacer
            str_sql_personne_films_delete = """SELECT *FROM theme_avoir_sujet
                                                        Where id_theme_avoir_sujet = %(value_id_theme_avoir_sujet)s"""


            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_personne_films_delete, valeur_select_dictionnaire)
                data_films_attribue_personne_delete = mydb_conn.fetchall()
                print("data_films_Nom_personne_delete...", data_films_attribue_personne_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personne/personne_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_personne_delete'] = data_films_attribue_personne_delete

                # Opération sur la BD pour récupérer "id_theme_avoir_sujet" et "intitule_personne" de la "theme_avoir_sujet"
                str_sql_id_theme_avoir_sujet = "SELECT id_theme_avoir_sujet, Nom_personne, Prenom_personne FROM theme_avoir_sujet WHERE id_theme_avoir_sujet = %(value_id_theme_avoir_sujet)s"

                mydb_conn.execute(str_sql_id_theme_avoir_sujet, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "name personne" pour l'action DELETE
                data_Nom_personne = mydb_conn.fetchone()
                print("data_Nom_personne ", data_Nom_personne, " type ", type(data_Nom_personne), " personne ",
                      data_Nom_personne["Nom_personne"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "personne_delete_wtf.html"
            form_delete.nom_personne_delete_wtf.data = data_Nom_personne["Nom_personne"]

            # Le bouton pour l'action "DELETE" dans le form. "personne_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_personne_delete_wtf:
        raise ExceptionpersonneDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{themesujet_delete_wtf.__name__} ; "
                                      f"{Exception_personne_delete_wtf}")

    return render_template("themesujet/themesujet_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_personne_delete)
