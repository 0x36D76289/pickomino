def take_dominoes(number_players, player, main_dominoes, temp_dominoes, last_other_dominoes, sum_dice):
    """ temp_dice, names, main_dominoes, temp_dominoes crée une liste takeable qui correspond aux dominos qui peuvent
    etre pris si 21 <= sum_dice <= 36 - Si sum_dice strictement égale à un entier dans last_other_dominoes - Si
    sum_dice strictement égale à un entier dans main_dominoes - Si sum_dice n'est pas strictement égale à un entier
    dans main_dominoes on ajoute l'entier le plus proche de sum_dice à takeable
    """
    # le caractere le plus proche de sum_dice dans main_dominoes
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
    # trie la liste takeable dans l'ordre croissant
    if len(takeable[1:]) == 0:
        return

    print(f"{number_players[player]} a comme dominos prennable : {takeable[1]}")
    choice = int(input("Quel dominos veut tu prendre : "))

    while choice not in takeable:
        choice = int(input("Quel dominos veut tu prendre : "))
    choice = int(choice)
    if choice in main_dominoes:
        # ajoute choice à temp_dominoes
        temp_dominoes.append(choice)
        # supprime choice de main_dominoes
        main_dominoes.remove(choice)
    if choice in last_other_dominoes:
        # ajoute choice à temp_dominoes
        temp_dominoes.append(choice)
        # supprime choice de last_other_dominoes
        last_other_dominoes.remove(choice)
    if choice == close_value:
        # ajoute choice à temp_dominoes
        temp_dominoes.append(choice)
        # supprime choice de main_dominoes
        main_dominoes.remove(choice)
    print(f"Vous avez pris {choice} à vos dominos")
    return


def skip_your_turn(main_dominoes: list[int], temp_dominoes: list[int]):
    """
    Si le dernier entier de temp_dominos est plus petit que le plus grand de la liste main_dominos,
     on l'ajoute à main_dominos et on le supprime de temp_dominos.
     si non on le supprime de temp_dominos.
    """
    if temp_dominoes[-1] < max(main_dominoes):
        main_dominoes.append(temp_dominoes[-1])
    temp_dominoes.pop()


def rolling_dice(number_dice):
    """
    On lance dice fois un des allant de 1 à 6
    """
    import random
    return [random.randint(1, 6) for _ in range(number_dice)]


def pass_your_turn(main_dominoes: list[int], temp_dominoes: list[int]):
    """
    Rend le dernier entier de temp_dominoes à main_dominoes
     Si cette entier est plus petit que le plus grand de la liste main_dominoes,
     on l'ajoute à main_dominoes et on le supprime de temp_dominoes.
    """
    print(f"Vous avez passé votre tour et rendu {temp_dominoes[-1]}")
    if temp_dominoes[-1] < max(main_dominoes):
        main_dominoes.append(temp_dominoes[-1])
    temp_dominoes.pop()
    print(f"Les dominos sur le plateau : {main_dominoes}\n"
          f"Vous avez maintenant       : {temp_dominoes}")


def choice_dice(number_players, player, temp_dice_roll, temps_dice):
    """
    Demande au joueur de choisir le nombre de dés qu'il veut lancer
    """
    if len(temps_dice) != 0:
        if all(i in temps_dice for i in temp_dice_roll):
            print(f"Tu as jeté que des dés {temp_dice_roll} que tu possèdes deja {temps_dice}, pas de chance")
            return -2
    choice = input(f"{number_players[player]}, Quel dominos veut tu prendre {temp_dice_roll} (N, pour arreter 1): ")

    if choice in ['n', 'N']:
        if 6 in temps_dice:
            return int(sum(temps_dice))
        return -1
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
        # tout les chiffres de temp_dice_roll sont dans temp_dice
        # regarde si tout les chiffres  de temp_dice_roll sont dans temps_dice
        # tout les chiffres de temp_dice_roll sont dans main_dominos
        choice = choice_dice(number_players, player, temp_dice_roll, temps_dice)
        if choice == sum(temps_dice):
            return sum(temps_dice)
        if choice == -1:
            return -1
        if choice == -2:
            return -2
        # ajoute tout les chiffres == choice à temp_dice et décrémente autant de fois number_dice
        for number in temp_dice_roll:
            if number == choice:
                temps_dice.append(number)
                number_dice -= 1
        print(f"Vous avez pris les dés {choice} : {temps_dice} = {sum(temps_dice)}")
    if 6 not in temps_dice:
        print("Vous n'avez pas de 6")
        return -1
    print()
    return int(sum(temps_dice))


