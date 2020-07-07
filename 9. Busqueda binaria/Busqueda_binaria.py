import random

def busqueda_binaria(lista, comienzo, final, objetivo, i = 0):
    i += 1
    if comienzo > final:
        return (False, i)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, i)
    elif lista [medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, i = i)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, i = i)



if __name__ == '__main__':
    tamaño_de_lista = int(input('¿De qué tamaño es la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamaño_de_lista)])
    
    (encontrado, i) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {i}')