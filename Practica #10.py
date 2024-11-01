di = {}
rango = int(input("Ingresa el rango de datos que deseas para el diccionario: "))

for i in range(rango):
    di[f"Dato {i}"] = f"valor_{i}"

def mostrar_diccionario():
    print("\nContenido actual del diccionario:")
    for clave, valor in di.items():
        print(f"{clave}: {valor}")

def modificar_elemento():
    clave = input("Ingresa la clave del elemento que deseas modificar: ")
    if clave in di:
        nuevo_valor = input("Ingresa el nuevo valor: ")
        di[clave] = nuevo_valor
        print("Elemento modificado.")
    else:
        print("La clave no existe en el diccionario.")

def eliminar_elemento():
    clave = input("Ingresa la clave del elemento que deseas eliminar: ")
    if clave in di:
        del di[clave]
        print("Elemento eliminado.")
    else:
        print("La clave no existe en el diccionario.")

while True:
    print("\nMenú:")
    print("1. Mostrar diccionario")
    print("2. Modificar elemento")
    print("3. Eliminar elemento")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_diccionario()
    elif opcion == "2":
        modificar_elemento()
    elif opcion == "3":
        eliminar_elemento()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
