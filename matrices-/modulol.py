
def gauss_2x2(matrix):
    """
    Resuelve un sistema de ecuaciones 2x2 usando el método de Gauss.
    """
    # Extrae los coeficientes y constantes
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    
    # Calcula el determinante
    det = a * e - b * d
    
    if det == 0:
        return "El sistema no tiene solución única."
    
    # Aplica el método de Cramer
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    
    return f"x = {x}, y = {y}"

def gauss_3x3(matrix):
    """
    Resuelve un sistema de ecuaciones 3x3 usando el método de Gauss.
    """
    # Extrae los coeficientes y constantes
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]
    e, f, g, h = matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3]
    i, j, k, l = matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3]
    
    # Eliminación de Gauss
    # Etapa 1: Eliminar la variable x de las ecuaciones 2 y 3
    factor1 = e / a
    for col in range(3):
        matrix[1][col] -= factor1 * matrix[0][col]
    matrix[1][3] -= factor1 * d
    
    factor2 = i / a
    for col in range(3):
        matrix[2][col] -= factor2 * matrix[0][col]
    matrix[2][3] -= factor2 * d
    
    # Etapa 2: Eliminar la variable y de la ecuación 3
    factor3 = j / f
    for col in range(3):
        matrix[2][col] -= factor3 * matrix[1][col]
    matrix[2][3] -= factor3 * h
    
    # Sustitución regresiva
    k_val = matrix[2][3] / matrix[2][2]
    j_val = (matrix[1][3] - matrix[1][2] * k_val) / matrix[1][1]
    i_val = (matrix[0][3] - matrix[0][2] * k_val - matrix[0][1] * j_val) / matrix[0][0]
    
    return f"x = {i_val}, y = {j_val}, z = {k_val}"

# Ejemplo de uso para 2x2
print("Sistema 2x2:")
matrix_2x2 = [
    [3, 1, 6],
    [1, 2, 5]
]
print("Matriz aumentada:")
for row in matrix_2x2:
    print(row)
print("\nSolución:")
print(gauss_2x2(matrix_2x2))

# Ejemplo de uso para 3x3
print("\n\nSistema 3x3:")
matrix_3x3 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -6]
]
print("Matriz aumentada:")
for row in matrix_3x3:
    print(row)
print("\nSolución:")
print(gauss_3x3(matrix_3x3))
def gauss_2x2(matrix):
    """
    Resuelve un sistema de ecuaciones 2x2 usando el método de Gauss.
    """
    # Extrae los coeficientes y constantes
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    
    # Calcula el determinante
    det = a * e - b * d
    
    if det == 0:
        return "El sistema no tiene solución única."
    
    # Aplica el método de Cramer
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    
    return f"x = {x}, y = {y}"

def gauss_3x3(matrix):
    """
    Resuelve un sistema de ecuaciones 3x3 usando el método de Gauss.
    """
    # Extrae los coeficientes y constantes
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]
    e, f, g, h = matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3]
    i, j, k, l = matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3]
    
    # Eliminación de Gauss
    # Etapa 1: Eliminar la variable x de las ecuaciones 2 y 3
    factor1 = e / a
    for col in range(3):
        matrix[1][col] -= factor1 * matrix[0][col]
    matrix[1][3] -= factor1 * d
    
    factor2 = i / a
    for col in range(3):
        matrix[2][col] -= factor2 * matrix[0][col]
    matrix[2][3] -= factor2 * d
    
    # Etapa 2: Eliminar la variable y de la ecuación 3
    factor3 = j / f
    for col in range(3):
        matrix[2][col] -= factor3 * matrix[1][col]
    matrix[2][3] -= factor3 * h
    
    # Sustitución regresiva
    k_val = matrix[2][3] / matrix[2][2]
    j_val = (matrix[1][3] - matrix[1][2] * k_val) / matrix[1][1]
    i_val = (matrix[0][3] - matrix[0][2] * k_val - matrix[0][1] * j_val) / matrix[0][0]
    
    return f"x = {i_val}, y = {j_val}, z = {k_val}"

# Ejemplo de uso para 2x2
print("Sistema 2x2:")
matrix_2x2 = [
    [3, 2, 7],
    [1, 4, 9]
]
print("Matriz aumentada:")
for row in matrix_2x2:
    print(row)
print("\nSolución:")
print(gauss_2x2(matrix_2x2))

# Ejemplo de uso para 3x3
print("\n\nSistema 3x3:")
matrix_3x3 = [
    [2, 3, 4, 10],
    [1, 2, 3, 8],
    [3, 1, 2, 7]
]
