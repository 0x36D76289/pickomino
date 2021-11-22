def take_dominoes(number_players, player, main_dominoes, temp_dominoes, last_other_dominoes, sum_dice):
    """ temp_dice, names, main_dominoes, temp_dominoes crée une liste takeable qui correspond aux dominos qui peuvent
    etre pris si 21 <= sum_dice <= 36 - Si sum_dice strictement égale à un entier dans last_other_dominoes - Si
    sum_dice strictement égale à un entier dans main_dominoes - Si sum_dice n'est pas strictement égale à un entier
    dans main_dominoes on ajoute l'entier le plus proche de sum_dice à takeable
    """
    close_value = [i for i in main_dominoes if abs(sum_dice - i) == min(abs(sum_dice - i) for i in main_dominoes)] # liste des dominos proches de sum_dice
    takeable = [] # liste des dominos que le joueur peut prendre

    if sum_dice in last_other_dominoes: # si sum_dice est dans last_other_dominoes
        temp_list = [i for i in last_other_dominoes if i == sum_dice] # on ajoute les dominos de la liste last_other_dominoes
        takeable += temp_list # on ajoute les dominos qui ont la meme valeur que sum_dice
    if sum_dice in main_dominoes: # si sum_dice est strictement dans main_dominoes
        temp_list = [i for i in main_dominoes if i == sum_dice] # on ajoute les dominos de main_dominoes
        takeable += temp_list # on ajoute les dominos de main_dominoes qui sont égaux à sum_dice
    if sum_dice != close_value: # si sum_dice n'est pas strictement égale à un entier dans main_dominoes
        takeable.append(close_value) # on ajoute le plus proche de sum_dice à takeable
    # trie la liste takeable dans l'ordre croissant
    if len(takeable[1:]) == 0: # si la liste takeable est vide
        return # on ne fait rien

    print(f"{number_players[player]} a comme dominos prennable : {takeable[1]}") # on affiche les dominos prennable
    choice = int(input("Quel dominos veut tu prendre : ")) # on demande à l'utilisateur de choisir un dominos

    while choice not in takeable: # tant que l'utilisateur n'a pas choisi un dominos prennable
        choice = int(input("Quel dominos veut tu prendre : ")) # on demande à l'utilisateur de choisir un dominos
    choice = int(choice) # on convertit la valeur de choice en entier
    if choice in main_dominoes: # si choice est dans main_dominoes
        temp_dominoes.append(choice) # on ajoute choice à temp_dominoes
        main_dominoes.remove(choice) # on supprime choice de main_dominoes
    if choice in last_other_dominoes: # si choice est dans last_other_dominoes
        temp_dominoes.append(choice) # on ajoute choice à temp_dominoes
        last_other_dominoes.remove(choice) # on supprime choice de last_other_dominoes
    if choice == close_value: # si choice est égale à un entier dans main_dominoes
        temp_dominoes.append(choice) # on ajoute choice à temp_dominoes
        main_dominoes.remove(choice) # on supprime choice de main_dominoes
    print(f"Vous avez pris {choice} à vos dominos") # on affiche le message de prise de dominos
    return # on retourne


def skip_your_turn(main_dominoes: list[int], temp_dominoes: list[int]):
    """
    Si le dernier entier de temp_dominos est plus petit que le plus grand de la liste main_dominos,
     on l'ajoute à main_dominos et on le supprime de temp_dominos.
     si non on le supprime de temp_dominos.
    """
    if temp_dominoes[-1] < max(main_dominoes): # si le dernier entier de temp_dominoes est plus petit que le plus grand de la liste main_dominoes
        main_dominoes.append(temp_dominoes[-1]) # on ajoute le dernier entier de temp_dominoes à main_dominoes
    temp_dominoes.pop() # on supprime le dernier entier de temp_dominoes


def rolling_dice(number_dice):
    """
    On lance dice fois un des allant de 1 à 6
    """
    import random # on importe la bibliothèque random
    return [random.randint(1, 6) for _ in range(number_dice)] # on lance dice fois un des allant de 1 à 6


def pass_your_turn(main_dominoes: list[int], temp_dominoes: list[int]):
    """
    Rend le dernier entier de temp_dominoes à main_dominoes
     Si cette entier est plus petit que le plus grand de la liste main_dominoes,
     on l'ajoute à main_dominoes et on le supprime de temp_dominoes.
    """
    print(f"Vous avez passé votre tour et rendu {temp_dominoes[-1]}") # on affiche le message de rendu de dominos
    if temp_dominoes[-1] < max(main_dominoes): # si le dernier entier de temp_dominoes est plus petit que le plus grand de la liste main_dominoes
        main_dominoes.append(temp_dominoes[-1]) # on ajoute le dernier entier de temp_dominoes à main_dominoes
    temp_dominoes.pop() # on supprime le dernier entier de temp_dominoes
    print(f"Les dominos sur le plateau : {main_dominoes}\n"
          f"Vous avez maintenant       : {temp_dominoes}") # on affiche les dominos dans main_dominoes et temp_dominoes


