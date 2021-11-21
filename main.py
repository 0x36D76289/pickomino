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
	""" Fonction qui permet de prendre le pikominos d'un autre joueur
	Fonction qui ajoute le pikominos au joueur
	:param pikominos_joueur: liste des pikominos du joueur
	:param pikominos_autre_joueurs: liste des pikominos des autres joueurs
	:param need_pikominos: pikominos que le joueur veut prendre
	:return: pikominos_joueur:list et pikominos_autre_joueurs:list
	"""
	pikominos_joueur.append(need_pikominos) # on ajoute le pikominos au joueur
	# on supprime le derniere element de la liste pikominos_autre_joueurs
	pikominos_autre_joueurs.remove(pikominos_autre_joueurs[-1])
	return pikominos_joueur, pikominos_autre_joueurs # 

def takeClosest(myList:list, myNumber:int) -> int:
	return min(myList, key=lambda x:abs(x-myNumber))

def sur_plateau(pikominos:list, pikominos_joueur:list, need_pikominos:int):
	pikominos_joueur.append(need_pikominos)
	pikominos.remove(need_pikominos)
	return pikominos_joueur, pikominos

def prendre_pikominos_proche(pikominos:list, need_pikominos:int, pikominos_joueur:list):
	"""
	ajoute à pikominos_joueurs le le caractere pikominos_a_prendre et le supprime de pikominos
	"""
	pikominos_joueur.append(need_pikominos)
	pikominos.remove(need_pikominos)
	return pikominos_joueur, pikominos

def prendre_pikominos(pikominos:list, pikominos_joueur:list, pikominos_autre_joueurs:list, somme_des:int):
	""" 
	Si la somme des dés est dans la liste pikominos, on prend le pikominos de la liste
	Si la somme des dés est dans la liste pikominos_autre_joueurs, on prend le pikominos de la liste
	Si aucune d'entre elle est dans la liste, on prend le pikominos le plus proche de la somme des dés dans la liste pikominos
	:param pikominos: liste des pikominos
	:param pikominos_joueur: liste des pikominos du joueur
	:param pikominos_autre_joueurs: liste des pikominos des autres joueurs
	:somme_des: somme des dés
	:return: pikominos_joueur:list et pikominos:list et pikominos_autre_joueurs:list
	"""
	print("\t{}, {}, {}".format(pikominos, pikominos_joueur, pikominos_autre_joueurs))
	if 21 <= somme_des <= 36:
		number_list = 0
		if somme_des in pikominos:
			pikominos_eligible = [i for i in pikominos if i == somme_des]
			number_list = 1
		elif somme_des in pikominos_autre_joueurs:
			pikominos_eligible = [i for i in pikominos_autre_joueurs if i == somme_des]
			number_list = 2
		else:
			pikominos_eligible = [i for i in pikominos if i == takeClosest(pikominos, somme_des)]
			number_list = 3

		need_pikominos = int(input("Quel pikominos veut tu prendre {} somme des = {} :  ".format(pikominos_eligible, somme_des)))
		if need_pikominos in pikominos_eligible:
			if number_list == 1: # si le pikominos est sur le plateau
				pikominos_joueur, pikominos = sur_plateau(pikominos, pikominos_joueur, need_pikominos)
			elif number_list == 2: # si le pikominos n'est pas sur le plateau mais que tu vex prendre celui le plus proche inférieur
				pikominos_joueur, pikominos_autre_joueurs = autre_joueur(pikominos_joueur, pikominos_autre_joueurs, need_pikominos)
			else: # si le pikominos n'est pas sur le plateau mais que tu vex prendre celui le plus proche inférieur
				pikominos_joueur, pikominos = prendre_pikominos_proche(pikominos, need_pikominos, pikominos_joueur)
			print("\t{}, {}, {}".format(pikominos, pikominos_joueur, pikominos_autre_joueurs))
			return pikominos, pikominos_joueur, pikominos_autre_joueurs
		return prendre_pikominos(pikominos, pikominos_joueur, pikominos_autre_joueurs, somme_des)
	print("Tu en peux pas prendre de dés car {} n'est pas dans l'interval 21 <= n <= 36".format(somme_des))
	return pikominos_joueur, pikominos, pikominos_autre_joueurs

def pass_ton_tour(pikominos:list, pikominos_joueur:list):
	"""
	Rend le dernier pikominos du joueur et le met dans la list pikominos, si il est le plus pikominos le plus élever apres sont ajout on le supprime
	"""
	print("Tu as perdu le pikominos {}" .format(pikominos_joueur[-1]))
	if max(pikominos) > int(pikominos_joueur[-1]):
		print("Le Pickominos {} as été remis sur le plateau".format(pikominos_joueur[-1]))
		pikominos.append(pikominos_joueur[-1])
		pikominos_joueur.pop()
	else: 
		print("Le Pickominos {} as été remis sur le plateau mais il n'est plus disponible car c'est le plus grand".format(pikominos_joueur[-1]))
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
	#si tout les chiffres du temp_des_lancer est dans temp_des_poches on passe sont tour
	if all(x in temp_des_poche for x in temp_des_lancer):
		print("Tu passe ton tour")
		return [0], -2
	need_dominos = input("Quel dominos veut tu prendre : ")
	if need_dominos == "n":
		if 6 in temp_des_poche:
			return temp_des_poche, -3
		print("Tu passe ton tour")
		return [0], -1
	if int(need_dominos) in temp_des_lancer:
		if int(need_dominos) in temp_des_poche:
			print("Tu ne peux pas prendre un dominos qui tu possede deja")
			return condition(pikominos, pikominos_joueur, temp_des_poche, temp_des_lancer, nombre_des)
	else:
		print("Tu ne peux pas prendre un dominos qui n'est pas disponible")
		return condition(pikominos, pikominos_joueur, temp_des_poche, temp_des_lancer, nombre_des)
	temp_des_poche, nombre_des = condition2(temp_des_lancer, temp_des_poche, need_dominos, nombre_des)
	return temp_des_poche, nombre_des

