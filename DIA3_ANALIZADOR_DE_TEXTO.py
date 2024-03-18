texto1 = input("Ingrese un texto: ")
texto2 = texto1.lower()

print("Ahora, ingrese tres letras a su libre elección: ")
l1 = input("Ingrese la primera letra: ")
l1 = [l1.lower()]
l2 = input("Ingrese la segunda letra: ")
l2 = [l2.lower()]
l3 = input("Ingrese la tercera letra: ")
l3 = [l3.lower()]
lista = l1+l2+l3

print('1. A continuacion veremos cuantas veces aparece cada una de las letras en el texto proporcionado.')
cantidadl1 = texto2.count(lista[0])
cantidadl2 = texto2.count(lista[1])
cantidadl3 = texto2.count(lista[2])

print(f'La letra "{lista[0]}" aparece {cantidadl1} veces. \nLa letra "{lista[1]}" aparece {cantidadl2} veces. \nLa letra "{lista[2]}" aparece {cantidadl3} veces.')

print(f"2. El texto que proporcionaste tiene {len(texto1.split())} palabras.")
print(f"3. La primera letra del texto proporcionado es {texto1[0]} y la ultima letra es {texto1[-1]}")
print(f"4. El texto que proporcionado leido al reves seria lo siguiente: \n{texto1[::-1]}")
input("¿Crees que en el texto proporcionado se encuentra la palabra 'Python'?: ")
palabra = 'python' in texto2
cpalabra = texto2.count('python')
print(f"5. La respuesta es: \n{palabra}, se encuentra {cpalabra} veces")