def choice_dice(number_players, player, temp_dice_roll, temps_dice):
    """
    Demande au joueur de choisir le nombre de dés qu'il veut lancer
    """
    if len(temps_dice) != 0: # si temps_dice n'est pas vide
        if all(i in temps_dice for i in temp_dice_roll): # si tous les éléments de temp_dice_roll sont dans temps_dice
            print(f"Tu as jeté que des dés {temp_dice_roll} que tu possèdes deja {temps_dice}, pas de chance") # on affiche le message de jet de dés
            return -2 # on retourne -2
    choice = input(f"{number_players[player]}, Quel dominos veut tu prendre {temp_dice_roll} (N, pour arreter 1): ") # on demande à l'utilisateur de choisir un dominos

    if choice in ['n', 'N']: # si l'utilisateur a choisi de ne pas prendre de dominos
        if 6 in temps_dice: # si 6 est dans temps_dice
            return int(sum(temps_dice)) # on retourne la somme de temps_dice
        return -1 # on retourne -1
    choice = int(choice) # on convertit la valeur de choice en entier
    if choice not in temp_dice_roll: # si choice n'est pas dans temp_dice_roll
        print("Tu ne peux pas prendre un des que tu n'a pas lancer") # on affiche le message de jet de dés
        return choice_dice(number_players, player, temp_dice_roll, temps_dice) # on retourne choice_dice
    if choice in temps_dice: # si choice est dans temps_dice
        print("Tu ne peux pas prendre un des que tu possede deja") # on affiche le message de jet de dés
        return choice_dice(number_players, player, temp_dice_roll, temps_dice) # on retourne choice_dice
    return choice # on retourne choice


def player_turn(player, number_players):
    """
    Tant que le nombre de dés != 0 , on lance le dés tant que :
    - dice != 0
    - tout les chiffres de 1 à 6 ne sont pas dans temp_dice
    - l'utilisateur ne veut pas prendre de des avec "n" ou "N"
    """
    number_dice = 8 # on initialise number_dice à 8
    temps_dice = [] # on initialise temps_dice à []
    throw_of_dice = 0 # on initialise throw_of_dice à 0
    while number_dice > 0: #tant que number_dice est supérieur à 0
        throw_of_dice += 1 # on incrémente throw_of_dice
        temp_dice_roll = rolling_dice(number_dice) # on lance dice fois un des allant de 1 à 6
        choice = choice_dice(number_players, player, temp_dice_roll, temps_dice) # on demande au joueur de choisir un dominos
        if choice == sum(temps_dice): # si la somme de temps_dice est égale à choice
            return sum(temps_dice) # on retourne la somme de temps_dice
        if choice == -1: # si choice est égal à -1
            return -1 # on retourne -1
        if choice == -2: # si choice est égal à -2
            return -2 # on retourne -2
        for number in temp_dice_roll: # pour chaque chiffre temp_dice_roll
            if number == choice: # si le chiffre est égal à choice
                temps_dice.append(number) # on ajoute le chiffre à temps_dice
                number_dice -= 1 # on décrémente number_dice
        print(f"Vous avez pris les dés {choice} : {temps_dice} = {sum(temps_dice)}") # on affiche le message de prise de dominos
    if 6 not in temps_dice: # si 6 n'est pas dans temps_dice
        print("Vous n'avez pas de 6") # on affiche le message de jet de dés
        return -1 # on retourne -1
    print() # on affiche un retour à la ligne
    return int(sum(temps_dice)) # on retourne la somme de temps_dice


