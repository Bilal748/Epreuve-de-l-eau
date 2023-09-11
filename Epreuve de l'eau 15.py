def ascii_sort(arguments):
    try:
        sorted_arguments = sorted(arguments, key=lambda x: "".join(map(str, map(ord, x))))
        return sorted_arguments
    except Exception as e:
        return "error"

user_input = input("Entrez des éléments séparés par des espaces : ")
input_values = user_input.split()

if len(input_values) < 1:
    print("error")
else:
    sorted_arguments = ascii_sort(input_values)
    if "error" in sorted_arguments:
        print("error")
    else:
        print(" ".join(sorted_arguments))