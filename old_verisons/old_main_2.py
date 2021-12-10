def list_to_point(list_dominoes):
    """ list_dominoes: list -> dict
    Renvoie la liste des dominos en points avec :
    21 à 24 = 1,
    25 à 28 = 2,
    29 à 32 = 3,
    33 à 36 = 4
    """
    point_dominoes = []
    for domino in list_dominoes:
        if domino in range(21, 25):
            point_dominoes.append(1)
        elif domino in range(25, 29):
            point_dominoes.append(2)
        elif domino in range(29, 33):
            point_dominoes.append(3)
        elif domino in range(33, 37):
            point_dominoes.append(4)
    # crée un dictionnaire avec les dominos et les points
    point_dominoes = dict(zip(list_dominoes, point_dominoes))
    return point_dominoes

def sum_dice(dice:list):
    """dice: list -> int
    Affiche et affiche la somme de dice en prenant en compte que les 6 = 5
    """
    sum_dice = 0
    for i in dice:
        if i in ['vers', 6]:
            sum_dice += 5
        else:
            sum_dice += i
    return sum_dice

def print_dice(dice:list):
    """
    crée une liste de dés en remplaçant les 6 par un "vers"
    """
    dice_print = []
    for dice in dice:
        if dice == 6:
            dice_print.append("vers")
        else:
            dice_print.append(dice)
    return dice_print


def take_dominoes(number_players, player, main_dominoes, temp_dominoes, last_other_dominoes, sum_dice):
    """ temp_dice, names, main_dominoes, temp_dominoes crée une liste takeable qui correspond aux dominos qui peuvent
    etre pris si 21 <= sum_dice <= 36 - Si sum_dice strictement égale à un entier dans last_other_dominoes - Si
    sum_dice strictement égale à un entier dans main_dominoes - Si sum_dice n'est pas strictement égale à un entier
    dans main_dominoes on ajoute l'entier le plus proche de sum_dice à takeable
    """
    print("----------------------------------------------------")
    # ajoute la valeur la plus proche de sum_dice dans main_dominoes close_value, si il yen a deux qui ont le meme equart on choisi la valeur la plus petite
    close_value = min(main_dominoes, key=lambda x: abs(x - sum_dice))
    # close_value = [i for i in main_dominoes if abs(sum_dice - i) == min(abs(sum_dice - i) for i in main_dominoes)]
    takeable = []

    # si sum_dice est strictement égale à un entier dans last_other_dominoes on l'joute à la liste takeable
    take = 0
    if sum_dice in last_other_dominoes:
        takeable.append(sum_dice)
        take = 1
    
    # si sum_dice est strictement égale à un entier dans main_dominoes on l'joute à la liste takeable
    elif sum_dice in main_dominoes:
        takeable.append(sum_dice)
        take = 2
    
    # si sum_dice n'est pas strictement égale à un entier dans main_dominoes on ajoute l'entier le plus proche de sum_dice à takeable
    else:
        takeable.append(close_value)
        take = 3

    if len(takeable) == 0:
        return
    # affiche les dominos qui peuvent etre pris avec le nom du joueur
    print("{} peut prendre : {}".format(number_players[player], takeable))
    # demande au joueur de choisir un domino
    choice = input("Choisissez un domino : ")    

    while int(choice) not in takeable:
        choice = input("Quel dominos veut tu prendre : ")
    choice = int(choice)
    # si chocie est dans main_dominoes on le supprime de main_dominoes et on l'ajoute dans temp_dominoes
    if take == 1:
        temp_dominoes.append(choice)
        last_other_dominoes.remove(choice)
    elif take == 2:
        main_dominoes.remove(choice)
        temp_dominoes.append(choice)
    else:
        temp_dominoes.append(close_value)
        main_dominoes.remove(close_value)


    print(f"Vous avez ajouter {choice} à vos dominos")
    print("----------------------------------------------------")
    return

def rolling_dice(number_dice) :
    """
    On lance dice fois un des allant de 1 à 6
    """
    import random
    return [random.randint(1, 6) for _ in range(number_dice)]


