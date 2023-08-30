def est_nombre_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def premier_superieur(n):
    if n <= 0:
        return -1
    i = n + 1
    while True:
        if est_nombre_premier(i):
            return i
        i += 1

if __name__ == "__main__":
    n = int(input("Entrez un nombre : "))
    result = premier_superieur(n)
    if result == -1:
        print("Erreur : Paramètre négatif ou mauvais.")
    else:
        print(result)
