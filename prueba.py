from itertools import permutations
from collections import deque

# Grafo ponderado con las 10 ciudades de México
grafo = {
    'Ciudad de México': [('Guadalajara', 550), ('Puebla', 130), ('Querétaro', 210)],
    'Guadalajara': [('Ciudad de México', 550), ('Monterrey', 700), ('León', 220)],
    'Monterrey': [('Guadalajara', 700), ('Tijuana', 1420)],
    'Puebla': [('Ciudad de México', 130), ('Cancún', 1520)],
    'Tijuana': [('Monterrey', 1420), ('Chihuahua', 1130)],
    'León': [('Guadalajara', 220), ('Querétaro', 180)],
    'Querétaro': [('Ciudad de México', 210), ('León', 180)],
    'Cancún': [('Puebla', 1520), ('Mérida', 310)],
    'Mérida': [('Cancún', 310)],
    'Chihuahua': [('Tijuana', 1130)]
}

# Función para obtener la distancia entre dos ciudades conectadas
def obtener_distancia(grafo, ciudad1, ciudad2):
    for vecino, distancia in grafo[ciudad1]:
        if vecino == ciudad2:
            return distancia
    return float('inf')  # Retorna infinito si no hay conexión directa

# Generar todas las rutas posibles
def generar_rutas(grafo, inicio, destino):
    ciudades = list(grafo.keys())
    rutas = []
    for permutacion in permutations(ciudades):
        if permutacion[0] == inicio and permutacion[-1] == destino:
            rutas.append(permutacion)
    return rutas

# Calcular la longitud (distancia) total de una ruta
def calcular_distancia_ruta(grafo, ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += obtener_distancia(grafo, ruta[i], ruta[i+1])
    return distancia_total

# Implementación de ordenamiento mergesort
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
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Implementación de ordenamiento bubblesort
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Encontrar la ruta con menor peso usando ordenamiento
def encontrar_ruta_menor_peso(grafo, inicio, destino, metodo='mergesort'):
    rutas = generar_rutas(grafo, inicio, destino)
    rutas_con_distancia = [(ruta, calcular_distancia_ruta(grafo, ruta)) for ruta in rutas]
    
    if metodo == 'mergesort':
        rutas_ordenadas = mergesort(rutas_con_distancia)
    elif metodo == 'bubblesort':
        rutas_ordenadas = bubblesort(rutas_con_distancia)
    else:
        raise ValueError("Método de ordenamiento no reconocido. Usa 'mergesort' o 'bubblesort'.")

    ruta_optima = rutas_ordenadas[0][0]
    distancia_optima = rutas_ordenadas[0][1]
    return ruta_optima, distancia_optima

# Ejemplo: Encontrar la ruta con menor peso entre 'Ciudad de México' y 'Monterrey'
ruta, distancia = encontrar_ruta_menor_peso(grafo, 'Ciudad de México', 'Monterrey', metodo='mergesort')
print(f"Ruta con menor peso usando Mergesort: {' -> '.join(ruta)} con una distancia de {distancia} km")

ruta, distancia = encontrar_ruta_menor_peso(grafo, 'Ciudad de México', 'Monterrey', metodo='bubblesort')
print(f"Ruta con menor peso usando Bubblesort: {' -> '.join(ruta)} con una distancia de {distancia} km")
