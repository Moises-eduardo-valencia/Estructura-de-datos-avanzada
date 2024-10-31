"""
diccionario={
    "Key":"Value",
    "name":"Moises",
    "pais":"Mexico"
}
diccionario["pais"]="Us"
print(diccionario["pais"])
"""
alumno={
    "matricula":input("Ingrese la matrícula: "),
    "nombre":input("Ingrese el nombre: "),
    "escuela":input("Ingrese la escuela: "),
    "grado":input("Ingrese el grado: "),
    "Carrera":input("Ingrese tu carrera: ")
}

print("DATOS PERSONALES")
print("Hola,",alumno["nombre"])
print("Matricula:",alumno["matricula"])
print("Escuela:",alumno["escuela"])
print("Grado:",alumno["grado"])
print("Carrera:",alumno["Carrera"])