def pass_your_turn(main_dominoes, temp_dominoes):
    """
    Rend le dernier entier de temp_dominoes à main_dominoes
     Si cette entier est plus petit que le plus grand de la liste main_dominoes,
     on l'ajoute à main_dominoes et on le supprime de temp_dominoes.
    """
    print(f"Vous avez passé votre tour et rendu {temp_dominoes[-1]}")
    if temp_dominoes[-1] < max(main_dominoes):
        main_dominoes.append(temp_dominoes[-1])
    temp_dominoes.pop()
    main_dominoes.sort()
    main_dominoes.pop()
    print(f"Les dominos sur le plateau 1: {list_to_point(main_dominoes)}\n"
          f"Vous avez maintenant       1: {list_to_point(temp_dominoes)}")


def choice_dice(number_players, player, temp_dice_roll, temps_dice):
    """
    On demande à l'utilisateur de choisir le nombre de dés qu'il veut lancer
    """
    if len(temps_dice) != 0: # si le joueur a déjà joué
        if all(number in temps_dice for number in temp_dice_roll): # si tous les dés sont dans temps_dice
            print(f"Tu as jeté que des dés {print_dice(temp_dice_roll)} que tu possèdes deja {print_dice(temps_dice)}, pas de chance")
            return -2

    # Deamnde au joueur de choisir entre les valeurs de tmep_dice_roll qu'il veut garder en str
    print(f"{number_players[player]} a comme dés disponibles : {print_dice(temp_dice_roll)}")
    choice = input("Quel dés veut tu garder : ")
    
    # choice = str(input(f"{number_players[player]}, Quel dés veut tu dés {print_dice(temp_dice_roll)} (6 pour 'vers'): "))

    # si choice est égale à vers on ajoute 6 à temp_dice_roll
    if choice in ['6', 'vers', 'VERS']:
        return 6
    choice = int(choice)
    if choice not in temp_dice_roll:
        print("Tu ne peux pas prendre un des que tu n'a pas lancer")
        return choice_dice(number_players, player, temp_dice_roll, temps_dice)
    if choice in temps_dice:
        print("Tu ne peux pas prendre un des que tu possede deja")
        return choice_dice(number_players, player, temp_dice_roll, temps_dice)
    return choice


def player_turn(player, number_players):
    """
    Tant que le nombre de dés != 0 , on lance le dés tant que :
    - dice != 0
    - tout les chiffres de 1 à 6 ne sont pas dans temp_dice
    - l'utilisateur ne veut pas prendre de des avec "n" ou "N"
    """
    number_dice = 8
    temps_dice = []
    throw_of_dice = 0
    while number_dice > 0:
        throw_of_dice += 1
        print("----------------------------------------------------")
        end = input(f"{number_players[player]}, veux tu arrêter à lancer des dés ? (O/N) : ")
        while end not in ['o', 'O', 'n', 'N']:
            end = input("Veuillez entrer O ou N : ")

        if end not in ['o', 'O']:
            temp_dice_roll = rolling_dice(number_dice)
            choice = choice_dice(number_players, player, temp_dice_roll, temps_dice)
            if choice == -1:
                return -1
            if choice == -2:
                return -2
            for number in temp_dice_roll:
                if number == choice:
                    temps_dice.append(number)
                    number_dice -= 1
            # affiche les des que vous avez pris avec print_dice et affiche leurs somme avec sum_dice
            print(f"Vous avez maintenant {print_dice(temps_dice)}")
            #afffiche sum_dice(temps_dice)
            print(f"La somme de ces dés est de {sum_dice(temps_dice)}")
            continue
        if sum_dice(temps_dice) == 0:
            return 0
        return sum_dice(temps_dice)
    # si 6 ou 'vers' n'est pas dans temp_dice alors afficher "Vous n'avez pas de vers" retretourner -1
    if 6 not in temps_dice and 'vers' not in temps_dice:
        print("Vous n'avez pas de vers")
        return -1
    return sum_dice(temps_dice)


