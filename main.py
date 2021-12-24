
def dict_dominoes(dominoes):
	"""
	créer un disctionnaire avec les entier de la liste dominoes avec comme leurs points associer et affiche leurs points avec leurs valeurs dans dominoes
	- si le dominoe est entre 21 et 24 = 1;
	- si le dominoe est entre 25 et 28 = 2;
	- si le dominoe est entre 29 et 32 = 3;
	- si le dominoe est entre 33 et 36 = 4.
	"""
	points = []
	for i in dominoes:
		if i in range(21, 25):
			points.append(1)
		elif i in range(25, 29):
			points.append(2)
		elif i in range(29, 33):
			points.append(3)
		elif i in range(33, 37):
			points.append(4)
	return dict(zip(dominoes, points))

def print_players(list_noms):
	"""
	Créer un dictionnaire qui assosie le nom du joueur avec son numéro (0, 1, 2, etc en foction de leurs ordre d'apparaition dans la liste)
	"""
	players = []
	for i in range(len(list_noms)):
		players.append({"nom": list_noms[i], "numéro": i+1})
	return players

def list_dominoes_all_player(dominoes):
	"""
	créer un dictionnaire qui affiche Les dominos des autres joueurs avec dict_dominoes()
	"""
	list_dominoes = []
	for i in range(len(dominoes)):
		list_dominoes.append(dict_dominoes(dominoes[i]))
	return list_dominoes

def print_dice(dice):
	"""
	Ajoute les valeurs de dice si cette valeurs est de 6 alors on ajoute "vers" dans une liste
	"""
	dice_vers = []
	for i in dice:
		if i == 6:
			dice_vers.append("vers")
		else:
			dice_vers.append(i)
	return dice_vers

def sum_dice(dice):
	"""
	Somme les valeurs de dice si la valeur est de 6 on ajoute 5
	"""
	sum_dice = 0
	for i in dice:
		if i == 6:
			sum_dice += 5
		else:
			sum_dice += i
	return sum_dice

def rolling_dice(number_dice):
	"""
	créer une liste de nombre aléatoire entre 1 et 6
	"""
	import random
	return [random.randint(1, 6) for i in range(number_dice)]

def player_turn(name):
	"""
	Tant que le joueur veux jouer on lance les des tant que:
	- le nombre de dice est différent de 0
	- tout les chiffres de 1 à 6 soit dans la main du joueur
	"""
	dice = 8
	player_dice = []
	turn = 1
	while dice != 0:
		print("-----------------")
		# Demande au joueur si il veut lancer les des
		print(f"{name}, veux tu lancer les des? (oui/non)")
		answer = input()
		# Tant que answer est différent de oui ou non on continue
		while answer != "oui" and answer != "non":
			print("Je n'ai pas compris ta réponse, veux tu lancer les des? (oui/non)")
			answer = input()
		# Si le joueur veux lancer les des
		if answer == "oui":
			# Lancer les des
			temps_dice = rolling_dice(dice)
			print(f"{name} a lancé les des: {print_dice(temps_dice)}")
			# Si player_dice n'est pas vide et que toutes les valeurs de temps_dice sont deja dans player_dice
			if player_dice != [] and all(i in player_dice for i in temps_dice):
				print(f"{name} a déjà joué avec ces dés")
				return -1
			# Demande au joueurs quelle des il veut garder
			print(f"{name}, quelle dés veux tu garder (6 pour vers) ?")
			answer = input()
			# tant que answer n'est pas un entier on repose la question
			while not answer.isdigit():
				print("Je n'ai pas compris ta réponse, quelle dés veux tu garder ?")
				answer = input()
			# tant que answer est danas temps_dice et n'est pas dans player_dice on repose la question
			while int(answer) not in temps_dice or int(answer) in player_dice:
				print("Je n'ai pas compris ta réponse, quelle dés veux tu garder ?")
				answer = input()
			answer = int(answer)
			# Si le joueur veux garder les des
			for i in temps_dice:
				if answer == i:
					player_dice.append(i)
					dice -= 1
			# affiche les dés du joueurs et leurs sum_dice
			print(f"{name} a gardé: {print_dice(player_dice)}")
			print(f"{name} a {sum_dice(player_dice)} points")
			# affiche le nombre de dés restant
			print(f"Il reste {dice} dés")
		# si 6 n'est pas dans player_dice et que le joueur veux pas lancer les des
		if answer == "non":
			if 6 not in player_dice:
				print(f"{name} tu n'as pas de vers")
				print("-----------------")
				return -1
			print("-----------------")
			return player_dice
	# si il n'a pas de 6
	if 6 not in player_dice:
		print(f"{name} tu n'as pas de vers")
		return -1
	return player_dice

