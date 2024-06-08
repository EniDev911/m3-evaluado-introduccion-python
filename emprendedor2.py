precio_suscripcion = int(input("Ingresar el precio de suscripción: "))
numero_usuarios_normal = int(input("Ingresar el número de usuarios (normal): "))
numero_usuarios_premiun = int(input("Ingresar el número de usuarios (premium): "))
gasto_total = int(input("Ingresar el gasto total: "))

total_suscripcion_normal = precio_suscripcion * numero_usuarios_normal
total_suscripcion_premium = (precio_suscripcion * .5) * numero_usuarios_premiun

utilidades = (total_suscripcion_normal + total_suscripcion_premium) - gasto_total

print("Total utilidades generadas:", round(utilidades))