from collections import deque

grafo = {
    'Oaxaca': [('Guadalajara', 550), ('Puebla', 130), ('Queretaro', 210)],
    'Guadalajara': [('Oaxaca', 550), ('Monterrey', 700), ('Leon', 220)],
    'Monterrey': [('Guadalajara', 700), ('Tijuana', 1420)],
    'Puebla': [('Oaxaca', 130), ('Cancun', 1520)],
    'Tijuana': [('Monterrey', 1420), ('Chihuahua', 1130)],
    'Leon': [('Guadalajara', 220), ('Queretaro', 180)],
    'Queretaro': [('Oaxaca', 210), ('Leon', 180)],
    'Cancun': [('Puebla', 1520), ('Merida', 310)],
    'Merida': [('Cancun', 310)],
    'Chihuahua': [('Tijuana', 1130)]
}

# encontrar distancia (si no como se cuanto tarda)
def obtener_distancia(grafo, ciudad1, ciudad2):
    for vecino, distancia in grafo[ciudad1]:
        if vecino == ciudad2:
            return distancia
    return float('inf')  # Retorna el infinito si no encuentra nada como dicta los grafos ponderados :D

# bussqueda en anchura para encontrar la ruta mas corta
def bfs(grafo, inicio, destino):
    queue = deque([(inicio, [inicio])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == destino:
            return path

        for neighbor, _ in grafo[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

def calcular_distancia_ruta(grafo, ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += obtener_distancia(grafo, ruta[i], ruta[i+1])
    return distancia_total

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def mostrar_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"--{key}")

# aseguro que todo funcione con un try, si no, cacha el error
while True:
    try:
        print("Ciudades disponibles:")
        mostrar_diccionario(grafo)
        print("")
        inicio = input("Ciudad de inicio: ").title()#uso tittle para hacer que la primera sea mayuscula y las demas minusculas
        destino = input("Ciudad de destino: ").title()

        ruta_mas_corta = bfs(grafo, inicio, destino)
        if ruta_mas_corta:
            distancia = calcular_distancia_ruta(grafo, ruta_mas_corta)
            print(f"Ruta más corta: {' -> '.join(ruta_mas_corta)}")
            print(f"Longitud de la ruta: {distancia} km")
        else:
            print("No se encontró una ruta.")

        # mergesort
        sorted_ruta = mergesort(ruta_mas_corta)
        print("Ruta ordenada con mergesort:", sorted_ruta)

        # bubblesort
        sorted_ruta = bubblesort(ruta_mas_corta)
        print("Ruta ordenada con bubblesort:", sorted_ruta)

        break

    except KeyError:
        print("Alguna de las ciudades no es valida")
    


# Búsqueda en anchura para encontrar la ruta más corta


