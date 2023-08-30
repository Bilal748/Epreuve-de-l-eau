def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n+1):
            fib_next = fib_prev + fib_curr
            fib_prev, fib_curr = fib_curr, fib_next
        return fib_curr

if __name__ == "__main__":
    n = int(input("Entrez un nombre n : "))
    result = fibonacci(n)
    if result == -1:
        print("Erreur : Paramètre négatif ou mauvais.")
    else:
        print(result)