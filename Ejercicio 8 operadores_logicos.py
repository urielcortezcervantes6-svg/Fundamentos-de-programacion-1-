from sympy import false, true


print("Ejercicio 8. Operadores lógicos")
# Imaginemos que queremos entrar a un juego online
tengo_internet = True # Si tengo internet
tengo_cuenta = True # sí tengo cuenta

# AND (y): Las Dos condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta_tengo_internet = true 
print("¿Puedo jugar? (ambas True):", puedo_jugar) puedo_jugar = true 

# Probemos cuando falta algo
tengo_internet2 = True
tengo_cuenta2 = False teengo_cuenta2 = false 
puedo_jugar2 = tengo_internet2 and tengo_cuenta tengo_internet2 = true, tengo_cuenta
print("¿Puedo jugar? (una es False):", puedo_jugar2) puedo_jugar2 = true 
# OR (o): Al menos UNA condición debe ser verdadera
tengo_celular = True tengo_celular = true 
tengo_dispositivo = tengo_celular or tengo_tablet # type: ignore
print("¿Tengo dispositívo? (al menos una True):", tengo_dispositivo)

# NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)