if __name__ == "__main__":
    print("----------------------------------------------------")
    print("----------------------Pikomino----------------------")
    print("----------------------------------------------------")
    main_dominoes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    print(list_to_point(main_dominoes))

    nb_players = input("Combien de joueurs ? ")
    # tant que nb_players n'est pas un int et entre 2 et 7 compris on redemande
    while int(nb_players) not in [2, 3, 4, 5, 6, 7]:
        nb_players = input("Combien de joueurs ? ")
    nb_players = int(nb_players)

    players_dominoes = []
    for i in range(nb_players):
        players_dominoes.append([])

    names = []
    print("----------------------------------------------------")
    for i in range(nb_players):
        names.append(input(f"Quel est le nom du joueur {i + 1} ? "))
    
    print("----------------------------------------------------")
    print(players_dominoes, names)
    print("----------------------------------------------------")

    turn = 1
    while len(main_dominoes) > 0:
        for play in range(nb_players):
            print(f"\t\tTour {turn}")
            # affche le nom du joueur
            print(f"\t\t{names[play]}")
            print("----------------------------------------------------")
            #affiche les dominos des joueurs et sur le plateau
            print(f"Les dominos du joueur : {list_to_point(players_dominoes[play])}")
            # affiche les dominos des joueurs
            print(f"Les dominos des autres joueurs (temporaire) : {players_dominoes}")
            print(f"Les dominos sur le plateau 2 : {list_to_point(main_dominoes)}")
            
            dice = 8
            main_dominoes.sort()
            temp_dominoes = players_dominoes[play]
            last_other_dominoes = []
            for i in range(nb_players):
                if i != play:
                    if len(players_dominoes[i]) != 0:
                        last_other_dominoes.append(players_dominoes[i][-1])

            temp_dice = player_turn(play, names)
            print("----------------------------------------------------")
            if temp_dice in [0, -1, -2]:
                if temp_dice == 0:
                    print("Vous n'avez pris aucun dés")
                elif len(temp_dominoes) != 0:
                    print("Vous passer votre tour")
                    pass_your_turn(main_dominoes, temp_dominoes)
                else:
                    print("Vous n'avez pas assez de dominos pour passer votre tour")
                print("----------------------------------------------------")
                continue
        
            else:
                # print(f"Vous avez obtenu un score de {temp_dice} avec les dés")
                # si temp_dice est entre 21 et 36 compris
                if 21 <= int(temp_dice) <= 36:
                    print(f"Vous avez obtenu un score de {temp_dice} avec les dés")
                    # print(f"Dominos sur le plateau 3: {list_to_point(main_dominoes)}\n"
                    #       f"Dominos visibles des autres joueurs : {list_to_point(last_other_dominoes)}\n"
                    #       f"Dominos des autres joueurs (temporaire) : {players_dominoes}\n")
                    take_dominoes(names, play, main_dominoes, temp_dominoes, last_other_dominoes, temp_dice)
                    # met à jour la liste des dominos des autres joueurs
                    print(f"Dominos sur le plateau 4: {list_to_point(main_dominoes)}\nDominos que tu possede : {list_to_point(temp_dominoes)}\n"
                          f"Dominos visibles des autres joueurs : {list_to_point(last_other_dominoes)}\n"
                          f"Dominos des autres joueurs (temporaire) : {players_dominoes}\n")
                    players_dominoes[play] = temp_dominoes
                else:
                    print("Vous n'avez pas obtenu un score suffisant pour prendre un domino")
            main_dominoes.sort()
            print("----------------------------------------------------")
            turn += 1

    print("\n\n\n\n\nLe jeux est terminer nous allons voir le gagnant")
    point_players = []
    dict_main_dominoes = list_to_point(main_dominoes)
    # dictionnaire de valeur aléatoire mais avec un index trier dans l'ordre croissant
    dict_main_dominoes = dict(sorted(dict_main_dominoes.items(), key=lambda x: x[1]))
    # ajoute chaque point de dict_main_dominoes dans point_players si le dominos est égal à la valeur du dominos
    for dominos in dict_main_dominoes:
        if dict_main_dominoes[dominos] == dominos:
            point_players.append(dominos)
    print("----------------------------------------------------")
    print(f"Le joueur ayant le plus de points est)\n"
          f"{names[point_players.index(max(point_players))]} avec {max(point_players)} vers !")
    print("----------------------------------------------------")
    print("\n\n\tFIN DU JEU")
    print("----------------------------------------------------")