def distancia(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def orientacion(p1, p2, p3):
    valor = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if valor == 0:
        return 0  # Colineales
    elif valor > 0:
        return 1  # Sentido antihorario
    else:
        return 2  # Sentido horario

def convex_hull(puntos):
    n = len(puntos)
    if n < 3:
        return puntos

    hull = []
    l = 0
    for i in range(1, n):
        if puntos[i][0] < puntos[l][0]:
            l = i

    p = l
    q = 0
    while True:
        hull.append(puntos[p])
        q = (p + 1) % n

        for i in range(n):
            if orientacion(puntos[p], puntos[i], puntos[q]) == 2:
                q = i

        p = q
        if p == l:
            break

    return hull

"""Ejemplo de uso"""
print("ALGORITMO DE GRAHAM ") 
puntos = [(1, 2), (3, 4), (2, 1), (4, 3)]
print("DATOS ENTRADA : ", puntos) 
hull = convex_hull(puntos)
print("DATOS SALIDA :  ",hull)