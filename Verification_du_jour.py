#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                       NOYADE SECHE - Premier pas dans l'eau
#   Djadid OUSSENI RIZIKI
#       Formation Manager en Ingénierie Informatique L3
#           2018-2021

#               Exercice pour la vérification du jour d'une date grégorienne

# --> Consignes <--

# ---------->  Date minimale = 01/11/1582  <-------------  #

        # En fonction du calcul du jour qui sera fait, les mois seront associés à des chiffres
                # 0 pour Janvier;
                # 3 pour Février, Mars et Novembre;
                # 6 pour Avril et Juillet;
                # 1 pour Mai; 4 pour Juin;
                # 2 pour Août;
                # 5 pour Septembre et Décembre

        # En fonction du calcul du jour qui sera fait, les siècles seront associés à un chiffre
                # 6 pour le 16ième siècle et 20ième siècle;
                # 4 pour le 17ième et 21ième siècle;
                # 2 pour le 18ième siècle;<
                # 0 pour le 19ième siècle;

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#NOUS UTILISERONS PRINCIPALEMENT DES FONCTIONS POUR CHAQUE PARAMETRE QUI SERVIRA DANS LE CALCUL FINAL DE DERTMINATION DU JOUR DE LA SEMAINE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Importation de la  bibliotheque pour les expressions régulieres qui seront primordiales pour le programme

import re

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           DEBUT DU PROGRAMME SECONDAIRE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Utilisation d'une fonction de vérification pour savoir si la date est bissextile après saisie
    # Les valeurs renvoyés sont : return True si c'est bisextile, et return = False si ce n'est pas bissextile

        # Cette fonction est utilisée pour verifier la date si c'est bien bissextile dans le cas d'une date valide(bonne saisie)

def Bissextile_vrai(annee):

    annee = int(annee)

    if(annee % 400 == 0):
        return True

    elif(annee % 100 == 0):
        return False

    elif(annee % 4 == 0):
        return True

    return False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Utilisation d'une fonction de vérification pour associer les mois aux données de la consigne

    # Les valeurs renvoyés sont :
        # 0 pour Janvier;
        # 3 pour Février, Mars et Novembre;
        # 6 pour Avril et Juillet;
        # 1 pour Mai; 4 pour Juin;
        # 2 pour Août;
        # 5 pour Septembre et Décembre

            # Cette fonction sera utilisée pour le calcul qui nous permettra d'obtenir le jour d'une date donnée

def Consigne_mois(mois):

    mois = int(mois)  # Enleve les zeros inutiles des associations des mois avec leurs valeurs en fonction de la consigne

    if (mois == 1 or mois == 10): #   Pour Janvier et Octobre
        return 0

    elif (mois == 2 or mois == 3 or mois == 11): #   Pour Février, Mars et Novembre
        return 3

    elif (mois == 4 or mois == 7):    #   Pour Avril et Juillet
        return 6

    elif (mois == 5):  # Pour Mai
        return 1

    elif (mois == 6):  # Pour Juin
        return 4

    elif (mois == 8):  # Pour Aout
        return 2

    elif (mois == 9 or mois == 12):   # Pour Septembre et Decembre
        return 5

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Utilisation d'une fonction de vérification pour associer les siècles aux données de la consigne

# Pour nôtre cas le 16ième siècle est le minimum

    # Les valeurs renvoyés sont :
        # 6 pour le 16ième siècle et 20ième siècle;
        # 4 pour le 17ième et 21ième siècle;
        # 2 pour le 18ième siècle;
        # 0 pour le 19ième siècle;

            # Cette fonction sera utilisée pour le calcul qui nous permettra d'obtenir le jour d'une date donnée

def Consigne_Siecle(century):

    c = int(century) - 1500

    if(c % 400 == 0):
        return 0

    elif(c % 300 == 0):
        return 2

    elif(c % 200 == 0):
        return 4

    return 6

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Vérification de la date si elle est bien valable mais aussi si elle est dans la période grégorienne

# Le type de variable qui sera utilisée sera le string

# Nous avons trois potentiels scénarios : --> return 0 = pas une date;
                                            # return 1 = date gregorinne. Donc -> OK.
                                            # return 2 = date non gregorienne. Donc -> Non OK avec notre exercice

def Verif_Gregorien(str):
    if(re.sub('^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/][0-9]{4}$', "", str)): # Cette ligne nous permets de garder une date valable en ne depassant jamais 31 pour le jour, 12 pour le mois et permet de rester dans la plage grégorienne en passant par un regex
        return 0

    substr = str.split('/')
    if (int(substr[2]) > 1582 or (int(substr[2]) == 1582 and int(substr[1]) >= 11)):
        return 1

    return 2

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Utilisation d'une fonction de pour la détermination du jour avec les différents éléments pour associés précédemment

    # Renvoie le résulat du calcul entre 0 et 6 pour l'associer à la valeur du jour.
        # On suppose que la date est  valide et au format dd/mm/aaaa.

def Verification_Jour_Semaine(date):

    Separation_date = date.split('/')  # Séparateur des éléments de la date
    Decenie = int(Separation_date[2][2] + Separation_date[2][3])  # Ce qui nous intéresse pour le programme est seulement la décénie

    Quart_de_la_Decenie = Decenie // 4

    jour = int(Separation_date[0])  # Utilisation de l'élement séparateur pour notre date afin de selection la première partie de la date
    mois = int(Separation_date[1]) # Utilisation de l'élement séparateur pour notre date afin de selection la seconde partie de la date

    valMois = int(Consigne_mois(mois))  # Utilisation de la valeur liée à ce qu'on a fixé grâce à la consigne

    anneeAjustee = int(Separation_date[2][0] + Separation_date[2][1] + '0' + '0')  # Ajustement de l'année au millier

    valSiecle = int(Consigne_Siecle(anneeAjustee))  # Valeur associee a l'annee arrondie

    bissextile =  1 \
        if (Bissextile_vrai(anneeAjustee) and (int(Separation_date[1]) == 1 or int(Separation_date[1]) == 2)) else 0
    # Vérification de la consigne avec l'année bissextile avec le mois de Janvier ou Février par rapport à la consigne

    return int(Decenie+Quart_de_la_Decenie+jour+valMois-bissextile+valSiecle)%7


#                                         DEBUT DU PROGRAMME PRINCIPAL
def Fonction_Principale():

    val_saisie = "Saisir une date GREGORIENNE en respectant le format suivant : (dd/mm/aaaa). Donc >= 01/11/1582 :\n"

# L'utilisateur saisie la date donnée

    date = input(val_saisie)

# Lancement de la boucle en cas de mauvaise saisie ou mauvaise date

    while(Verif_Gregorien(date)!=1):

        if(Verif_Gregorien(date)==2):
            print('\nLa date saisie n\'est pas une date GREGORIENNE !\n')

        else:
            print('\nLa saisie est incorrecte !\n')

        date = input(val_saisie)

# Les retours possible du programme

    Jour_probable = [
            'Dimanche',
            'Lundi',
            'Mardi',
            'Mercredi',
            'Jeudi',
            'Vendredi',
            'Samedi'
            ]

    # Affichage du jour de la semaine

    print("Le ", date, " est un ",Jour_probable[Verification_Jour_Semaine(date)])

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           LANCEMENT DU PROGRAMME
Fonction_Principale()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           FIN DU PROGRAMME