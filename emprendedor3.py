precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios = int(input("Ingresar el número de usuarios: "))
gasto_total = int(input("Ingresar el gasto total: "))
periodo_anterior = int(input("Ingresa las utilidades del año pasado: "))

utilidades_actuales = (precio_suscripcion * numero_usuarios) - gasto_total

la_razon = round(utilidades_actuales / periodo_anterior, 2)

print("La razón entre las utilidades actuales y las del año anterior es:", la_razon)