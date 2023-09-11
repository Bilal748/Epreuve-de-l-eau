def contains_only_digits(input_string):
    # Vérifier si tous les caractères de la chaîne sont des chiffres
    if input_string.isdigit():
        return True
    else:
        return False

user_input = input("Entrez une chaîne de caractères : ")

try:
    if contains_only_digits(user_input):
        print("true")
    else:
        print("false")
except:
    print("error")
