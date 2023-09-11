def find_element_index(arr, target):
    try:
        index = arr.index(target)
        return index
    except ValueError:
        return -1

user_input = input("Entrez des éléments séparés par des espaces, suivi de l'élément recherché : ")
input_values = user_input.split()

if len(input_values) < 2:
    print("error")
else:
    target = input_values[-1]
    arr = input_values[:-1]

    result = find_element_index(arr, target)
    print(result)
