def solve_2x2(matrix):
    """Resuelve un sistema de ecuaciones 2x2 usando el método de Gauss."""
    # Coefficients and constants
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    
    # Determinant
    det = a * e - b * d
    
    if det == 0:
        return "El sistema no tiene solución única."
    
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    
    return f"x = {x}, y = {y}"

def solve_3x3(matrix):
    """Resuelve un sistema de ecuaciones 3x3 usando el método de Gauss."""
    # Coefficients and constants
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

print("Por favor, ingresa los valores de la matriz aumentada. El formato debe ser:")
print("Matriz 2x2:")
print("a b c")
print("d e f")
print("\nMatriz 3x3:")
print("a b c d")
print("e f g h")
print("i j k l")

size = int(input("Ingrese el tamaño de la matriz (2 o 3): "))
if size == 2:
    matrix = []
    print("Ingrese las filas de la matriz 2x2:")
    for _ in range(2):
        row = list(map(float, input().split()))
        matrix.append(row)
elif size == 3:
    matrix = []
    print("Ingrese las filas de la matriz 3x3:")
    for _ in range(3):
        row = list(map(float, input().split()))
        matrix.append(row)

if size == 2:
    solution = solve_2x2(matrix)
else:
    solution = solve_3x3(matrix)

print("\nSolución:")
print(solution)
