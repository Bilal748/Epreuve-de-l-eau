def my_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    user_input = input("Entrez une liste de nombres séparés par des espaces : ")
    input_values = user_input.split()

    try:
        numbers = [int(val) for val in input_values]
        sorted_numbers = my_bubble_sort(numbers)
        print(" ".join(map(str, sorted_numbers)))
    except ValueError:
        print("error")