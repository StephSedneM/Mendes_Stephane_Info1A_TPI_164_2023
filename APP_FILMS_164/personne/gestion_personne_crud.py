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
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFAjouterPersonne
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFDeletePersonne
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFUpdatePersonne

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /personne_afficher
    
    Test : ex : http://127.0.0.1:5575/personne_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_personne_sel = 0 >> tous les personne.
                id_personne_sel = "n" affiche la personne dont l'id est "n"
"""


@app.route("/personne_afficher/<string:order_by>/<int:id_personne_sel>", methods=['GET', 'POST'])
def personne_afficher(order_by, id_personne_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_personne_sel == 0:
                    strsql_personne_afficher = """SELECT * FROM t_personnes ORDER BY id_personne ASC"""
                    mc_afficher.execute(strsql_personne_afficher)

                elif order_by == "ASC":

                    valeur_id_personne_selected_dictionnaire = {"value_id_personne_selected": id_personne_sel}
                    strsql_personne_afficher = """Select * From t_personnes WHERE id_personne = %(value_id_personne_selected)s"""

                    mc_afficher.execute(strsql_personne_afficher, valeur_id_personne_selected_dictionnaire)
                else:
                    strsql_personne_afficher = """SELECT * FROM t_personnes ORDER BY id_personne DESC"""

                    mc_afficher.execute(strsql_personne_afficher)

                data_personne = mc_afficher.fetchall()

                print("data_personne ", data_personne, " Type : ", type(data_personne))

                # Différencier les messages si la table est vide.
                if not data_personne and id_personne_sel == 0:
                    flash("""La table "t_personnes" est vide. !!""", "warning")
                elif not data_personne and id_personne_sel > 0:
                   flash(f"La personne demandé n'existe pas !!", "warning")
                else:
                    flash(f"Voici les humains qui ont souffert!!", "success")

        except Exception as Exception_personne_afficher:
            raise ExceptionpersonneAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{personne_afficher.__name__} ; "
                                          f"{Exception_personne_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("personne/personne_afficher.html", data=data_personne)

@app.route("/personne_ajouter", methods=['GET', 'POST'])
def personne_ajouter_wtf():
    form = FormWTFAjouterPersonne()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                Nom_personne_wtf = form.nom_personne_wtf.data
                Nom_personne = Nom_personne_wtf.lower()


                Prenom_personne_wtf = form.prenom_personne_wtf.data
                Prenom_personne = Prenom_personne_wtf.lower()


                valeurs_insertion_dictionaire = {"Value_Prenom_personne": Prenom_personne_wtf}
                valeurs_insertion_dictionnaire = {"value_Nom_personne": Nom_personne_wtf, "Value_Prenom_personne": Prenom_personne_wtf}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_personnes = """INSERT INTO t_personnes (id_personne,Nom_personne,Prenom_personne) VALUES (NULL, %(value_Nom_personne)s, %(Value_Prenom_personne)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_personnes, valeurs_insertion_dictionnaire)


                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('personne_afficher', order_by='DESC', id_personne_sel=0))



        except Exception as Exception_personne_ajouter_wtf:
            raise ExceptionpersonneAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{personne_ajouter_wtf.__name__} ; "
                                            f"{Exception_personne_ajouter_wtf}")

    return render_template("personne/personne_ajouter_wtf.html", form=form)




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


@app.route("/personne_update", methods=['GET', 'POST'])
def personne_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_personne"
    id_personne_update = request.values['id_personne_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatePersonne()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "personne_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.

            nom_personne_update = form_update.nom_personne_update_wtf.data
            prenom_personne_update = form_update.nom_personne_update_wtf.data

            valeur_update_dictionnaire = {"value_id_personne": id_personne_update,
                                          "value_Nom_personne": nom_personne_update,
                                          "value_Prenom_personne_essai": prenom_personne_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_id_personne = """UPDATE t_personnes SET Nom_personne = %(value_Nom_personne)s 
                      WHERE id_personne = %(value_id_personne)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_id_personne, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_personne_update"
            return redirect(url_for('personne_afficher', order_by="ASC", id_personne_sel=id_personne_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_personne" et "intitule_personne" de la "t_personnes"
            str_sql_id_personne = "SELECT id_personne, nom_personne, prenom_personne FROM t_personnes " \
                               "WHERE id_personne = %(value_id_personne)s"
            valeur_select_dictionnaire = {"value_id_personne": id_personne_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "name personne" pour l'UPDATE
            data_name_personne = mybd_conn.fetchone()
            print("data_name_personne ", data_name_personne, " type ", type(data_name_personne), " personne ",
                  data_name_personne["nom_personne"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "personne_update_wtf.html"
            form_update.nom_personne_update_wtf.data = data_name_personne["nom_personne"]
            form_update.prenom_personne_wtf_essai.data = data_name_personne["prenom_personne"]


    except Exception as Exception_personne_update_wtf:
        raise ExceptionpersonneUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personne_update_wtf.__name__} ; "
                                      f"{Exception_personne_update_wtf}")

    return render_template("personne/personne_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /personne_delete
    
    Test : ex. cliquer sur le menu "personne" puis cliquer sur le bouton "DELETE" d'un "personne"
    
    Paramètres : sans
    
    But : Effacer(delete) un personne qui a été sélectionné dans le formulaire "personne_afficher.html"
    
    Remarque :  Dans le champ "name_personne_delete_wtf" du formulaire "personne/personne_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/personne_delete", methods=['GET', 'POST'])
def personne_delete_wtf():
    data_films_attribue_personne_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_personne"
    id_personne_delete = request.values['id_personne_btn_delete_html']

    # Objet formulaire pour effacer le personne sélectionné.
    form_delete = FormWTFDeletePersonne()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("personne_afficher", order_by="ASC", id_personne_sel=0))

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
                valeur_delete_dictionnaire = {"value_id_personne": id_personne_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)


                str_sql_delete_idpersonne = """DELETE FROM t_personnes WHERE id_personne = %(value_id_personne)s"""


                # Manière brutale d'effacer d'abord la "fk_personne", même si elle n'existe pas dans la "t_personnes_film"
                # Ensuite on peut effacer le personne vu qu'il n'est plus "lié" (INNODB) dans la "t_personnes_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_idpersonne, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idpersonne, valeur_delete_dictionnaire)

                flash(f"personne définitivement effacé !!", "success")
                print(f"personne définitivement effacé !!")

                # afficher les données
                return redirect(url_for('personne_afficher', order_by="ASC", id_personne_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_personne": id_personne_delete}
            print(id_personne_delete, type(id_personne_delete))

            # Requête qui affiche tous les films_personne qui ont le personne que l'utilisateur veut effacer
            str_sql_personne_films_delete = """SELECT *FROM t_personnes
                                                        Where id_personne = %(value_id_personne)s"""


            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_personne_films_delete, valeur_select_dictionnaire)
                data_films_attribue_personne_delete = mydb_conn.fetchall()
                print("data_films_Nom_personne_delete...", data_films_attribue_personne_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personne/personne_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_personne_delete'] = data_films_attribue_personne_delete

                # Opération sur la BD pour récupérer "id_personne" et "intitule_personne" de la "t_personnes"
                str_sql_id_personne = "SELECT id_personne, Nom_personne, Prenom_personne FROM t_personnes WHERE id_personne = %(value_id_personne)s"

                mydb_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
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
                                      f"{personne_delete_wtf.__name__} ; "
                                      f"{Exception_personne_delete_wtf}")

    return render_template("personne/personne_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_personne_delete)
