def gauss_2x2(matrix):
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    det = a * e - b * d

    if det == 0:
        return "El sistema no tiene solución única."

    x = (c * e - b * f) / det
    y = (a * f - c * d) / det

    return f"x = {x}, y = {y}"


def gauss_3x3(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]
    e, f, g, h = matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3]
    i, j, k, l = matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3]

    factor1 = e / a
    for col in range(3):
        matrix[1][col] -= factor1 * matrix[0][col]
    matrix[1][3] -= factor1 * d

    factor2 = i / a
    for col in range(3):
        matrix[2][col] -= factor2 * matrix[0][col]
    matrix[2][3] -= factor2 * d

    factor3 = j / f
    for col in range(3):
        matrix[2][col] -= factor3 * matrix[1][col]
    matrix[2][3] -= factor3 * h

    k_val = matrix[2][3] / matrix[2][2]
    j_val = (matrix[1][3] - matrix[1][2] * k_val) / matrix[1][1]
    i_val = (matrix[0][3] - matrix[0][2] * k_val - matrix[0][1] * j_val) / matrix[0][0]

    return f"x = {i_val}, y = {j_val}, z = {k_val}"


# Datos de prueba predefinidos (por restricción de entorno)
pruebas = [
    {
        "opcion": "1",
        "matrix": [
            [2, 1, 5],
            [4, -6, -2]
        ]
    },
    {
        "opcion": "2",
        "matrix": [
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3]
        ]
    }
]

for prueba in pruebas:
    opcion = prueba["opcion"]
    matrix = prueba["matrix"]

    print("\n==============================")
    print(f"Resolviendo sistema {opcion}x{opcion}:")
    for row in matrix:
        print(row)

    print("\nSolución:")

    if opcion == "1":
        print(gauss_2x2(matrix))
    elif opcion == "2":
        print(gauss_3x3(matrix))
    else:
        print("Opción no válida.")
    print("==============================\n")
