def suma(a, b):
    return a + b


if __name__ == '__main__':
    print("ejecutando directamente del archivo 'sumar.py'")
    r1 = suma(2, 3)
    print(f"El resultado de la primer suma es {r1}")

    r2 = suma(r1, r1)
    print(f"El resultado de la segunda suma es {r2}")