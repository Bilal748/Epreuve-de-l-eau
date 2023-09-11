def capitalize_words(input_string):
    words = input_string.split()  # Séparer la chaîne en mots

    # Vérifier si la chaîne contient au moins un mot avec des lettres
    if not any(word.isalpha() for word in words):
        print("error")
        return

    capitalized_words = []
    for word in words:
        if word.isalpha():
            capitalized_word = word[0].upper() + word[1:].lower()
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)

    # Joindre les mots en une chaîne et afficher le résultat
    result = ' '.join(capitalized_words)
    print(result)

user_input = input("Entrez une chaîne de caractères : ")
capitalize_words(user_input)