def tour(joueur, pikominos:list, pikominos_joueur:list) -> int:
	""" joueur: int, pikominos: list, pikominos_joueur: list -> int
	"""
	pikominos.sort()
	temp_des_poche = []
	nombre_des = 8
	while nombre_des != 0:
		temp_des_lancer = lance_des(nombre_des)
		print("{} a lancé les dés : {}".format(joueur, temp_des_lancer))
		temp_des_poche, nombre_des = condition(pikominos, pikominos_joueur, temp_des_poche, temp_des_lancer, nombre_des) # on vérifie si la condition 2 est respectée
		if temp_des_poche == [0] and nombre_des == -1: # si le joueur a passé son tour
			return -1
		if nombre_des == -2:
			return -2
		if nombre_des == -3:
			return sum(temp_des_poche)
		print("{} a prit les dominos {} = {}".format(joueur, temp_des_poche, sum(temp_des_poche)))
	print("Vous ne pouvez plus lancer de des")
	if 6 not in temp_des_poche:
		return -1
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

	# Création de la liste des pikominos des joueurs
	for i in range(nombre_joueurs):
		pikominos_joueur.append([])

	print("Joueurs :\n{}\nPikominos des joueurs\n{}\nC'est au joueurs 1 de commencer".format(liste_joueur, pikominos_joueur))
	tours = 1
	#le jeux commence
	while len(vers) != 0:
		nombre_des = 8 # nombre de dés à lancer
		for joueur in range(nombre_joueurs):
			somme_des = 0
			vers_joueurs = []
			vers_autre_joueurs = []
			if len(pikominos_joueur[joueur]) != 0: # si le joueur a des pikominos
				for i in range(len(pikominos_joueur[joueur])):
					vers_joueurs.append(pikominos_joueur[joueur][-1])
			print(vers_autre_joueurs)
			print("\n\tTour {}\n\tPikominos sur plateau {}\n\tPikominos autre joueurs {}\n".format(tours, vers, pikominos_joueur))
			somme_des = tour(liste_joueur[joueur], vers, vers_joueurs)
			#crée une liste vers_autre_joueurs qui contient tout les derniers caracteres des listes dasn la liste pikominos_joueur sauf celui du joueurs en cours
			if tours != 1: # si la liste n'est pas vide
				for i in range(nombre_joueurs): # on parcours la liste des joueurs
					if i != joueur: # si le joueur n'est pas celui en cours
						if len(pikominos_joueur[i]) != 0: # si la liste n'est pas vide
							vers_autre_joueurs.append(pikominos_joueur[i][-1]) # on ajoute le dernier caractere de la liste dans la liste vers_autre_joueurs
						else: # si la liste est vide
							vers_autre_joueurs.append(0) # on ajoute 0 dans la liste vers_autre_joueurs
			else:
				vers_autre_joueurs = []
				vers_joueurs = []
			vers = sorted(vers)
			#vers_autre_joueurs = sorted(vers_autre_joueurs)
			#vers_joueurs = sorted(vers_joueurs)
			if len(vers_joueurs) != 0:
				if somme_des == -1:
					print("{} a perdu car il n'a pas de 6".format(liste_joueur[joueur-1]))
					#pass ton tour
					vers_joueurs, pikominos_joueur[joueur] = pass_ton_tour(vers, vers_joueurs)
					continue
				if somme_des == -2:
					print("{} a perdu car il a jeter que des des qu'il possede deja".format(liste_joueur[joueur]))
					vers_joueurs, pikominos_joueur[joueur] = pass_ton_tour(vers, vers_joueurs)
					continue
			else:
				if somme_des == -1:
					print("{} a perdu car il n'a pas de 6 mais tu ne peux rendre aucun pikominos".format(liste_joueur[joueur]))
					continue
				if somme_des == -2:
					print("{} a perdu car il a jeter que des des qu'il possede deja".format(liste_joueur[joueur]))
					continue
			print("{} a obtenu un score de {} avec les des".format(liste_joueur[joueur], somme_des))
			#pikominos_joueur, pikominos, pikominos_autre_joueurs
			vers, vers_joueurs, vers_autre_joueurs = prendre_pikominos(vers, vers_joueurs, vers_autre_joueurs, somme_des)
			#supprime les doublons de la liste vers_joueurs
			vers_joueurs_temp = []
			for i in vers_joueurs:
				if i not in vers_joueurs_temp:
					vers_joueurs_temp.append(i)
			vers_joueurs = vers_joueurs_temp
			vers_autre_joueurs_temp = []
			for i in vers_autre_joueurs:
				if i not in vers_joueurs:
					vers_autre_joueurs_temp.append(i)
			vers_autre_joueurs = vers_autre_joueurs_temp
			print("{} a les pikominos {}".format(liste_joueur[joueur], vers_joueurs))
			pikominos_joueur[joueur] = vers_joueurs
			tours += 1

	max_score = 0
	gagnant = 0
	for i in range(nombre_joueurs):
		for x in range(len(pikominos_joueur[i])):
			if max_score < sum(pikominos_joueur[i][x]):
				max_score = sum(pikominos_joueur[i][x])
				gagnant = i

	print("Le gangnant est {} avec {} points".format(liste_joueur[gagnant-1], max_score))
	print("Fin du jeux")