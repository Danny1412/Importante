# lisas con nombres y apellidos
nombres = ["lucas","Matias","Pedro"]
apellidos = ["Dalto","Loco","Sonso"]

# registar la informacion en un txt de manear optima

with open("Problemas_archivos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n") for n,a in zip(nombres,apellidos)]