def pass_your_turn():
	"""
	Rend le dernier entier des dominos du joueur et supprime le plus grand de main_dominoes
	"""
	# affiche les dominos du joueur
	print(f"{list_noms[i]} a : {dict_dominoes(list_dominoes[i])}")
	# ajoute la derniere valeur de list_dominoes[i] dans main_dominoes
	main_dominoes.append(list_dominoes[i][-1])
	# supprime le derier domino de player_dice
	list_dominoes[i].pop()
	print(f"Tu as maintenant {dict_dominoes(list_dominoes[i])}")
	# supprime le domino le plus grand de main_dominoes
	main_dominoes.sort()
	main_dominoes.remove(max(main_dominoes))
	# affiche les dominos qu'il reste
	print(f"Il reste {dict_dominoes(main_dominoes)} sur le plateau")


if __name__ == "__main__":
	print("Pikomino")

	main_dominoes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
	print(dict_dominoes(main_dominoes))

	# Demande à l'utilistaeur le nombre de joueurs entre 2 et 7 les deux compris
	nb_joueurs = int(input("Combien de joueurs ? "))
	while nb_joueurs < 2 or nb_joueurs > 7:
		nb_joueurs = int(input("Combien de joueurs ? "))
	# demande à l'utilistaeur le noms des joueurs
	list_noms = []
	for i in range(nb_joueurs):
		list_noms.append(input("Nom du joueur {} ? ".format(i+1)))
	# créer une liste des dominos des joueurs
	list_dominoes = []
	for i in range(nb_joueurs):
		list_dominoes.append([])
	print("Le jeux peux commencer")
	print("Les joueurs sont : {}".format(print_players(list_noms)))
	print("Les dominos sont : {}".format(dict_dominoes(main_dominoes)))

	# commence le jeux jusqua ce que main_dominoes soit vide en comptanat les tours
	turn = 1
	while len(main_dominoes) > 0:
		# affiche le tour
		print("-----------------")
		print("Tour {}".format(turn))
		print("-----------------")
		# chaque joueurs joue
		for i in range(nb_joueurs):
			print("{} joue".format(list_noms[i]))

			# affiche les dominos du joueur, des autres joueurs, et des dominos restants
			print("{} dominos : {}".format(list_noms[i], dict_dominoes(list_dominoes[i])))
			print("Les dominos des autres joueurs : {}".format(list_dominoes_all_player(list_dominoes)))
			print("Les dominos restants : {}".format(dict_dominoes(main_dominoes)))
			# créer une liste des derniers entier de chaque liste de list_dominoes
			last_dominoes = []
			for j in range(nb_joueurs):
				# si j est différent de i
				if j != i and list_dominoes[j] != []:
					last_dominoes.append(list_dominoes[j][-1])
			# Deamnde au joueurs de choisirs les dés
			player_dice = player_turn(list_noms[i])
			# Si le joueur a des dominos et que player_dice est égale à -1
			if player_dice == -1:
				if list_dominoes[i] != []:
				# affiche le joueur a perdu
					print(f"{list_noms[i]} passe ton tour, tu doit rendre un domino")
					pass_your_turn()
				else:
					print(f"{list_noms[i]} n'as pas assez de dominos pour passer sont tour")
			else:
				player_dice = sum_dice(player_dice)
				# si player_dice est entre le minimum de main_dominoes ou de last_dominoes et le maximum de main_dominoes
				if (player_dice >= min(main_dominoes) and player_dice <= max(main_dominoes)) or player_dice in last_dominoes:
					# créer une variable correspondant à la valeur la plus proche de player_dice
					closest_value = min(main_dominoes, key=lambda x:abs(x-player_dice))
					# créer une liste des dominos prennable c'est à dire si il est dans main_dominoes et ou si il est exactement égal à une valeur dans last_dominoes
					prenable_dominoes = []
					take = 0
					if player_dice in last_dominoes:
						prenable_dominoes.append(player_dice)
						take = 1
					elif player_dice in main_dominoes:
						prenable_dominoes.append(player_dice)
						take = 2
					else:
						prenable_dominoes.append(closest_value)
						take = 3
					# Si il n'y a aucun dominoes prennable
					if prenable_dominoes == []:
						print(f"{list_noms[i]} n'a pas de dominos prennable")
					else:
						# affiche les dominoes sur le plateau
						print(f"Mes dominos sur le plateau sont : {dict_dominoes(main_dominoes)}")
						# affiche les dominos des autres joueurs
						print(f"Les autres joueurs dominos ont : {dict_dominoes(last_dominoes)}")
						# affiche les dominoes prennable
						print(f"{list_noms[i]} peut prendre : {dict_dominoes(prenable_dominoes)}")
						# demande au joueur quel dominos il veut prendre
						domino_choice = int(input(f"{list_noms[i]} choisis un domino : "))
						# Si le joueur a choisi un domino qui n'est pas dans prenable_dominoes
						while domino_choice not in prenable_dominoes:
							domino_choice = int(input(f"{list_noms[i]} choisis un domino : "))
						
						# Si take = 1 alors on ajoute le domino_choice à la liste de list_dominoes[i]
						if take == 1:
							list_dominoes[i].append(domino_choice)
							# parcours chaque liste de list_dominoes et supprime le carractere dominos_choice
							for j in range(nb_joueurs):
								if j != i and domino_choice in list_dominoes[j]:
									list_dominoes[j].remove(domino_choice)
						# Si take = 2 alors on ajoute le domino_choice à la liste de list_dominoes[i] et on supprime le domino_choice de main_dominoes
						elif take == 2:
							list_dominoes[i].append(domino_choice)
							main_dominoes.remove(domino_choice)
						# Si take = 3 alors on ajoute le closest_value à la liste de list_dominoes[i] et on supprime le closest_value de main_dominoes
						elif take == 3:
							list_dominoes[i].append(closest_value)
							main_dominoes.remove(closest_value)
				else:
					# le joueur n'as pas une valeur suffisante pour prendre un domino
					print(f"{list_noms[i]} n'a pas une valeur suffisante pour prendre un domino")
				# affiche les dominos du joueur, des autres joueurs, et des dominos restants
				last_dominoes = []
				for j in range(nb_joueurs):
					# si j est différent de i
					if j != i and list_dominoes[j] != []:
						last_dominoes.append(list_dominoes[j][-1])
				print("-----------------")
				print("{} dominos : {}".format(list_noms[i], dict_dominoes(list_dominoes[i])))
				print("Les dominos des autres joueurs : {}".format(dict_dominoes(last_dominoes)))
				print("Les dominos restants : {}".format(dict_dominoes(main_dominoes)))
				print("-----------------")
		# met à jour le tour
		turn += 1
	# affiche le gagnant
	print("Le gagnant est : {}".format(list_noms[list_dominoes.index(max(list_dominoes))]))
	# affiche les dominos du gagnant
	print("Les dominos du gagnant : {}".format(dict_dominoes(list_dominoes[list_dominoes.index(max(list_dominoes))])))
	# affiche un tableau des scores de chaque joueurs
	print("Tableau des scores :")
	for i in range(nb_joueurs):
		# affiche les dominos du joueur
		print(f"{list_noms[i]} dominos : {dict_dominoes(list_dominoes[i])}")
		print(f"{list_noms[i]} : {sum_dice(list_dominoes[i])}")
