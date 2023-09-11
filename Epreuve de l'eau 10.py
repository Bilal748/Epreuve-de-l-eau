def print_range(min_value, max_value):
    if min_value >= max_value:
        return "error"

    for num in range(min_value, max_value):
        print(num, end=" ")

    print()  # Pour afficher une nouvelle ligne à la fin

user_input = input("Entrez deux nombres séparés par un espace : ")
input_values = user_input.split()

if len(input_values) != 2:
    print("error")
else:
    try:
        min_value = int(input_values[0])
        max_value = int(input_values[1])
        result = print_range(min_value, max_value)
        if result == "error":
            print("error")
    except ValueError:
        print("error")




