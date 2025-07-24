def saludar():
    print("Bienvenido al programa para realizar operaciones matematicas.")

def sumar(a, b):
    return a + b

def promedio(a, b):
    return a + b /2

def area (base, altura):
    return base * altura / 2

def es_par(numero):
    return numero % 2 == 0


while True:
    print("\n=== MENÚ DE OPERACIONES ===")
    print("1. Sumar dos números")
    print("2. Calcular el area de un triángulo")
    print("3. Verificar si un número es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n numeros de y mostrar el mayor y menor")
    print("6. Salir del programa")

    opcion = input("Elija una opción (1-6): ")

    match opcion:
        case "1":
