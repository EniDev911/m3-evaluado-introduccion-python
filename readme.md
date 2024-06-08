<a href="https://colab.research.google.com/gist/EniDev911/7522d4bb9e0724f78e275bd67d99701a/introduccion-python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Velocidad de Escape

1. Se solicita crear un script `escape.py` que permita calcular la velocidad de escape ingresando como datos de entradas el radio `r` y la constante `g`. Los datos de entrada deben ingresarse de manera interactiva utilizando la función `input()`.

2. El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.


```python
import math

constante_g = float(input("Ingrese la constante g: "))
radio = int(input("Ingrese el radio en Kilómetros: "))

velocidad_escape = round(math.sqrt(2 * (radio * 1000) * constante_g), 1 )

print("Velocidad de Escape =", str(velocidad_escape)+ " [m/s]")
```

    Ingrese la constante g en : 9.8
    Ingrese el radio en Kilómetros: 6371
    Velocidad de Escape = 11174.6 [m/s]


## Rentabilidad

### Requerimiento 1

Crear el programa `emprendedor1.py` que utilice la fórmula descrita anteriormente para calcular las utilidades de un proyecto. Para ello utiliza `input()` para solicitar como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.


```python
precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios = int(input("Ingresar el número de usuarios: "))
gasto_total = int(input("Ingresar el gasto total: "))

utilidades = (precio_suscripcion * numero_usuarios) - gasto_total
print("Total utilidades generadas:", utilidades)
```

    Ingresar el precio de suscripción: 5000
    Ingresar el número de usuarios: 50
    Ingresar el gasto total: 120000
    Total utilidades generadas: 130000


### Requerimiento 2

Ahora nos dicen que el emprendedor considera 2 tipos de usuarios los **usuarios normales** y los **usuarios premium** a los cuales se le cobrará una suscripción un 50% mayor. Crea una segunda versión llamada `emprendedor2.py` que permita considerar el caso recién expuesto. Para ello debemos modificar lá función para que solicite mediante `input()` los siguientes parámetros de entrada:

- precio de suscripción `P`
- número de usuarios normales `U`
- número de usuarios premium `UP`
- gastos totales `GT`


```python
precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios_normal = int(input("Ingresar el número de usuarios (normal): "))
numero_usuarios_premiun = int(input("Ingresar el número de usuarios (premium): "))
gasto_total = int(input("Ingresar el gasto total: "))

total_suscripcion_normal = precio_suscripcion * numero_usuarios_normal
total_suscripcion_premium = (precio_suscripcion * .5) * numero_usuarios_premiun

utilidades = (total_suscripcion_normal + total_suscripcion_premium) - gasto_total

print("Total utilidades generadas:", round(utilidades))
```

    Ingresar el precio de suscripción: 5000
    Ingresar el número de usuarios (normal): 50
    Ingresar el número de usuarios (premium): 20
    Ingresar el gasto total: 170000
    Total utilidades generadas: 130000


### Requerimiento 3

Considera ahora una tercera versión llamada `emprendedor3.py` utilizando la formula original de utilidades donde el usuario ingrese los siguientes datos:

- precio de suscripción `P`
- número de usuarios normales `U`
- gastos totales `GT`
- utilidades periodo anterior `UA`

El programa debe calcular las utilidades actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos decimales.


```python
precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios = int(input("Ingresar el número de usuarios: "))
gasto_total = int(input("Ingresar el gasto total: "))
periodo_anterior = int(input("Ingresa las utilidades del año pasado: "))

utilidades_actuales = (precio_suscripcion * numero_usuarios) - gasto_total

la_razon = round(utilidades_actuales / periodo_anterior, 2)

print("La razón entre las utilidades actuales y las del año anterior es:", la_razon)
```

    Ingresar el precio de suscripción: 5000
    Ingresar el número de usuarios: 60
    Ingresar el gasto total: 120000
    Ingresa las utilidades del año pasado: 130000
    La razón entre las utilidades actuales y las del año anterior es: 1.38
