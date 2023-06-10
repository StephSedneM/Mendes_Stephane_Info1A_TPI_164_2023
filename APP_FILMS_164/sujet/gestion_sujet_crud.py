"""Gestion des "routes" FLASK et des données pour les sujet.
Fichier : gestion_sujet_crud.py
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
from APP_FILMS_164.sujet.gestion_sujet_wtf_forms import FormWTFAjoutersujet
from APP_FILMS_164.sujet.gestion_sujet_wtf_forms import FormWTFDeletesujet
from APP_FILMS_164.sujet.gestion_sujet_wtf_forms import FormWTFUpdatesujet

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /sujet_afficher
    
    Test : ex : http://127.0.0.1:5575/sujet_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_sujet_sel = 0 >> tous les sujet.
                id_sujet_sel = "n" affiche la sujet dont l'id est "n"
"""


@app.route("/sujet_afficher/<string:order_by>/<int:id_sujet_sel>", methods=['GET', 'POST'])
def sujet_afficher(order_by, id_sujet_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_sujet_sel == 0:
                    strsql_sujet_afficher = """SELECT * FROM t_sujet ORDER BY id_sujet ASC"""
                    mc_afficher.execute(strsql_sujet_afficher)

                elif order_by == "ASC":

                    valeur_id_sujet_selected_dictionnaire = {"value_id_sujet_selected": id_sujet_sel}
                    strsql_sujet_afficher = """Select * From t_sujet WHERE id_sujet = %(value_id_sujet_selected)s"""

                    mc_afficher.execute(strsql_sujet_afficher, valeur_id_sujet_selected_dictionnaire)
                else:
                    strsql_sujet_afficher = """SELECT * FROM t_sujet ORDER BY id_sujet DESC"""

                    mc_afficher.execute(strsql_sujet_afficher)

                data_sujet = mc_afficher.fetchall()

                print("data_sujet ", data_sujet, " Type : ", type(data_sujet))

                # Différencier les messages si la table est vide.
                if not data_sujet and id_sujet_sel == 0:
                    flash("""La table "t_sujet" est vide. !!""", "warning")
                elif not data_sujet and id_sujet_sel > 0:
                    # Si l'utilisateur change l'id_sujet dans l'URL et que le sujet n'existe pas,
                    flash(f"La sujet demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_sujet" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Voici les sujet!!", "success")

        except Exception as Exception_sujet_afficher:
            raise ExceptionsujetAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{sujet_afficher.__name__} ; "
                                          f"{Exception_sujet_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("sujet/sujet_afficher.html", data=data_sujet)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /sujet_ajouter
    
    Test : ex : http://127.0.0.1:5575/sujet_ajouter
    
    Paramètres : sans
    
    But : Ajouter un sujet pour un film
    
    Remarque :  Dans le champ "name_sujet_html" du formulaire "sujet/sujet_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/sujet_ajouter", methods=['GET', 'POST'])
def sujet_ajouter_wtf():
    form = FormWTFAjoutersujet()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                Nom_sujet_wtf = form.nom_sujet_wtf.data
                Nom_sujet = Nom_sujet_wtf.lower()





                valeurs_insertion_dictionnaire = {"value_Nom_sujet": Nom_sujet_wtf}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_sujet = """INSERT INTO t_sujet (id_sujet,Nom_sujet) VALUES (NULL, %(value_Nom_sujet)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_sujet, valeurs_insertion_dictionnaire)


                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('sujet_afficher', order_by='DESC', id_sujet_sel=0))



        except Exception as Exception_sujet_ajouter_wtf:
            raise ExceptionsujetAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{sujet_ajouter_wtf.__name__} ; "
                                            f"{Exception_sujet_ajouter_wtf}")

    return render_template("sujet/sujet_ajouter_wtf.html", form=form)




"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /sujet_update
    
    Test : ex cliquer sur le menu "sujet" puis cliquer sur le bouton "EDIT" d'un "sujet"
    
    Paramètres : sans
    
    But : Editer(update) un sujet qui a été sélectionné dans le formulaire "sujet_afficher.html"
    
    Remarque :  Dans le champ "name_sujet_update_wtf" du formulaire "sujet/sujet_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/sujet_update", methods=['GET', 'POST'])
def sujet_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_sujet"
    id_sujet_update = request.values['id_sujet_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatesujet()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "sujet_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.

            nom_sujet_update = form_update.nom_sujet_update_wtf.data


            valeur_update_dictionnaire = {"value_id_sujet": id_sujet_update,
                                          "value_Nom_sujet": nom_sujet_update,

                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_id_sujet = """UPDATE t_sujet SET Nom_sujet = %(value_Nom_sujet)s 
                      WHERE id_sujet = %(value_id_sujet)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_id_sujet, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_sujet_update"
            return redirect(url_for('sujet_afficher', order_by="ASC", id_sujet_sel=id_sujet_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_sujet" et "intitule_sujet" de la "t_sujet"
            str_sql_id_sujet = "SELECT id_sujet, nom_sujet FROM t_sujet " \
                               "WHERE id_sujet = %(value_id_sujet)s"
            valeur_select_dictionnaire = {"value_id_sujet": id_sujet_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_sujet, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "name sujet" pour l'UPDATE
            data_name_sujet = mybd_conn.fetchone()
            print("data_name_sujet ", data_name_sujet, " type ", type(data_name_sujet), " sujet ",
                  data_name_sujet["nom_sujet"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "sujet_update_wtf.html"
            form_update.nom_sujet_update_wtf.data = data_name_sujet["nom_sujet"]



    except Exception as Exception_sujet_update_wtf:
        raise ExceptionsujetUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{sujet_update_wtf.__name__} ; "
                                      f"{Exception_sujet_update_wtf}")

    return render_template("sujet/sujet_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /sujet_delete
    
    Test : ex. cliquer sur le menu "sujet" puis cliquer sur le bouton "DELETE" d'un "sujet"
    
    Paramètres : sans
    
    But : Effacer(delete) un sujet qui a été sélectionné dans le formulaire "sujet_afficher.html"
    
    Remarque :  Dans le champ "name_sujet_delete_wtf" du formulaire "sujet/sujet_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/sujet_delete", methods=['GET', 'POST'])
def sujet_delete_wtf():
    data_films_attribue_sujet_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_sujet"
    id_sujet_delete = request.values['id_sujet_btn_delete_html']

    # Objet formulaire pour effacer le sujet sélectionné.
    form_delete = FormWTFDeletesujet()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("sujet_afficher", order_by="ASC", id_sujet_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "sujet/sujet_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_sujet_delete = session['data_films_attribue_sujet_delete']
                print("data_films_attribue_sujet_delete ", data_films_attribue_sujet_delete)

                flash(f"Effacer le sujet de façon définitive de la BD !!!", "On s'en fou non?")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer sujet" qui va irrémédiablement EFFACER le sujet
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_sujet": id_sujet_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)


                str_sql_delete_idsujet = """DELETE FROM t_sujet WHERE id_sujet = %(value_id_sujet)s"""


                # Manière brutale d'effacer d'abord la "fk_sujet", même si elle n'existe pas dans la "t_sujet_film"
                # Ensuite on peut effacer le sujet vu qu'il n'est plus "lié" (INNODB) dans la "t_sujet_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_idsujet, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idsujet, valeur_delete_dictionnaire)

                flash(f"sujet définitivement effacé !!", "success")
                print(f"sujet définitivement effacé !!")

                # afficher les données
                return redirect(url_for('sujet_afficher', order_by="ASC", id_sujet_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_sujet": id_sujet_delete}
            print(id_sujet_delete, type(id_sujet_delete))

            # Requête qui affiche tous les films_sujet qui ont le sujet que l'utilisateur veut effacer
            str_sql_sujet_films_delete = """SELECT *FROM t_sujet
                                                        Where id_sujet = %(value_id_sujet)s"""


            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_sujet_films_delete, valeur_select_dictionnaire)
                data_films_attribue_sujet_delete = mydb_conn.fetchall()
                print("data_films_Nom_sujet_delete...", data_films_attribue_sujet_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "sujet/sujet_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_sujet_delete'] = data_films_attribue_sujet_delete

                # Opération sur la BD pour récupérer "id_sujet" et "intitule_sujet" de la "t_sujet"
                str_sql_id_sujet = "SELECT id_sujet, Nom_sujet FROM t_sujet WHERE id_sujet = %(value_id_sujet)s"

                mydb_conn.execute(str_sql_id_sujet, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "name sujet" pour l'action DELETE
                data_Nom_sujet = mydb_conn.fetchone()
                print("data_Nom_sujet ", data_Nom_sujet, " type ", type(data_Nom_sujet), " sujet ",
                      data_Nom_sujet["Nom_sujet"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "sujet_delete_wtf.html"
            form_delete.nom_sujet_delete_wtf.data = data_Nom_sujet["Nom_sujet"]

            # Le bouton pour l'action "DELETE" dans le form. "sujet_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_sujet_delete_wtf:
        raise ExceptionsujetDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{sujet_delete_wtf.__name__} ; "
                                      f"{Exception_sujet_delete_wtf}")

    return render_template("sujet/sujet_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_sujet_delete)
