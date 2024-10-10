print("LISTA DE COMPRAS")
a=["Manzana","Pan", "Leche","Peras","Naranjas"]
print(a)
b=input(print("¿Deseas eliminar el ultimo elemento de la lista?: "))
if b=="si":
    a.pop()
    print("La lista fue modificada")
    print(a)
else:
    print("La lista no fue modificada")