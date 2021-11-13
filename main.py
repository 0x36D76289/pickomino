def lance_des(nombre_des:int) -> list:
    """
    Fonction qui lance des dés "nombre_des" fois et retourne le résultat
    :param des: nombre de dés à lancer
    :return: liste des valeurs obtenues
    """
    from random import randint
    valeurs = []
    for i in range(nombre_des):
        valeurs.append(randint(1, 6))
    return valeurs

def n_j() -> int:
    """
    Fonction qui demande le nombre de joueurs si le nombre est <= 2 et => 7
    :return: nombre de joueurs
    """
    nombre_joueurs = int(input("Combien de joueurs ? "))
    if 7 <= nombre_joueurs <= 2:
        print("Il faut un chiffre <= 2 et => 7")
        return n_j()
    return nombre_joueurs

def autre_joueur(pikominos_joueur:list, pikominos_autre_joueurs:list, need_pikominos:int):
    pikominos_joueur.append(need_pikominos)
    pikominos_autre_joueurs.remove(need_pikominos)
    return pikominos_joueur, pikominos_autre_joueurs

from bisect import bisect_left

def takeClosest(myList:list, myNumber:int) -> int:
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

def sur_plateau(pikominos:list, pikominos_joueur:list, need_pikominos:int, somme_des:int):
    if somme_des in pikominos: # si le joueur a le pikominos sur le plateau
        pikominos_joueur.append(somme_des) # on l'ajoute au joueur
        pikominos.remove(somme_des) # on le supprime du plateau
        return pikominos_joueur, pikominos # on retourne les listes

    pikominos_a_prendre = takeClosest(pikominos, somme_des) # on prend le plus proche

    need_pikominos = int(input("Quel pikominos veut tu prendre {}: ".format(pikominos_a_prendre))) # on demande le pikominos
    if need_pikominos not in pikominos_a_prendre: # si le joueur ne veut pas prendre le pikominos
        return sur_plateau(pikominos, need_pikominos, somme_des) # on recommence
    pikominos_joueur.append(need_pikominos) # on ajoute le pikominos au joueur
    return pikominos_joueur, pikominos # on retourne les listes

def prendre_pikominos(pikominos:list, pikominos_joueur:list, pikominos_autre_joueurs:list, somme_des:int):
    print("Le joueurs a {} pikominos,\nLes joueurs en face ont {} pikominos prenable,\nEt il y a {} Pikominos sur disponible".format(pikominos_joueur, pikominos_autre_joueurs, pikominos)) # on affiche les informations
    need_pikominos = int(input("Quel pikominos veut tu prendre (tu as un score de {} avec tes lancés de des) (entrez un entier): ".format(somme_des))) # on demande le pikominos
    if need_pikominos == somme_des or need_pikominos in takeClosest(pikominos, somme_des): # si le joueur a le pikominos sur le plateau
        if need_pikominos > 36 or need_pikominos < 21: # si le joueur veut prendre un pikominos qui n'est pas sur le plateau
            return prendre_pikominos(pikominos, pikominos_joueur, pikominos_autre_joueurs, somme_des) # on recommence
        if need_pikominos == takeClosest(pikominos, somme_des): # si le joueur a le pikominos sur le plateau
            pikominos_joueur, pikominos = sur_plateau(pikominos, pikominos_joueur, need_pikominos, somme_des) # on ajoute le pikominos au joueur
        elif need_pikominos == somme_des: # si le joueur a le pikominos sur le plateau
            pikominos_joueur, pikominos_autre_joueurs = autre_joueur(pikominos_joueur, pikominos_autre_joueurs, need_pikominos) # on ajoute le pikominos au joueur
        return pikominos_joueur, pikominos, pikominos_autre_joueurs # on retourne les listes
    return prendre_pikominos(pikominos, pikominos_joueur, pikominos_autre_joueurs, somme_des) # on recommence

def pass_ton_tour(pikominos:list, pikominos_joueur:list):
    """
    Rend le dernier pikominos du joueur et le met dans la list pikominos, si il est le plus pikominos le plus élever apres sont ajout on le supprime
    """
    if max(pikominos) > pikominos_joueur[-1]:
        pikominos.append(pikominos_joueur[-1])
        pikominos_joueur.pop()
    else: 
        pikominos_joueur.pop()
    return pikominos, pikominos_joueur

