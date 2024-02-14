def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado
    

print("chanchito")
l = largo("hola mundo")
print(l)

#Como se pudo observar el depurador de texto sirve mayormente para esos casos en los cuales el error no se encuentra y el vscode no lo muestra
# En el caso de este ejemplo el return se encontraba identado al ciclo for
# sabiendo que el return finaliza cualquier ejecucion cuando asigna el valor a la variable en cuestion
# es decir retornaba valor 1 a la variable resultado cuando esta apenas se ejecuaba todo por estar dentro del ciclo el cual esta dentrod e una funcion
# Por eso depuramos el texto para saber cuantos caracteres tenia el sring pero no daba ya que return finalizaba toda ejecucion al tener directametne un valor que asignar
# y no al finalizar el ciclo para retornar los valoresa