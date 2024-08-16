from collections import deque

# Implementación de búsqueda en anchura para encontrar la ruta más corta
def bfs(graph, start, end):
    # Una cola para los nodos por explorar
    queue = deque([(start, [start])])
    # Un conjunto para los nodos ya visitados
    visited = set()

    while queue:
        # Extraer un nodo y su ruta de la cola
        node, path = queue.popleft()

        # Si ya hemos visitado este nodo, continuamos con el siguiente
        if node in visited:
            continue

        # Marcar el nodo como visitado
        visited.add(node)

        # Si hemos llegado al nodo de destino, retornar la ruta
        if node == end:
            return path

        # Añadir los vecinos del nodo a la cola si no han sido visitados
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # Si no se encontró una ruta, retornar None
    return None

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
        if left[i] < right[j]:
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
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
graph = {
    1: [2, 3, 4, 5],
    2: [],
    3: [6],
    4: [3, 8],
    5: [],
    6: [7],
    7: [2],
    8: [6],
    9: [5, 8],
}

start = 1
end = 7

# Búsqueda en anchura para encontrar la ruta más corta
shortest_path = bfs(graph, start, end)
print("Ruta más corta:", shortest_path)

# Ordenamiento de rutas con mergesort
sorted_path = mergesort(shortest_path)
print("Ruta ordenada con mergesort:", sorted_path)

# Ordenamiento de rutas con bubblesort
sorted_path = bubblesort(shortest_path)
print("Ruta ordenada con bubblesort:", sorted_path)


                

