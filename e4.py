#programa que calcula un promedio
numeros = [float(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
promedio = sum(numeros) / len(numeros)
print(f"El promedio es {promedio}")
