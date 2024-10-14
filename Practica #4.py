l=[]
v=input("Ingresa valores a la lista: ")
l.extend(v.split(','))
print("Lista con valores:"+str(l))
n=input("Ingrese el numero a buscar: ")
o=l.count(n)
print(f"El numero {n} aparece {o} veces en esta lista")
print("Lista con los elementos duplicados eliminados:")
def eli(l):
    return list(set(l))
print(eli(l))
