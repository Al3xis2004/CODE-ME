print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comezar, ¿Cuál es tu nombre?: ")

matematicas = int(input((nombre + " ¿Cuál es tu claificación en matemáticas?: ")))
comunicación = int(input(nombre + " ¿Cuál es tu calificación en comunicación?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificación en quimica?: "))

promedio = (matematicas + quimica + comunicación) / 3
promedio = int(promedio)
if promedio >= 11:
                  print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
if promedio <= 10:
    print(nombre + '" desaprovaste" con un promedio de: ', promedio)

print("Fin.")






















                  
                  
                  


                  
                  
                  
