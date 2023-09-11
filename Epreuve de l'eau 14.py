def my_select_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    user_input = input("Entrez une liste de nombres séparés par des espaces : ")
    input_values = user_input.split()

    try:
        numbers = [int(val) for val in input_values]
        sorted_numbers = my_select_sort(numbers)
        print(" ".join(map(str, sorted_numbers)))
    except ValueError:
        print("error")