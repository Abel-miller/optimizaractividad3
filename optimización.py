import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(1000)]
print(numeros_aleatorios)

maximo_numero = max(numeros_aleatorios)
suma_numeros = sum(numeros_aleatorios)

print(maximo_numero)
print(suma_numeros)
