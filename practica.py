#diccionario de estudiantes y calificaciones

#estudiantes = {"Ana": 85, "juan": 92, "Maria": 78}

#Agregar un nuevo estudiante

#estudiantes["Carlos"] = 88

#Calcular el promedio de las calificaciones

#promedio = sum(estudiantes.values()) / len(estudiantes)
#print(f'Promedio de calificaciones: {promedio:.2f}')

#Encontrar el esrudiante con la calificacion mas alta
#mejor_estudiante = max(estudiantes, key=estudiantes.get)

#promedio = sum(estudiantes.values()) / len({estudiantes[mejor_estudiante]} puntos)')
#print(f'Mejor estudiante: {mejor_estudiante:.2f}')
                                           
#ver error
#Imprimir  el estudiante con la calificacion mas alta


# funciona ok
#edad = int(input("Ingrese su edad: "))

#if 0 < edad <= 12:
#    print('Clasificación: Niño')
#elif edad >= 13 and edad <= 17:
#    print('Clasificación: Adolescente')
#elif edad >= 18 and edad <= 64:
#    print('Clasificación: Adulto')
#elif edad >= 65:
#    print('Clasificación: Adulto mayor')
#else:
#    print('Recien nacido, menor a 1 año')

#-------------------------------
#calculo de impuesto
    
#ingresos = float(input("Ingrese sus ingresos anuales: "))

#if ingresos <=10000:
#    impuestos = ingresos * 0.10
#elif ingresos <= 20000:
#    impuestos = ingresos * 0.10 + 0.20 + (ingresos - 10000)
#elif ingresos <= 30000:
#    impuestos = ingresos * 0.10 + 0.20 + (ingresos - 20000) * 0.30
#else:
#    impuestos = 10000 * 0.10 + 0.20 + 10000 * 0.30 + (ingresos - 30000) * 0.40
#print(f'Impuesto a pagar:${impuestos:.2f}')

#--------------------

#calcule e imprima los primeros 20 numeros de fibonacci
fibonacci = [0, 1]

for i in range(1, 20):
    #siguiente = fibonacci[i-1] + fibonacci[i-2]
    siguiente = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(siguiente)
print(f'Serie Fibonacci: {fibonacci}')







