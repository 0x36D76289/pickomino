import random

#Create a class that allows you to identify the players, their pikominos in their pockets, the dice they collect during their turns
class Joueur():
    def __init__(self, nom, pikominos, des, score):
        self.nom = nom
        self.pikominos = pikominos
        self.des = des
        self.score = score

def nombre_joueur():
    """
    définie le nombre de joueur de la partie
    """
    nombre_joueur = int(input("nombre de joueurs : "))
    if  2 <= nombre_joueur <= 7:
        return nombre_joueur
    return nombre_joueur()

def lancer_des(des):
    """
    renvoie les resultats des des non pris par le joueur
    """
    resultat = []
    for i in range(len(des)):
        resultat.append(des[random.randint(0, len(des)-1)])
    return resultat

def un_tour(joueur):
    """
    Execute the function throw_des(), ask the player the dice he wants to put in list_des,
    he can't take a number taken before he plays again until he decides to stop or there are no more dice, the player is obliged to take at least one "green" one
    """
    # while len(joueur.des) != 6:
    #     print(joueur.nom + " : " + str(joueur.des))
    #     print("Voulez vous lancer les dés ? oui/non")
    #     choix = input()
    #     if choix == "oui":
    #         resultat = lancer_des(des - joueur.des)
    #         print(resultat + "\n Quel nombre voulez vous garder non si vous voulez pas en prendre: ")
    #         choix =  input()
    #         if resultat = "non":
    #             return resultat
            

    #     else:
    #         break
    des = [1,2,3,4,5,"vert"]
    pioche = []
    point = 0
    while point < 21:
        lancer = lancer_des(des)
        print(lancer)
        reponse = input("que voulez vous prendre ? ")
        pioche.append(reponse)


if __name__ == "__main__":
    nombre_joueur = nombre_joueur() #demande le nombre de joueur

    pikominos = {21:1, 22:1, 23:1, 24:1,
                 25:2, 26:2, 27:2, 28:2,
                 29:3, 30:3, 31:3, 32:3,
                 34:4, 35:4, 36:4} #crée la liste de dominots possible au depart

    des = [1,2,3,4,5,"vert"] #crée la liste des possibiliter pour un dé

    first = int(input("quel joueur imite le mieux le cri du dindon ? (1, 2, 3 , ...) : ")) #demande au joueur 
    
    #
