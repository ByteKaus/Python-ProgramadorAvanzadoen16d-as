print("Hola, por favor responda las siguientes dos preguntas para calcular la comision que le corresponde.")
x = input("Ingrese su nombre: ")
y = float(input("Ingrese las ventas totales realizadas en este mes: "))
z = round(y*13/100,2)
print(f"Hola {x}, la comision que le corresponde por las ventas realizadas durante este mes es de: {z} soles")