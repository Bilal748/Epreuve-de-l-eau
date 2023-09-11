def min_absolute_difference(numbers):
    if len(numbers) < 2:
        return "error"
    
    numbers.sort()  # Tri des nombres dans l'ordre croissant

    min_diff = abs(numbers[1] - numbers[0])

    for i in range(2, len(numbers)):
        diff = abs(numbers[i] - numbers[i-1])
        if diff < min_diff:
            min_diff = diff

    return min_diff

user_input = input("Entrez des nombres séparés par des espaces : ")
input_values = user_input.split()

try:
    numbers = [int(val) for val in input_values]
    result = min_absolute_difference(numbers)
    if result == "error":
        print("error")
    else:
        print(result)
except ValueError:
    print("error")
