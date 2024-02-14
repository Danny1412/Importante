Cursos_min = 2.5
Cursos_max =  7
Cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudo

crudo_promedio = 5
crudo_dalto = 3.5

# diferencia de tiempo duradero

diferencia_min = 100 - dalto_curso / Cursos_min * 100
diferencia_max = 100 - dalto_curso * 1000 // Cursos_max / 10
diferencia_promedio = 100 - dalto_curso / Cursos_promedio * 100

# Calculamos el porcentaje de tiempo vacio o basura

tiempo_vacio_promedio = 100 - Cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

# mostrando la diferencia de duracion
print(f"el curso de dalto dura un {diferencia_min} menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_max} menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_promedio} menos que el mas promedio")

#tiempo vacio promedio

print(f"Un curso promedio elimina un {tiempo_vacio_promedio} % de tiempo vacio")
print(f"Un curso de dalto elimina un {tiempo_vacio_dalto} % de tiempo vacio")

# mostramos la diferencia de los cursos si duran 10 h
print(f"ver 10 horas de este curso equivale a ver {Cursos_promedio*100 //dalto_curso/10} horas de este curso")
print(f"ver 10 horas de otros curso equivale a ver {dalto_curso*100 //Cursos_promedio/10} horas de este curso")
