def es_oreja(v, v_prev, v_sig, vertices):
    # Verifica si el triángulo formado por v, v_prev y v_sig es una oreja
    for v_i in vertices:
        if (v_i == v or v_i == v_prev or v_i == v_sig):
            continue
        if (punto_dentro_triángulo(v_i, v, v_prev, v_sig)):
            return False
    return True

def punto_dentro_triángulo(p, v1, v2, v3):
    # Verifica si el punto p está dentro del triángulo formado por v1, v2 y v3
    area = abs((v1[0]*(v2[1]-v3[1]) + v2[0]*(v3[1]-v1[1]) + v3[0]*(v1[1]-v2[1]))/2.0)
    area1 = abs((p[0]*(v2[1]-v3[1]) + v2[0]*(v3[1]-p[1]) + v3[0]*(p[1]-v2[1]))/2.0)
    area2 = abs((v1[0]*(p[1]-v3[1]) + p[0]*(v3[1]-v1[1]) + v3[0]*(v1[1]-p[1]))/2.0)
    area3 = abs((v1[0]*(v2[1]-p[1]) + v2[0]*(p[1]-v1[1]) + p[0]*(v1[1]-v2[1]))/2.0)
    return area == area1 + area2 + area3

def triangulación_ear_clipping(vertices):
    triángulos = []
    vertices = vertices[:]
    while len(vertices) > 3:
        for i in range(len(vertices)):
            v_prev = vertices[(i-1)%len(vertices)]
            v = vertices[i]
            v_sig = vertices[(i+1)%len(vertices)]
            if es_oreja(v, v_prev, v_sig, vertices):
                triángulos.append((v_prev, v, v_sig))
                vertices.remove(v)
                break
    triángulos.append((vertices[0], vertices[1], vertices[2]))
    return triángulos