if __name__ == "__main__":
    print("Pikomino")
    # Liste des dominos de 21 à 36
    main_dominoes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    print(main_dominoes)

    # Nombre de joueurs entre 2 et 7
    nb_players = int(input("Combien de joueurs ? "))
    while nb_players < 2 or nb_players > 7:
        nb_players = int(input("Combien de joueurs ? "))

    # Liste des dominos des joueurs dans une liste de listes
    players_dominoes = []
    for i in range(nb_players):
        players_dominoes.append([])

    # Liste des prenom des joueurs
    names = []
    for i in range(nb_players):
        names.append(input("Quel est le prénom du joueur " + str(i + 1) + " ? "))

    # Affiche le nom des joueurs et leurs dominos
    print(players_dominoes, names)

    # Debut du premier tour
    turn = 1
    # Boucle tant que dominos n'est pas vide

    while len(main_dominoes) > 15:
        for play in range(nb_players):
            print(f"\n\n\tTour {turn}\n\n")
            # Nombre de des à chaque tour définie à 8
            dice = 8
            main_dominoes.sort()  # tri la liste main_dominos par ordre croissant
            sum_dice = 0  # somme des dés du joueur
            temp_dominoes = players_dominoes[play]  # dominos du joueur temporaire
            last_other_dominoes = []  # dernier dominos des autres joueurs que player
            # si ce n'est pas le premier tour alors on ajoute les derniers dominos de chaque joueur à last_dominos
            for i in range(nb_players):
                if i != play:
                    if len(players_dominoes[i]) != 0:
                        last_other_dominoes.append(players_dominoes[i][-1])

            temp_dice = player_turn(play, names)  # Fait passer le premier tour au joueur play
            if temp_dice in [-1, -2]:
                if temp_dice == -1:
                    print(f"Vous n'avez pas de 6 dans vos dés")
                # Pas besoin d'afficher du texte la fonction choice_dice le fait déjà
                if len(temp_dominoes) != 0:
                    print("Vous passer votre tour")
                    pass_your_turn(main_dominoes, temp_dominoes)
                else:
                    print("Vous n'avez pas assez de dominos pour passer votre tour")
                continue

            else:
                print(f"Vous avez obtenu un score de {temp_dice} avec les dés")
                if not 21 > temp_dice or temp_dice > 36:
                    # Si 21 <= temp_dices <= 36
                    print(f"Dominos sur le plateau : {main_dominoes}"
                          f"Dominos visibles des autres joueurs : {last_other_dominoes}")
                    take_dominoes(names, play, main_dominoes, temp_dominoes, last_other_dominoes, temp_dice)
                    print(f"Dominos sur le plateau : {main_dominoes}\nDominos que tu possede : {temp_dominoes}\n"
                          f"Dominos visibles des autres joueurs : {last_other_dominoes}")
                    players_dominoes[play] = temp_dominoes
            turn += 1

    print("\n\n\n\n\nLe jeux est terminer nous allons voir le gagnant")
    point_players = []
    # Calcul la somme de chaque liste de players_dominoes
    for i in range(nb_players):
        temp_point_player = 0
        for x in range(len(players_dominoes[i])):
            if 24 >= players_dominoes[i][x] >= 21:
                temp_point_player += 1
            if 28 >= players_dominoes[i][x] >= 25:
                temp_point_player += 2
            if 32 >= players_dominoes[i][x] >= 29:
                temp_point_player += 3
            if 36 >= players_dominoes[i][x] >= 33:
                temp_point_player += 4
        point_players.append(temp_point_player)
    # affiche le joueur ayant le plus de points et le nombre de points qu'il a
    print(f"Le joueur ayant le plus de points est)\n"
          f"{names[point_players.index(max(point_players))]} avec {max(point_players)} vers !")
    print("\n\n\tFIN DU JEU")
