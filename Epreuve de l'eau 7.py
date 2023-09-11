def alternate_case(input_string):
    if not any(char.isalpha() for char in input_string):
        print("error")
        return

    result = []
    upper = True

    for char in input_string:
        if char.isalpha():
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper
        else:
            result.append(char)

    print(''.join(result))

user_input = input("Entrez une chaîne de caractères : ")
alternate_case(user_input)