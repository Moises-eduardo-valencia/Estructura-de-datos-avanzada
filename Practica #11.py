alumnos={
    "01":{
    "Nombre":"Moisés Eduardo Valencia Hernández",
    "Edad":20,
    "Carrera":"Ingenieria en Software",
    "Grado":"4to cuatrimestre"
},
    "02":{
    "Nombre":"Luis Gomez Sanchez",
    "Edad":18,
    "Carrera":"Ingenieria en Logistica y Transporte",
    "Grado":"2do cuatrimestre"
},
    "03":{
    "Nombre":"Luis Fernando Soto",
    "Edad":22,
    "Carrera":"Ingenieria en mecatronica",
    "Grado":"6to cuatrimestre"
},
    "04":{
    "Nombre":"Isabel Lopez Villa",
    "Edad":19,
    "Carrera":"Administracion de empresas",
    "Grado":"8vo cuatrimestre"
}
}
a=input("Ingresa la matricula del alumno que deseas visualizar: ")
if a in alumnos:
    alumno=alumnos[a]
    print(f"Nombre: {alumno['Nombre']}")
    print(f"Edad: {alumno['Edad']}")
    print(f"Carrera: {alumno['Carrera']}")
    print(f"Grado: {alumno['Grado']}")
else:
    print("No se encontró un alumno con esa matrícula.")