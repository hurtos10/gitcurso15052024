import math

# Función para verificar si un número es impar
def es_impar(num):
    return num % 2 != 0

# Función para obtener los primeros 3 números impares de los dígitos de un número
def primeros_impares(num):
    impares = []
    while num > 0 and len(impares) < 3:
        digito = num % 10
        if es_impar(digito):
            impares.append(digito)
        num //= 10
    return impares

# Entrada de los números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Suma de los números y elevación a la 1024 potencia
resultado = (num1 + num2) ** 1024

# División entre pi
resultado /= math.pi

# Resta de los primeros 3 números impares de los dígitos
impares_num1 = sum(primeros_impares(int(abs(num1))))
impares_num2 = sum(primeros_impares(int(abs(num2))))
resultado -= (impares_num1 + impares_num2)

print("El resultado final es:", resultado)
