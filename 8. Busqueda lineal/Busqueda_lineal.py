import random

def busqueda_lineal(lista, objetivo, i = 0):
    match = False

    for elemento in lista: #O(n)
        i += 1
        if elemento == objetivo:
            match == True
            break

    return(match, i)

if __name__ == '__main__':
    tamaño_de_lista = int(input('¿De qué tamaño sera la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]

    (encontrado, i) = busqueda_lineal(lista, objetivo)

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Número de iteraciones: {i}')