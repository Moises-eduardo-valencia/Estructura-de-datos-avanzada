a=[]
while True:
    print("MENU \n1. Ver\n2. Agregar\n3. Modificar\n4. Eliminar\n5. Salir")
    o=input("Opción: ")
    if o=='1':
        print(a)
    elif o=='2':
        a.append(input("Elemento: "))
    elif o=='3':
        i=int(input("Índice: "))
        a[i]=input("Nuevo: ")
    elif o=='4':
        i=int(input("Índice: "))
        a.pop(i)
    elif o=='5':
        break
    else:
        print("Opción no válida")
