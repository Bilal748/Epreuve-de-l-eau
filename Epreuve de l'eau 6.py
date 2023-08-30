def recherche_chaine(chaine, recherche):
    return recherche in chaine

if __name__ == "__main__":
    try:
        chaine = input("Entrez une chaîne de caractères : ")
        recherche = input("Entrez la chaîne à rechercher : ")

        if recherche_chaine(chaine, recherche):
            print("true")
        else:
            print("false")
    except:
        print("error")