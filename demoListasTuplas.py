lista_de_alumnos = list()
def initAlumnos():
  return [
    ("Orlando Betancourth", "obetancourthunicah@gmail.com", "50400000000", "Comentario 1"),
    ("Josue Betancourth", "jbetancourthunicah@gmail.com", "50400000000", "Comentario 2"),
    ("Adriana Betancourth", "abetancourthunicah@gmail.com", "50400000000", "Comentario 3"),
  ]
lista_de_alumnos = initAlumnos()
for alumno in lista_de_alumnos:
  print(alumno, sep=", ")
