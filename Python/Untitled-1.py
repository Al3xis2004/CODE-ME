# Función para sumar
def sumar(a, b):
    return a + b

# Función para restar
def restar(a, b):
    return a - b

# Función para multiplicar
def multiplicar(a, b):
    return a * b

# Función para dividir
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre 0"

# Función principal de la calculadora
def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una opción (1/2/3/4): ")
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif opcion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
