

#Definir la clase principal

class registro:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.teléfono = telefono

#Crear funciones para cada operación CRUD:
        
#a). Crear un Registro:
def crear_registro(nombre, edad, telefono): 
    with open('registros.txt', 'a') as f:
        f.write(f"{nombre}, {edad}, {telefono}\n")

#b). Leer Registros:
def leer_registros():
    whit open('registros.txt', 'r') as f:
        registros = f.readlines()
        for registro in registros:
        print(registro.strip())
    
#c). Actualizar un Registro:
def actualizar_registro (nombre, nueva_edad, nuevo_telefono):
    registros_actualizados = []
    whit open('registros.txt', 'r') as f:
        registros = f.readlines()
        for registro in registros:
        nombre_actual, edad_actual, telefono_actual = registro.strip().split(',')
        if nombre_actual == nombre:
            registros_actualizados.append(f"{nombre},{nueva_edad},{nuevo_telefono}\n")
        else:
            registros_actualizados.append(registro)
    whit open('registros.txt', 'w') as f:
        f.writelines(registros_actualizados)
    
#d). Eliminar un Registro:
def eliminar_registro(nombre):
    registros_actualizados = []
    whit open('registros.txt', 'r') as f:
        registros = f.readlines()
        for registro in registros:
            nombre_actual, edad_actual, telefono_actual = registro.strip().split(',')
            if nombre_actual != nombre:
                registros_actualizados.append(registro)
    whit open('registros.txt', 'w') as f:
        f.writelines(registros_actualizados)

crear_registro('Ana', 25)
leer_registros()
actualizar_registro('Ana', 26)
eliminar_registro('Ana')

