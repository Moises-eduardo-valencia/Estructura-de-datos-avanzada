class stack:
    def __init__(self):
        self.pila = []
    def esta_vacia(self):
        return len(self.pila) == 0
    #metodo push
    def agregar_elemento(self,elemento):
        self.pila.append(elemento)
    #metodo pop
    def eliminar_elemento(self,elemento):
       self.pila.remove(elemento)

if __name__ == "__main__":
  stack=stack()
if stack.esta_vacia():
    print("La pila esta vacia")
else:
    print("La pila no esta vacia")
