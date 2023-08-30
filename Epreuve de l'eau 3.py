def afficher_arguments_envers(arguments):
    if not arguments:
        print("Erreur : Aucun argument fourni.")
        return

    for argument in arguments:
        mots = argument.split()
        mots_inverse = mots[::-1]
        argument_inverse = " ".join(mots_inverse)
        print(argument_inverse)

if __name__ == "__main__":
    arguments = input("Entrez des arguments séparés par des espaces : ").split(" | ")
    afficher_arguments_envers(arguments)