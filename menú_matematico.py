def saludar():
    print("Bienvenido al programa para realizar operaciones matematicas.")

def area_triangulo (base, altura):
    return base * altura / 2

def es_par(numero):
    return numero % 2 == 0

def pedir_numeros(n, mensaje="Ingrese un número: "):
    return [float(input(mensaje)) for _ in range(n)]

def analizar_numeros(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros) if numeros else 0
    positivos = sum(1 for num in numeros if num > 0)
    negativos = sum(1 for num in numeros if num < 0)
    return suma, promedio, positivos, negativos

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

def encontrar_mayor_menor(numeros):
    return max(numeros), min(numeros) if numeros else (None, None)

while True:
    print("\n=== MENÚ DE OPERACIONES ===")
    print("1. Sumar dos números")
    print("2. Calcular el area de un triángulo")
    print("3. Verificar si un número es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n numeros de y mostrar el mayor y menor")
    print("6. Salir del programa")

    opcion = input("Elija una opción (1-6): ")