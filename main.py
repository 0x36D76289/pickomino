import random
from collections import Counter

#Create a class that allows you to identify the players, their pikominos in their pockets, the dice they collect during their turns
# class Joueur():
#     def __init__(self, nom, pikominos, des, score):
#         self.nom = nom
#         self.pikominos = pikominos
#         self.des = des
#         self.score = score

def nombre_joueur():
    """
    définie le nombre de joueur de la partie
    """
    nombre_joueur = int(input("nombre de joueurs : "))
    if  2 <= nombre_joueur <= 7:
        return nombre_joueur
    return nombre_joueur()

def lancer_le_des(des):
    """
    renvoie les resultats des des non pris par le joueur
    """
    return random.choice(des)

def resultat_des_des(des, nombre) -> list:
    temp_des = []
    #pioche une valeur aléatoire dans chaque liste dans la liste des
    for i in des:
        temp_des.append(L[i][random.randint(5)])
    return temp_des

def un_tour(joueur):
    """
    """
    des = [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6],
           [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6],
           [1,2,3,4,5,6], [1,2,3,4,5,6]] #liste des des et de leurs posibiliter
    
    while True:
        tour = 0
        des_lancer = resultat_des_des(des, len(des))
        dict_des = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}#Create a dictionary of the values of the des and their iteration numbers
        for i in des_lancer:    #met les valeurs des des dans le dictionnaire
            dict_des[i-1] += 1
        
        prendre = int(input(f"voici votre pioche {des_lancer} quel des voulez vous prendre ? {dict_des} / non : ")) #demande a l'utilisateur de choisir un/des des
        if prendre == "non" and tour != 0:
            break
        elif prendre == "non" and tour == 0:
            print("vous n'avez pas de des")
            continue
        else:
            for i in range(dict_des[prendre]):
                des.remove([i-1])
            joueur.des.append(des_lancer[prendre-1])
            tour += 1

if __name__ == "__main__":
    nombre_joueur = nombre_joueur() #demande le nombre de joueur
    joueur1 = 0
    joueur2 = 0
    joueur3 = 0
    joueur4 = 0
    

    pikominos = {21:1, 22:1, 23:1, 24:1,
                 25:2, 26:2, 27:2, 28:2,
                 29:3, 30:3, 31:3, 32:3,
                 34:4, 35:4, 36:4} #crée la liste de dominots possible au depart

    des = [1,2,3,4,5,6] #crée la liste des possibiliter pour un dé

    first = int(input("quel joueur imite le mieux le cri du dindon ? (1, 2, 3 , ...) : ")) #demande au joueur 
    
    #