if __name__ == "__main__": # si le fichier est lancé en tant que programme principal
    print("Pikomino") # on affiche le message de bienvenue
    main_dominoes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] # on initialise main_dominoes à [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    print(main_dominoes) # on affiche main_dominoes

    nb_players = int(input("Combien de joueurs ? ")) # on demande à l'utilisateur de choisir le nombre de joueurs
    while nb_players < 2 or nb_players > 7: # tant que nb_players est inférieur à 2 ou supérieur à 7
        nb_players = int(input("Combien de joueurs ? ")) # on demande à l'utilisateur de choisir le nombre de joueurs

    players_dominoes = [] # on initialise players_dominoes à []
    for i in range(nb_players): # pour chaque i allant de 0 à nb_players
        players_dominoes.append([]) # on ajoute [] à players_dominoes

    names = [] # on initialise names à []
    for i in range(nb_players): # pour chaque i allant de 0 à nb_players
        names.append(input(f"Quel est le nom du joueur {i+1} ? ")) # on demande à l'utilisateur de choisir le nom de joueur
    print(players_dominoes, names) # on affiche players_dominoes et names

    turn = 1 # on initialise turn à 1
    while len(main_dominoes) > 0: # tant que main_dominoes n'est pas vide
        for play in range(nb_players): # pour chaque play allant de 0 à nb_players
            print(f"\n\n\tTour {turn}\n\n") # on affiche le message de tour
            dice = 8 # on initialise dice à 8
            main_dominoes.sort()  # tri la liste main_dominos par ordre croissant
            sum_dice = 0  # somme des dés du joueur
            temp_dominoes = players_dominoes[play]  # dominos du joueur temporaire
            last_other_dominoes = []  # dernier dominos des autres joueurs que player
            for i in range(nb_players): # pour chaque i allant de 0 à nb_players
                if i != play: # si i est différent de play
                    if len(players_dominoes[i]) != 0: # si la taille de players_dominoes[i] est différente de 0
                        last_other_dominoes.append(players_dominoes[i][-1]) # on ajoute le dernier dominos de players_dominoes[i] à last_other_dominoes

            temp_dice = player_turn(play, names)  # Fait passer le premier tour au joueur play
            if temp_dice in [-1, -2]: # si temp_dice est égal à -1 ou -2
                if temp_dice == -1: # si temp_dice est égal à -1
                    print(f"Vous n'avez pas de 6 dans vos dés") # on affiche le message de jet de dés
                if len(temp_dominoes) != 0: # si la taille de temp_dominoes est différente de 0
                    print("Vous passer votre tour") # on affiche le message de passer son tour
                    pass_your_turn(main_dominoes, temp_dominoes) # on passe le tour du joueur
                else: # sinon
                    print("Vous n'avez pas assez de dominos pour passer votre tour") # on affiche le message de pas assez de dominos
                continue # on continue la boucle

            else: # sinon
                print(f"Vous avez obtenu un score de {temp_dice} avec les dés") # on affiche le message de score du joueur
                if not 21 > temp_dice or temp_dice > 36: # si temp_dice n'est pas compris entre 21 et 36
                    print(f"Dominos sur le plateau : {main_dominoes}\n"
                          f"Dominos visibles des autres joueurs : {last_other_dominoes}") # on affiche le message de dominos sur le plateau et dominos visibles des autres joueurs
                    take_dominoes(names, play, main_dominoes, temp_dominoes, last_other_dominoes, temp_dice) # on prend les dominos du joueur
                    print(f"Dominos sur le plateau : {main_dominoes}\nDominos que tu possede : {temp_dominoes}\n"
                          f"Dominos visibles des autres joueurs : {last_other_dominoes}") # on affiche le message de dominos sur le plateau et dominos que le joueur possède
                    players_dominoes[play] = temp_dominoes # on met à jour players_dominoes[play]
            turn += 1 # on incrémente turn

    print("\n\n\n\n\nLe jeux est terminer nous allons voir le gagnant") # on affiche le message de fin de jeux
    point_players = [] # on initialise point_players à []
    for i in range(nb_players): # pour chaque i allant de 0 à nb_players
        temp_point_player = 0 # on initialise temp_point_player à 0
        for x in range(len(players_dominoes[i])): # pour chaque x allant de 0 à la taille de players_dominoes[i]
            if 24 >= players_dominoes[i][x] >= 21: # si players_dominoes[i][x] est compris entre 21 et 24
                temp_point_player += 1 # on incrémente temp_point_player
            if 28 >= players_dominoes[i][x] >= 25: # si players_dominoes[i][x] est compris entre 25 et 28
                temp_point_player += 2 # on incrémente temp_point_player
            if 32 >= players_dominoes[i][x] >= 29: # si players_dominoes[i][x] est compris entre 29 et 32
                temp_point_player += 3 # on incrémente temp_point_player
            if 36 >= players_dominoes[i][x] >= 33: # si players_dominoes[i][x] est compris entre 33 et 36
                temp_point_player += 4 # on incrémente temp_point_player
        point_players.append(temp_point_player) # on ajoute temp_point_player à point_players

    print(f"Le joueur ayant le plus de points est)\n"
          f"{names[point_players.index(max(point_players))]} avec {max(point_players)} vers !") # on affiche le message de gagnant
    print("\n\n\tFIN DU JEU") # on affiche le message de fin de jeux
