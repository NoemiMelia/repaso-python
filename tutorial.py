print("Hola Mundo")
#Variables
texto= "Hola amigos"
nombre= "Noemi Melià"
altura= "153cm"
year= "2006"

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

#Entrada
#sitioweb = input("¿Cuál es tu página web?: ")
#print("El sitio web del usuario es: " + sitioweb)
"""
# Condiciones
altura = int(input("¿Cual es tu altura?: "))

if altura >=150:
    print("Eres medianamente alto!!")
else: 
    print("Eres un minion!!")
"""

#Funciones
"""
var_altura = int(input("¿Cuál és tu altura?: "))

def mostrarAltura(altura):
    resultado = ""
    
    if altura >=150:
     print("Eres medianamente alto!!")
    else: 
     print("Eres un minion!!")

     return resultado

print(mostrarAltura(var_altura))
"""
#Listas
personas = ["Víctor", "Paco", "Pepe"]

print(personas[1])

for persona in personas:
    print("-" + persona)
