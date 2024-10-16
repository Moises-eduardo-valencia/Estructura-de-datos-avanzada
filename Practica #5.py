h=[]
while True:
    print("HISTORIAL DE BUSQUEDA")
    p=input("¿Deseas agregar una visita?: ")
    if p=='si':
        b=input("Ingresa la URL y la fecha de la búsqueda: ")
        h.append(b)
        print("Historial de visitas:")
        print(h)
    elif p=='no':
        e=input("¿Deseas eliminar una visita?: ")
        if e=='si':
            h.pop()
            print("El historial fue modificado:")
            print(h)
        elif e=='no':
            print("El historial no fue modificado:")