def a_des_chiffres_repetes(nombre):
    nombre_str = str(nombre)
    return len(set(nombre_str)) != len(nombre_str)

def generer_combinaisons():
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                nombre = i * 100 + j * 10 + k
                if not a_des_chiffres_repetes(nombre):
                    print(f"{i}{j}{k}", end=", ")

generer_combinaisons()