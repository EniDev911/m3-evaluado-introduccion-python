precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios = int(input("Ingresar el número de usuarios: "))
gasto_total = int(input("Ingresar el gasto total: "))

utilidades = (precio_suscripcion * numero_usuarios) - gasto_total
print("Total utilidades generadas:", utilidades)