from itertools import permutations

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

# Calcular el peso total de una ruta
def calcular_peso_ruta(grafo, ruta):
    peso_total = 0
    for i in range(len(ruta) - 1):
        peso_total += obtener_distancia(grafo, ruta[i], ruta[i+1])
    return peso_total

# Ordenar rutas usando Bubble Sort
def bubble_sort_rutas(rutas, grafo):
    n = len(rutas)
    for i in range(n):
        for j in range(0, n-i-1):
            if calcular_peso_ruta(grafo, rutas[j]) > calcular_peso_ruta(grafo, rutas[j+1]):
                rutas[j], rutas[j+1] = rutas[j+1], rutas[j]
    return rutas

# Encontrar la ruta con menor peso entre dos ciudades
def encontrar_ruta_menor_peso(grafo, inicio, destino):
    rutas = generar_rutas(grafo, inicio, destino)
    rutas_ordenadas = bubble_sort_rutas(rutas, grafo)
    ruta_optima = rutas_ordenadas[0]
    peso_optimo = calcular_peso_ruta(grafo, ruta_optima)
    return ruta_optima, peso_optimo

# Ejemplo: Encontrar la ruta con menor peso entre 'Ciudad de México' y 'Monterrey'
ruta, peso = encontrar_ruta_menor_peso(grafo, 'Ciudad de México', 'Monterrey')
print(f"La ruta con menor peso es: {' -> '.join(ruta)} con un peso de {peso} km")
