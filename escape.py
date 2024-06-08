import math

constante_g = float(input("Ingrese la constante g: "))
radio = int(input("Ingrese el radio en Kilómetros: "))

velocidad_escape = round(math.sqrt(2 * (radio * 1000) * constante_g), 1 )

print("Velocidad de Escape =", str(velocidad_escape)+ " [m/s]")