def condition2(temp_des_lancer:list, temp_des_poche:list, need_dominos:str, nombre_des:int) -> list:
    """
    Fonction qui vérifie si la condition 2 est respectée
    :param temp_des_lancer: liste des dés lancés
    :param temp_des_poche: liste des dés de la poche
    :param need_dominos: nécessité de dominos
    :param nombre_des: nombre de dés à lancer
    :return: liste des dés à lancer
    """
    for i in range(len(temp_des_lancer)): # on parcours la liste des dés lancés
        if temp_des_lancer[i] == int(need_dominos): # si le joueur a le dominos
            temp_des_poche.append(temp_des_lancer[i]) # on ajoute le dominos à la poche
            nombre_des = nombre_des - 1
    return temp_des_poche, nombre_des

def condition(pikominos:list, pikominos_joueur:list, temp_des_poche:list, temp_des_lancer:list, nombre_des:int):
    """
    Check if the player wants to roll again and what pair of dice they want to take
    :param pikominos: list of the pikominos
    :param temp_des_poche: list of the pikominos in the poche
    :param temp_des_lancer: list of the dice values
    :param nombre_des: number of dice values
    :return: temp_des_poche, nombre_des
    """
    need_dominos = input("Quel dominos veut tu prendre ? {}".format(temp_des_lancer))
    if need_dominos == "n":
        if 6 in temp_des_poche:
            return temp_des_poche, 0
        print("Tu passe ton tour")
        return [0], nombre_des
    elif need_dominos in temp_des_poche:
        print("Tu ne peux pas prendre un dominos qui tu possede deja")
        return condition(pikominos, temp_des_poche, temp_des_lancer, nombre_des)
    temp_des_poche, nombre_des = condition2(temp_des_lancer, temp_des_poche, need_dominos, nombre_des)
    return temp_des_poche, nombre_des

def tour(joueur, pikominos, pikominos_joueur):
    pikominos.sort()
    temp_des_poche = []
    nombre_des = 8
    while nombre_des != 0:
        temp_des_lancer = lance_des(nombre_des)
        print("{} a lancé les dés : {}".format(joueur, temp_des_lancer))
        temp_des_poche, nombre_des = condition(pikominos, pikominos_joueur, temp_des_poche, temp_des_lancer, nombre_des)
        print("{} a prit les dominos {}".format(joueur, temp_des_poche))
    print("Vous ne pouvez plus lancer de des")
    return sum(temp_des_poche)

if __name__ == "__main__":
    vers = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] # Liste des pikominos
    print(vers)

    # On demande le nombre de joueurs et on crée la liste des joueurs avec leurs pikominos
    nombre_joueurs = n_j()
    liste_joueur = []
    pikominos_joueur = []

    # Création de la liste des joueurs
    for x in range(nombre_joueurs):
        nom_joueur = input("Nom du joueur " + str(x+1) + ": ")
        liste_joueur.append(nom_joueur)

    # Création de la liste des pikominos
    for i in range(nombre_joueurs):
        pikominos_joueur.append([])

    print("Joueurs :\n{}\nPikominos des joueurs\n{}\nC'est au joueurs 1 de commencer".format(liste_joueur, pikominos_joueur))

    #le jeux commence
    while vers != 0:
        nombre_des = 8 # nombre de dés à lancer
        for joueur in range(nombre_joueurs):
            vers_autre_joueurs = []
            if len(pikominos_joueur[joueur]) != 0:
                for i in range(nombre_joueurs):
                    vers_autre_joueurs.append(pikominos_joueur[i-1][-1])
                vers_joueurs = []
                for i in range(len(nombre_joueurs[joueur-1])):
                    vers_joueurs.append(pikominos_joueur[joueur-1][-1])
            else:
                vers_autre_joueurs = []
                vers_joueurs = []
            somme_des = tour(liste_joueur[joueur-1], vers, vers_joueurs)
            print("{} a obtenu un score de {} avec les des".format(liste_joueur[joueur-1], somme_des))
            vers_joueurs, vers, vers_autre_joueurs = prendre_pikominos(vers, vers_joueurs, vers_autre_joueurs, somme_des)
            print("{} a pris les pikominos {}".format(liste_joueur[joueur-1], vers_joueurs))

    max_score = 0
    gagnant = 0
    for i in range(nombre_joueurs):
        for x in range(len(pikominos_joueur[i])):
            if max_score < sum(pikominos_joueur[i][x]):
                max_score = sum(pikominos_joueur[i][x])
                gagnant = i

    print("Le gangnant est {} avec {} points".format(liste_joueur[gagnant-1], max_score))
    print("Fin du jeux")

