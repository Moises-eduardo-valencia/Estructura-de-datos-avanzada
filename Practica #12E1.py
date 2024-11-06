#Sistema de registro de estudiantes inscritos
p=set(input("Ingresa los alumnos inscritos en Programación: ").split(","))
r=set(input("Ingresa los alumnos inscritos en Redes: ").split(","))
print("LISTA DE ESTUDIANTES INSCRITOS EN AMBOS CURSOS")
print(p&r)
print("LISTA DE ESTUDIANTES INSCRITOS EN PROGRAMACION")
print(p)
print("LISTA DE ESTUDIANTES INSCRITOS EN REDES")
print(r)