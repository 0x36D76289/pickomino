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

def sum_dice(dice):
    """dice: list -> int
    Affiche et affiche la somme de dice en prenant en compte que les 6 = 5
    """
    sum_dice = 0
    for dice in dice:
        if dice == 6:
            sum_dice += 5
        else:
            sum_dice += dice
    return sum_dice

def print_dice(dice):
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
    close_value = [i for i in main_dominoes if abs(sum_dice - i) == min(abs(sum_dice - i) for i in main_dominoes)]
    takeable = []

    if sum_dice in last_other_dominoes:
        temp_list = [i for i in last_other_dominoes if i == sum_dice]
        takeable += temp_list
    if sum_dice in main_dominoes:
        temp_list = [i for i in main_dominoes if i == sum_dice]
        takeable += temp_list
    if sum_dice != close_value:
        takeable.append(close_value)

    if len(takeable[1:]) == 0:
        return

    print(f"{number_players[player]} a comme dominos prennable : {list_to_point(takeable[1])}")
    choice = int(input("Quel dominos veut tu prendre : "))

    while choice not in takeable:
        choice = int(input("Quel dominos veut tu prendre : "))
    choice = int(choice)
    if choice in main_dominoes:
        temp_dominoes.append(choice)
        main_dominoes.remove(choice)
    if choice in last_other_dominoes:
        temp_dominoes.append(choice)
        last_other_dominoes.remove(choice)
    if choice == close_value:
        temp_dominoes.append(choice)
        main_dominoes.remove(choice)
    print(f"Vous avez pris {choice} à vos dominos")
    return


def skip_your_turn(main_dominoes, temp_dominoes):
    """
    Si le dernier entier de temp_dominos est plus petit que le plus grand de la liste main_dominos,
     on l'ajoute à main_dominos et on le supprime de temp_dominos.
     si non on le supprime de temp_dominos.
    """
    if temp_dominoes[-1] < max(main_dominoes):
        main_dominoes.append(temp_dominoes[-1])
    temp_dominoes.pop()


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
    print(f"Les dominos sur le plateau : {list_to_point(main_dominoes)}\n"
          f"Vous avez maintenant       : {temp_dominoes}")


def choice_dice(number_players, player, temp_dice_roll, temps_dice):
    """
    On demande à l'utilisateur de choisir le nombre de dés qu'il veut lancer
    """
    if len(temps_dice) != 0:
        if all(number in temps_dice for number in temp_dice_roll):
            print(f"Tu as jeté que des dés {print_dice(temp_dice_roll)} que tu possèdes deja {print_dice(temps_dice)}, pas de chance")
            return -2
    choice = input(f"{number_players[player]}, Quel dominos veut tu dés {print_dice(temp_dice_roll)} (N pour stop, 6 pour 'vers'): ")

    if choice in ['n', 'N']:
        if 6 in temps_dice:
            return int(sum(temps_dice))
        return -1
    # si choice est égale à vers on ajoute 6 à temp_dice_roll
    if choice in ['6', 'vers', 'VERS']:
        choice2 = 6
        return choice2
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
        temp_dice_roll = rolling_dice(number_dice)
        choice = choice_dice(number_players, player, temp_dice_roll, temps_dice)
        temp_dice_sum = sum(temp_dice_roll)
        if choice == temp_dice_sum:
            return temp_dice_sum
        if choice == -1:
            return -1
        if choice == -2:
            return -2
        for number in temp_dice_roll:
            if number == choice:
                temps_dice.append(number)
                number_dice -= 1
        print(f"Vous avez pris les dés {choice} : {print_dice(temps_dice)} = {sum_dice(temps_dice)}")
    if 6 not in temps_dice:
        print("Vous n'avez pas de vers")
        return -1
    print()
    return int(sum(temps_dice))


if __name__ == "__main__":
    print("Pikomino")
    main_dominoes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    print(list_to_point(main_dominoes))

    nb_players = int(input("Combien de joueurs ? "))
    while nb_players < 2 or nb_players > 7:
        nb_players = int(input("Combien de joueurs ? "))

    players_dominoes = []
    for i in range(nb_players):
        players_dominoes.append([])

    names = []
    for i in range(nb_players):
        names.append(input(f"Quel est le nom du joueur {i + 1} ? "))
    print(players_dominoes, names)

    turn = 1
    while len(main_dominoes) > 0:
        for play in range(nb_players):
            print(f"\n\n\tTour {turn}\n\n")
            dice = 8
            main_dominoes.sort()
            sum_dice = 0
            temp_dominoes = players_dominoes[play]
            last_other_dominoes = []
            for i in range(nb_players):
                if i != play:
                    if len(players_dominoes[i]) != 0:
                        last_other_dominoes.append(players_dominoes[i][-1])

            temp_dice = player_turn(play, names)
            if temp_dice in [-1, -2]:
                if temp_dice == -1:
                    print(f"Vous n'avez pas de 6 dans vos dés")
                if len(temp_dominoes) != 0:
                    print("Vous passer votre tour")
                    pass_your_turn(main_dominoes, temp_dominoes)
                else:
                    print("Vous n'avez pas assez de dominos pour passer votre tour")
                continue

            else:
                print(
                    f"Vous avez obtenu un score de {temp_dice} avec les dés")
                if not 21 > temp_dice or temp_dice > 36:
                    print(f"Dominos sur le plateau : {list_to_point(main_dominoes)}\n"
                          f"Dominos visibles des autres joueurs : {list_to_point(last_other_dominoes)}")
                    take_dominoes(names, play, main_dominoes, temp_dominoes, last_other_dominoes, temp_dice)
                    print(f"Dominos sur le plateau : {list_to_point(main_dominoes)}\nDominos que tu possede : {list_to_point(temp_dominoes)}\n"
                          f"Dominos visibles des autres joueurs : {list_to_point(last_other_dominoes)}")
                    players_dominoes[play] = temp_dominoes
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

    print(f"Le joueur ayant le plus de points est)\n"
          f"{names[point_players.index(max(point_players))]} avec {max(point_players)} vers !")
    print("\n\n\tFIN DU JEU")
