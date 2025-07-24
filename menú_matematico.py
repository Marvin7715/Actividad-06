def saludar():
    print("Bienvenido al programa para realizar operaciones matematicas.")

def area_triangulo (base, altura):
    return (base * altura) / 2

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
    print("1. Suma, promedio, positivos y negativos de n números")
    print("2. Calcular el area de un triángulo")
    print("3. Verificar si un número es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Mayor y menor de n números")
    print("6. Salir del programa")

    opcion = input("Elija una opción (1-6): ")

    match opcion:
        case "1":
            n = int(input("¿Cuántos números desea ingresar?: "))
            numeros = pedir_numeros(n)
            suma, promedio, pos, neg = analizar_numeros(numeros)
            print(f"Suma: {suma}, Promedio: {promedio}, Positivos: {pos}, Negativos: {neg}")

        case "2":
            base = float(input("Base del triángulo: "))
            altura = float(input("Altura del triángulo: "))
            print(f"Área: {area_triangulo(base, altura)}")

        case "3":
            numero = int(input("Ingrese un número: "))
            print("El número es par." if es_par(numero) else "El número es impar.")

        case "4":
            n = int(input("¿Cuántas calificaciones ingresará?: "))
            calificaciones = pedir_numeros(n, "Ingrese una calificación: ")
            print(f"Promedio: {calcular_promedio(calificaciones)}")

        case "5":
            n = int(input("¿Cuántos números desea ingresar?: "))
            numeros = pedir_numeros(n)
            mayor, menor = encontrar_mayor_menor(numeros)
            print(f"Mayor: {mayor}, Menor: {menor}")

        case "6":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida. Intente nuevamente.")